from flask import Flask
from os import path
from flask_login import LoginManager
import os
import database as db

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

from views import views
from auth import auth

app.register_blueprint(views, url_prefix='/')
app.register_blueprint(auth, url_prefix='/')

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

import user

@login_manager.user_loader
def load_user(id):
    u = db.get_user_by_id(id)
    if not u:
        return None
    return user.User(id=id)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=3000) #TODO: off in production