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