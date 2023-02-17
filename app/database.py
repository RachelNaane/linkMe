import os
from pymongo import MongoClient
from flask import current_app as app

mongo_hostname = os.environ.get('MONGO_HOSTNAME')
mongo_user = os.environ.get('MONGO_USER')
mongo_password = os.environ.get('MONGO_PASSWORD')

connected=False

try:
    client = MongoClient(mongo_hostname,27017,username=mongo_user, password=mongo_password, serverSelectionTimeoutMS=3000)
    db = client.data
    links = db.links    
    connected=True
except:
    app.logger.critical('no database connection!!')
    connected=False

## template
# link = {
#     "url": "https://www.google.com/",
#     "tag": "google",
#     "description": "a link to google search"
# }

def add_link(url, tag, description):
    if connected:
        links.insert_one({"url": url,"tag": tag, "description": description})
        app.logger.info('link added')
        return True
    return False

def delete_link(id):
    if connected:
        from bson.objectid import ObjectId
        _id = ObjectId(id)
        links.delete_one({"_id": _id})
        return True
    return False

def get_links():
    if connected:
        return links.find({})
    
def get_link_by_id(id):
    if connected:
        from bson.objectid import ObjectId
        _id = ObjectId(id)
        return links.find_one({"_id": _id})

def edit_link(id, new_url, new_tag, new_description):
    if connected:
        from bson.objectid import ObjectId
        _id = ObjectId(id)
        links.update_one({"_id": _id}, {"$set": {"url": new_url, "tag": new_tag, "description": new_description}})
        return True
    return False