from flask import Blueprint, render_template, request, flash, redirect, url_for
import re
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
import database as db

auth =  Blueprint('auth', __name__)

@auth.route('/login', methods= ['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        try:
            user = db.get_user_by_mail(email) 
        except:
            flash('sorry, we seem to have a problem. please try again later', category='error') 
            return render_template("login.html", user=current_user) 

        if user and check_password_hash(user['password'], password):
            user_id = user['_id']
            import user
            logger = user.User(str(user_id))
            login_user(logger, remember=True)
            flash('welcome back', category='success')
            return redirect(url_for('views.home'))
        else:
            flash('Incorrect email or password, try again', category='error')

    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/register', methods= ['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        email_pattern = r'^(?:[a-z0-9!#$%&\'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&\'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])$'
        try:
            if  db.get_user_by_mail({"email": email}):
                flash('email already exists', category='error')
            elif not re.search(email_pattern, email):
                flash('not a valid email address', category='error')
            elif len(name) < 2:
                flash('name needs to be longer than 1 character', category='error')
            elif len(password1) < 6:
                flash('password most be at least 6 characters', category='error')
            elif password1 != password2:
                flash('passwords do not match', category='error')
            else:
                new_user = {"name": name, "password": generate_password_hash(password1, method='sha256'), "email":email} #TODO: understand hash
                user_id = db.add_user(new_user)
        except:
            flash('sorry, we seem to have a problem. please try again later', category='error')
            return render_template("register.html", user=current_user)

        import user 
        logger = user.User(str(user_id))
        login_user(logger, remember=True)
        flash('account created!', category='success')
        return redirect(url_for('views.home'))
        
    return render_template("register.html", user=current_user)