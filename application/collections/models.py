from application import db
from application.models import Base


from sqlalchemy.sql import text

class Collections(Base):

    name = db.Column(db.String(144), nullable=False)
    number = db.Column(db.String(144), nullable=False)
    caught = db.Column(db.Integer(), nullable=False)
    imgLink = db.Column(db.String(144), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    def __init__(self, name, number, account_id, imgLink):
        self.name = name
        self.number = number
        self.caught = 0
        self.imgLink = imgLink
        self.account_id = account_id

    @staticmethod
    def find_users_collection(id, done=0):
        stmt = text("SELECT collections.number, collections.name, collections.caught, collections.id, collections.imgLink "
        "FROM collections LEFT JOIN account ON account.id = collections.account_id "
        "WHERE collections.account_id = :id;").params(done=done, id=id)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"number":row[0], "name":row[1], "caught":row[2], "id":row[3], "imgLink":row[4]})

        return response

    @staticmethod
    def how_many_caught(id, done=0):
        stmt = text("SELECT count(*) "
        "FROM collections LEFT JOIN account ON account.id = collections.account_id "
        "WHERE collections.caught = 1 AND collections.account_id = :id;").params(done=done, id=id)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({row[0]})

        return response

