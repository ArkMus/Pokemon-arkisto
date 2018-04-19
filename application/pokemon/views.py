from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db
from application.pokemon.models import Pokemons
from application.pokemon.forms import PokeForm
from application.roles.views import isAdmin


@app.route("/pokemon/all/", methods=["GET"])
def all_pokemon():
    return render_template("pokemon/all.html", pokemons=Pokemons.query.all(), isAdmin=isAdmin())



@app.route("/pokemon/new/")
@login_required
def new_form():
    error = None
    if request.method == "GET":
        if isAdmin():        
            return render_template("pokemon/new.html", form = PokeForm())
        else:
            return redirect(url_for("all_pokemon"))

@app.route("/pokemon/", methods=["POST"])
def pokemon_new():
    if isAdmin():
        return redirect(url_for("all_pokemon"))
    form = PokeForm(request.form)

    new_poke = Pokemons(form.name.data, form.number.data) 

    db.session().add(new_poke)
    db.session().commit()
    return redirect(url_for("all_pokemon"))