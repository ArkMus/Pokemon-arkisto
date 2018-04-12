from application import db
from application.models import Base

class Pokemons(Base):

    name = db.Column(db.String(144), nullable=False)
    number = db.Column(db.Integer(), nullable=False)
	

    def __init__(self, name, number):
        self.name = name
        self.number = number
