from flask import Blueprint, render_template, request, flash, redirect
import json
import database as db
from bson import json_util

views =  Blueprint('views', __name__)

@views.route('/', methods= ['GET', 'POST'])
def home():
    if request.method == 'POST':
        url = request.form.get('url')
        tag = request.form.get('tag')
        description = request.form.get('description')

        if len(url) < 1:
            flash("link can't be blank", category='error')
        elif len(tag) < 1:
            flash("name can't be blank", category='error')
        elif len(description) < 1:
            flash("description can't be blank", category='error')
        else:
            success = db.add_link(url,tag,description)
            if success:
                flash("link added successfully", category='success')
            else:
                flash("sorry...could not add link, try again later", category='error')
    return render_template("home.html")

@views.route('/get-links', methods= ['GET'])
def get_links():
    links = db.get_links()
    return json.dumps(list(links),default=json_util.default)

@views.route('/delete-link/<id>')
def delete_link(id):
    db.delete_link(id)
    return redirect("/")

@views.route('/edit-link/<id>', methods = ['POST', 'GET'])
def edit_link(id):
    if request.method == 'POST':
        id = request.form.get('id')
        new_url = request.form.get('url')
        new_tag = request.form.get('tag')
        new_description = request.form.get('description')
        
        if len(new_url) < 1:
            flash("link can't be blank", category='error')
        elif len(new_tag) < 1:
            flash("name can't be blank", category='error')
        elif len(new_description) < 1:
            flash("description can't be blank", category='error')
        else:
            db.edit_link(id, new_url, new_tag, new_description)
            return render_template("home.html")

    link=db.get_link_by_id(id)
    return render_template("editor.html", link=link, id=id)
    
@views.route('/health')
def is_healthy():
    return 'OK', 200

# @views.route("/test")
# def test():
#     try:
#         mongo_hostname = os.environ.get('MONGO_HOSTNAME')
#         mongo_user = os.environ.get('MONGO_USER')
#         mongo_password = os.environ.get('MONGO_PASSWORD')

#         client = MongoClient(mongo_hostname,27017,username=mongo_user, password=mongo_password)
#         db = client.data
#         test = db.test
#         test.insert_one({ "test": "this is a test" })
#         res = test.find()
#         for r in res:
#             re = r
#         return f"{re}"
#     except:
#         return f"{mongo_hostname}-{mongo_user}-{mongo_password}"