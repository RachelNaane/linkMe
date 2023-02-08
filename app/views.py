from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
import json
import database as db

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

    user_notes = db.get_user_notes(current_user.id)
    return render_template("home.html", user=current_user, notes = user_notes)

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