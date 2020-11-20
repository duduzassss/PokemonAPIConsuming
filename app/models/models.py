from app import db

class User(db.Model):
	__tablename__ = 'users'
	
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String,unique=True, nullable=False)
	password = db.Column(db.String, nullable=False)
	pokedexs      = db.relationship('Pokedex', backref='users', lazy=True)

	@property
	def is_authenticated(self):
		return True
	
	@property
	def is_active(self):
		return True
	
	@property
	def is_anonymous(self):
		return False
	
	def get_id(self):
		return str(self.id)
	
	def __init__(self, username, password):
		self.username = username
		self.password = password
		
	def __repr__(self):
		return '<User %r>' % self.username
	
class Pokedex(db.Model):
	__tablename__ = 'pokedex'
	
	id = db.Column(db.Integer, primary_key=True)
	id_user = db.Column(db.Integer, db.ForeignKey('users.id'))
	
class ImagePokemon(db.Model):
	__tablename__ = 'images_pokemons'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String, unique=True)
	link_img = db.Column(db.String, unique=True)