from application import db
from application.models import Base


from sqlalchemy.sql import text

class Collections(Base):

    name = db.Column(db.String(144), nullable=False)
    number = db.Column(db.Integer(), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    def __init__(self, name, number):
        self.name = name
        self.number = number

    @staticmethod
    def find_users_collection():
        stmt = text("SELECT collections.name, collections.number "
        "FROM collections LEFT JOIN account ON account.id = collections.account_id "
        "WHERE collections.account_id = 1;")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"number":row[0], "name":row[1]})

        return response
