from tables import *
from sqlalchemy import table, column, select, update, insert, and_
import datetime
import logging
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

SETTLEMENT_LIMIT = 5
CITY_LIMIT = 4 
ROAD_LIMIT = 20
RESOURCE_MAX = 19
KNIGHT_MAX = 14
VP_CARD_MAX = 5
PROGRESS_CARD_MAX = 2



def initializeUserAssets(user_id, game_id):
	# Tie Assets to User, create using default values of 0
	cards = Cards(user_id,game_id)
	limits = Limits(user_id,game_id)
	resources = Resources(user_id,game_id)
	db.session.add(cards)
	db.session.add(limits)
	db.session.add(resources)
	db.session.commit()


class GameSetup:
	playerone = 0
	playertwo = 0
	playerthree = 0
	playerfour = 0
	game_id = 0

	def __init__(self,playerone=0,playertwo=0,playerthree=0,playerfour=0):
		# Initialize game user and get master ID from that
		self.playerone = playerone
		self.playertwo = playertwo
		self.playerthree = playerthree
		self.playerfour = playerfour

	def initializeGame(self):
		# Generate the game object for database write
		game = Game(self.playerone,self.playertwo,self.playerthree,self.playerfour)
		db.session.add(game)
		db.session.commit()
		self.game_id = game.game_id
		# Generate the master game cards and resources
		cards = Cards(0,game.game_id,VP_CARD_MAX,KNIGHT_MAX,
			PROGRESS_CARD_MAX,PROGRESS_CARD_MAX,PROGRESS_CARD_MAX)
		resources = Resources(0,game.game_id,RESOURCE_MAX,RESOURCE_MAX,
			RESOURCE_MAX,RESOURCE_MAX,RESOURCE_MAX)
		db.session.add(resources)
		db.session.add(cards)
		db.session.commit()
		# Add Vertex and Edge Information? Not sure if we should insert

		#Insert the user assets below
		for i in [self.playerone,self.playertwo,self.playerthree,self.playerfour]:
			if(i >= 0):
				initializeUserAssets(i,self.game_id)

def updateResource(u_id, g_id,resourcetype = [],quantity = []):

	resourceArray = ['wood','ore','wheat','sheep','brick']
	toupdate = Resources.query.filter(and_(Resources.user_id == u_id, Resources.game_id == g_id)).first()
	gameupdate = Resources.query.filter(and_(Resources.user_id == 0, Resources.game_id == g_id)).first()
	
	for r,q in zip(resourcetype,quantity):
		if r == resourceArray[0]:
			toupdate.wood = toupdate.wood + q
			gameupdate.wood = gameupdate.wood - q

		elif r == resourceArray[1]:
			toupdate.ore = toupdate.ore + q
			gameupdate.ore = gameupdate.ore - q

		elif r == resourceArray[2]:
			toupdate.wheat = toupdate.wheat + q
			gameupdate.wheat = gameupdate.wheat - q

		elif r == resourceArray[3]:
			toupdate.sheep = toupdate.sheep + q
			gameupdate.sheep = gameupdate.sheep - q

		elif r == resourceArray[4]:
			toupdate.brick = toupdate.brick + q
			gameupdate.brick = gameupdate.brick - q
		else:
			None
	db.session.commit()

def updateCards(u_id, g_id,cardtype = [],quantity = []):

	cardArray = ['victorypoints','knights','yearofplenty','monopoly','roadbuilder']
	toupdate = Cards.query.filter(and_(Cards.user_id == u_id, Cards.game_id == g_id)).first()
	gameupdate = Cards.query.filter(and_(Cards.user_id == 0, Cards.game_id == g_id)).first()
	for c, q in zip(cardtype, quantity):
		if c == cardArray[0]:
			toupdate.victorypoints = toupdate.victorypoints + q
			gameupdate.victorypoints = gameupdate.victorypoints - q

		elif c == cardArray[1]:
			toupdate.knights = toupdate.knights + q
			gameupdate.knights = gameupdate.knights - q

		elif c == cardArray[2]:
			toupdate.yearofplenty = toupdate.yearofplenty + q
			gameupdate.yearofplenty = gameupdate.yearofplenty - q

		elif c == cardArray[3]:
			toupdate.monopoly = toupdate.monopoly + q
			gameupdate.monopoly = gameupdate.monopoly - q

		elif c == cardArray[4]:
			toupdate.roadbuilder = toupdate.roadbuilder + q
			gameupdate.roadbuilder = gameupdate.roadbuilder - q
		else:
			None
	db.session.commit()


# class UserAssets:
# 	def __init__(self,user_id = 0,game_id = 0):
# 		self.user_id = user_id
# 		self.game_id = game_id

# Initialize the assets for a user. If it's a master user then the master user must 
# first be created. This will be user

# initialsetup = GameSetup(1,2,3,4)
# initialsetup.initializeGame()
updateResource(2,1,['wood','ore'],[4,-2])
# updateCards(1,13,['knights'],[1])

# print (initialsetup.game_id)

