from application import db
from application.models import Base

class roles(Base):

    __tablename__ = "roles"
    
    role = db.Column(db.String(144), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
	

    def __init__(self, role):
        self.role = role
