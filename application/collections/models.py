from application import db
from application.models import Base


from sqlalchemy.sql import text

class Collections(Base):

    name = db.Column(db.String(144), nullable=False)
    number = db.Column(db.String(144), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    def __init__(self, name, number, account_id):
        self.name = name
        self.number = number
        self.account_id = account_id

    @staticmethod
    def find_users_collection(id, done=0):
        stmt = text("SELECT collections.name, collections.number "
        "FROM collections LEFT JOIN account ON account.id = collections.account_id "
        "WHERE collections.account_id = :id;").params(done=done, id=id)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"number":row[0], "name":row[1]})

        return response
