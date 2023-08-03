#STANDARD roots where the users will go.
from flask import Blueprint,render_template,request,flash, jsonify
from flask_login import login_required,current_user
from .models import Note
from . import db
import json
# from website import data



views = Blueprint('views', __name__)

@views.route('/', methods=['GET','POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note') #getting the note from the form

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note) #adding new note to the database
            db.session.commit() #commiting the changes to the database
            flash('Note added!', category='success')
    return render_template("home.html", user=current_user)

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data) #getting the note from the request
    noteId = note['noteId'] #getting the note id from the note
    note = Note.query.get(noteId) #getting the note by id
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
    return jsonify({}) #returning an empty json object