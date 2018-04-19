from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db
from application.roles.models import roles



def isAdmin():
    role = roles.query.filter_by(account_id = current_user.id).first()
    
    if role and role.role == "ADMIN":
        print(role.role)
        return True
    return False
