from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
import json
import database as db
from bson import json_util
from pymongo import MongoClient
import os

views =  Blueprint('views', __name__)

@views.route('/', methods= ['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash("note can't be blank", category='error')
        else:
            db.add_note(user_id=current_user.id, text=note)
            flash("note added successfully", category='success')
    
    if not db.is_connected():
        return render_template("nodb.html", user=current_user)
    return render_template("home.html", user=current_user)

@views.route('/get-notes', methods= ['GET'])
def get_notes():
    notes = db.get_user_notes(current_user.id)
    return json.dumps(list(notes),default=json_util.default)

@views.route('/delete-note', methods= ['POST'])
def delete_note():
    data = json.loads(request.data)
    noteId = data['noteId']
    db.delete_note(noteId)
    return jsonify({})

@views.route('/edit_note', methods = ['PUT'])
def edit_note():
    data = json.loads(request.data)
    noteId = data['noteId']
    new_note = data['newNote']
    db.edit_note(noteId, new_note)
    return jsonify({})

@views.route('/health')
def is_healthy():
    return 'OK', 200

@views.route("/test")
def test():
    try:
        mongo_hostname = os.environ.get('MONGO_HOSTNAME')
        mongo_user = os.environ.get('MONGO_USER')
        mongo_password = os.environ.get('MONGO_PASSWORD')

        client = MongoClient(mongo_hostname,27017,username=mongo_user, password=mongo_password)
        db = client.data
        test = db.test
        test.insert_one({ "test": "this is a test" })
        res = test.find()
        for r in res:
            re = r
        return f"{re}"
    except:
        return f"{mongo_hostname}-{mongo_user}-{mongo_password}"