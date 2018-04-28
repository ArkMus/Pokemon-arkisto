from application import db
from application.models import Base

class Pokemons(Base):

    name = db.Column(db.String(144), nullable=False)
    number = db.Column(db.String(144), nullable=False)
    imgLink = db.Column(db.String(144), nullable=False)
    

    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.imgLink = "https://img.pokemondb.net/sprites/x-y/normal/"+ name.lower() +".png"
