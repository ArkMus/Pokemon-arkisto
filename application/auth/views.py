from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user
  
from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm, RegisterForm
from werkzeug.security import generate_password_hash, check_password_hash

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)
    # mahdolliset validoinnit

    user = User.query.filter_by(username=form.username.data).first()
    
    if not check_password_hash(user.password, form.password.data):
        return render_template("auth/loginform.html", form = form,
                                error = "Wrong password")

    if not user:
        return render_template("auth/loginform.html", form = form,
                                error = "No such username or password")


    login_user(user)
    return redirect(url_for("index"))    

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index")) 

@app.route("/auth/register", methods=["GET", "POST"])
def auth_register():
    error = None
    if request.method == "GET":
        return render_template("auth/registerform.html", form = RegisterForm())

    form = RegisterForm(request.form)

    if not form.validate():
        return render_template("auth/registerform.html", form = form, 
        error = "Password has to be at least 8 characters")

    que = User.query.filter_by(username = form.username.data).first()
    if not que:
        new_User = User(name = form.name.data, username = form.username.data, password = generate_password_hash(form.password.data))
        db.session().add(new_User)
        db.session().commit()
        return redirect(url_for("auth_login"))
    
    return render_template("auth/registerform.html", form = form,
                                error = "Username already in use")