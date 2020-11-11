from app import db

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String,unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    pet      = db.Column(db.String)

    def __init__(self, username, password):
        self.username = username
        self.password = password
        
    def __repr__(self):
        return '<User %r>' % self.username
    
class Pokedex(db.Model):
    __tablename__ = 'pokedex'
    
    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    user = db.relationship('User', foreign_key=id_user)