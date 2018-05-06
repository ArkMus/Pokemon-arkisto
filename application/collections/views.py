from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db
from application.collections.models import Collections
from application.pokemon.forms import PokeForm

@app.route("/collections/user/", methods=["GET"])
@login_required
def all_collections():
    return render_template("collections/user.html", user_collection=Collections.find_users_collection(current_user.id), user_count=Collections.how_many_caught(current_user.id))

@app.route("/collections/user/<pokeid>/", methods=["POST"])
def pokemon_set_caught(pokeid):
    poke = Collections.query.filter_by(id=pokeid).first()
    if poke.caught == 1:
        poke.caught = 0
    else:
        poke.caught = 1
    db.session().commit()

    return redirect(url_for("all_collections"))

@app.route("/collections/remove/", methods=["GET", "POST"])
@app.route("/collections/remove/<pokeid>", methods=["GET", "POST"])
@login_required
def remove_pokemon(pokeid):
    pokeToDelete = Collections.query.filter_by(id=pokeid).first()

    if request.method == "GET":
        return render_template("collections/remove.html", pokeid = pokeid, pokemon=pokeToDelete)
    

    db.session.delete(pokeToDelete)
    db.session().commit()

    return redirect(url_for("all_collections"))

@app.route("/collections/rename/", methods=["GET", "POST"])
@app.route("/pokemon/rename/<pokeid>", methods=["GET", "POST"])
@login_required
def rename_pokemon(pokeid):

    pokeToRename = Collections.query.filter_by(id=pokeid).first() 
    form = PokeForm()
    form.name.data = pokeToRename.name
    
    if request.method == "GET":
        return render_template("collections/rename.html", pokeid = pokeid, pokemon=pokeToRename, form=form)
        
    form = PokeForm(request.form)

    pokeToRename.name = form.name.data
    
    db.session().commit()

    return redirect(url_for("all_collections"))