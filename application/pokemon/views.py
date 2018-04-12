from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db
from application.pokemon.models import Pokemons


@app.route("/pokemon/all/", methods=["GET"])
def all_pokemon():
    return render_template("pokemon/all.html", pokemons = Pokemons.query.all())
