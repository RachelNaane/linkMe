from dotenv import load_dotenv, find_dotenv
import os
from pymongo import MongoClient

load_dotenv(find_dotenv())
connection_string = os.environ.get('DB_URI')

client = MongoClient(connection_string)
db = client.data
users = db.users
notes = db.notes

## duocument templates: ##
# user = {
#     "name": "rachel",
#     "email": "ratash3@gamil.com",
#     "password": "123456"
# }

# note = {
#     "text": "my first note",
#     "user_id": "768790531br456"
# }

#users collection functions
def add_user(user):
    return users.insert_one(user).inserted_id

def get_user(email, password):
    return users.find_one({"email": email, "password": password})

def get_all_users():
    return users.find()

def get_user_by_mail(email):
    return users.find_one({"email": email})

def get_user_by_id(id):
    from bson.objectid import ObjectId
    _id = ObjectId(id)
    return users.find_one({"_id": _id})

#notes collection functions
def add_note(user_id, text):
    from bson.objectid import ObjectId
    _id = ObjectId(user_id)
    notes.insert_one({"text": text, "user_id": _id})

def get_user_notes(user_id):
    from bson.objectid import ObjectId
    _id = ObjectId(user_id)
    return notes.find({"user_id": _id})

def get_note_by_id(id):
    from bson.objectid import ObjectId
    _id = ObjectId(id)
    return notes.find_one({"_id": _id})

def delete_note(id):
    from bson.objectid import ObjectId
    _id = ObjectId(id)
    notes.delete_one({"_id": _id})

def edit_note(id, new_text):
    from bson.objectid import ObjectId
    _id = ObjectId(id)
    notes.update_one({"_id": _id}, {"$set": {"text": new_text}})