from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db
from application.pokemon.models import Pokemons
from application.pokemon.forms import PokeForm
from application.roles.views import isAdmin


@app.route("/pokemon/all/", methods=["GET"])
def all_pokemon():
    return render_template("pokemon/all.html", pokemons=Pokemons.query.order_by('number').all(), isAdmin=isAdmin())


@app.route("/pokemon/new", methods=["GET", "POST"])
def pokemon_new():
    if request.method == "GET":
        if isAdmin():        
            return render_template("pokemon/new.html", form = PokeForm())
        else:
            return redirect(url_for("all_pokemon"))

    if not isAdmin():
        return redirect(url_for("all_pokemon"))
        
    form = PokeForm(request.form)

    new_poke = Pokemons(form.name.data, form.number.data) 

    db.session().add(new_poke)
    db.session().commit()
    return redirect(url_for("all_pokemon"))

@app.route("/pokemon/edit/", methods=["GET", "POST"])
@app.route("/pokemon/edit/<pokeid>", methods=["GET", "POST"])
def edit_pokemon(pokeid):

    pokeToEdit = Pokemons.query.filter_by(id=pokeid).first() 

    if request.method == "GET":
        if isAdmin():        
            return render_template("pokemon/edit.html", pokeid = pokeid, pokemon=pokeToEdit, form = PokeForm())
        else:
            return redirect(url_for("all_pokemon"))
        
    
    if not isAdmin():
        return redirect(url_for("all_pokemon"))

    form = PokeForm(request.form)

    pokeToEdit.name = form.name.data
    pokeToEdit.number = form.number.data
    
    db.session().commit()

    return redirect(url_for("all_pokemon"))

@app.route("/pokemon/delete/", methods=["GET", "POST"])
@app.route("/pokemon/delete/<pokeid>", methods=["GET", "POST"])
def delete_pokemon(pokeid):
    pokeToDelete = Pokemons.query.filter_by(id=pokeid).first()

    if request.method == "GET":
        if isAdmin():        
            return render_template("pokemon/delete.html", pokeid = pokeid, pokemon=pokeToDelete)
        else:
            return redirect(url_for("all_pokemon"))
    
    if not isAdmin():
        return redirect(url_for("all_pokemon"))

    db.session.delete(pokeToDelete)
    db.session().commit()

    return redirect(url_for("all_pokemon"))

