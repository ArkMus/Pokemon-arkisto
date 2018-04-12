from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db
from application.collections.models import Collections


@app.route("/collections/user/", methods=["GET"])
def all_collections():
    return render_template("collections/user.html", user_collection=Collections.find_users_collection())
