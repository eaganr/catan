from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dbinfo import IP, USER, PASSWORD, DB


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://%s:%s@%s/%s' % (USER,PASSWORD,IP,DB)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# print('mysql://%s:%s@%s/%s' % (USER,PASSWORD,IP,DB))
db = SQLAlchemy(app)

class Game(db.Model):
	__tablename__ = 'game'
	game_id = db.Column('game_id',db.Integer,primary_key = True)
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

	
games = Game.query.all()
for item in games:
	print(item.game_id)