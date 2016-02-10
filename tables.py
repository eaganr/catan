from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dbinfo import IP, USER, PASSWORD, DB

# SETTLEMENT_LIMIT = 5
# CITY_LIMIT = 4 
# ROAD_LIMIT = 20
# RESOURCE_MAX = 19
# KNIGHT_MAX = 14
# VP_CARD_MAX = 5
# PROGRESS_CARD_MAX = 2

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://%s:%s@%s/%s' % (USER,PASSWORD,IP,DB)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# print('mysql://%s:%s@%s/%s' % (USER,PASSWORD,IP,DB))
db = SQLAlchemy(app)

class User(db.Model):
	__tablename__ = 'user'
	user_id = db.Column('user_id',db.Integer,primary_key = True)
	username = db.Column('username',db.Unicode)
	password = db.Column('password',db.Unicode)

	def __init__(self, username, password):
		self.username = username
		self.password = password

class Game(db.Model):
	__tablename__ = 'game'
	game_id = db.Column('game_id',db.Integer,primary_key = True, autoincrement = True)
	game_user_id = db.Column('game_user_id', db.Integer)
	playerone = db.Column('playerone', db.Integer)
	playertwo = db.Column('playertwo', db.Integer)
	playerthree = db.Column('playerthree', db.Integer)
	playerfour = db.Column('playerfour', db.Integer)
	playeronevp = db.Column('playeronevp', db.Integer)
	playertwovp = db.Column('playertwovp', db.Integer)
	playerthreevp = db.Column('playerthreevp', db.Integer)
	playerfourvp = db.Column('playerfourvp', db.Integer)
	largestarmy = db.Column('largestarmy', db.Integer)
	longestroad = db.Column('longestroad', db.Integer)
	currentturn = db.Column('currentturn', db.Integer)
	winner = db.Column('winner', db.Integer)

	def __init__(self, game_user_id, playerone = 0, playertwo = 0, playerthree = 0,
		playerfour = 0, playeronevp = 0, playertwovp = 0, playerthreevp = 0, playerfourvp = 0,
		largestarmy = 0, longestroad  = 0, currentturn  = 0, winner  = 0):
		# self.game_id = None 
		self.game_user_id = game_user_id
		self.playerone = playerone
		self.playertwo = playertwo
		self.playerthree = playerthree
		self.playerfour = playerfour
		self.playeronevp = playeronevp
		self.playertwovp = playertwovp
		self.playerthreevp = playerthreevp
		self.playerfourvp = playerfourvp
		self.largestarmy = largestarmy
		self.longestroad = longestroad
		self.currentturn = currentturn
		self.winner = winner

class Cards(db.Model):
	__tablename__ = 'cards'
	card_id = db.Column('card_id',db.Integer,primary_key = True)
	user_id = db.Column('user_id',db.Integer)
	game_id = db.Column('game_id',db.Integer)
	victorypoints = db.Column('victorypoints',db.Integer)
	knights = db.Column('knights',db.Integer)
	yearofplenty = db.Column('yearofplenty',db.Integer)
	monopoly = db.Column('monopoly',db.Integer)
	roadbuilder = db.Column('roadbuilder',db.Integer)

	def __init__(self, user_id, game_id, victorypoints = 0, knights = 0,
		yearofplenty = 0, monopoly = 0, roadbuilder = 0):
		self.user_id  = user_id 
		self.game_id = game_id
		self.victorypoints = victorypoints
		self.knights = knights
		self.yearofplenty = yearofplenty
		self.monopoly = monopoly
		self.roadbuilder = roadbuilder

class Limits(db.Model):
	__tablename__ = 'limits'
	limit_id = db.Column('limit_id',db.Integer,primary_key = True)
	user_id = db.Column('user_id',db.Integer)
	game_id = db.Column('game_id',db.Integer)
	roads = db.Column('roads',db.Integer)
	settlements = db.Column('settlements',db.Integer)
	cities = db.Column('cities',db.Integer)

	def __init__(self, user_id, game_id, roads = 0, settlements = 0,
		cities = 0, monopoly = 0, roadbuilder = 0):
		
		self.user_id = user_id
		self.game_id = game_id
		self.roads = roads
		self.settlements = settlements
		self.cities = cities

class Resources(db.Model):
	__tablename__ = 'resources'
	resource_id = db.Column('resource_id',db.Integer,primary_key = True)
	user_id = db.Column('user_id',db.Integer)
	game_id = db.Column('game_id',db.Integer)
	wood = db.Column('wood',db.Integer)
	ore = db.Column('ore',db.Integer)
	wheat = db.Column('wheat',db.Integer)
	sheep = db.Column('sheep',db.Integer)
	brick = db.Column('brick',db.Integer)

	def __init__(self, game_id, user_id, wood = 0, ore = 0,
		wheat = 0, sheep = 0, brick = 0):
		
		self.user_id = user_id
		self.game_id = game_id
		self.wood = wood
		self.ore = ore
		self.wheat = wheat
		self.sheep = sheep
		self.brick = brick

class Vertex(db.Model):
	__tablename__ = 'vertex'
	vertex_id = db.Column('vertex_id',db.Integer,primary_key = True)
	user_id = db.Column('user_id',db.Integer)
	game_id = db.Column('game_id',db.Integer)
	type = db.Column('type',db.Unicode)
	roll1 = db.Column('roll1',db.Integer)
	roll2 = db.Column('roll2',db.Integer)
	roll3 = db.Column('roll3',db.Integer)

	def __init__(self, game_id, user_id, type = '', roll1 = 0,
		roll2 = 0, roll3 = 0):
		
		self.user_id = user_id
		self.game_id = game_id
		self.type = type
		self.roll1 = roll1
		self.roll2 = roll2
		self.roll3 = roll3

class Edge(db.Model):
	__tablename__ = 'edge'
	edge_id = db.Column('edge_id',db.Integer,primary_key = True)
	user_id = db.Column('user_id',db.Integer)
	game_id = db.Column('game_id',db.Integer)
	type = db.Column('type',db.Unicode)

	def __init__(self, game_id, user_id, type = ''):
		
		self.user_id = user_id
		self.game_id = game_id
		self.type = type


# games = Game.query.filter_by(game_id = 1).first()
# games.playerone = 2342342
# db.session.commit()
# print(games.playerone)
# user = User('Matt','test')
# db.session.add(user)
# db.session.commit()
