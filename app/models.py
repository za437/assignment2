import hashlib
import uuid

from flask_login import UserMixin
from sqlalchemy import sequence

from app import db


db.create_all()


class LoginUser(db.Model, UserMixin):
    __tablename__ = 'user'

    username = db.Column(db.String(120), unique=True, nullable=False, primary_key=True)
    mfa = db.Column(db.String(80), nullable=False)
    authenticated = db.Column(db.Boolean, default=False)
    pw_hash = db.Column(db.String)

    def is_active(self):
        return True

    def get_id(self):
        return self.username

    def is_authenticated(self):
        return self.authenticated

    def is_anonymous(self):
        return False

    def set_password(self, password):
        self.pw_salt = uuid.uuid4().hex
        self.pw_hash = hashlib.sha256(password.encode('utf-8') + self.pw.salt.encode('utf-8')).hexdigest()
        
    def check_password(self, password):
        temp_pw = hashlib.sha256(password.encode('utf-8') + self.pw_sale.encode('utf-8')).hexdigest()
        return temp_pw == self.pw_hash
    
    class SpellCheck(db.Model):
        __tablename__ = 'spell'
        
        query_id = db.Column(db.Integer, Sequence('query_id_seq'), primary_key=True)
        spell_query = db.Column(db.String, default=None)
        spell_result = db.Column(db.String, default=None)
        user_id = db.Column(db.String, db.ForeignKey('user.username'),
                            nullable=True)
