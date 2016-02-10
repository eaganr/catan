from tables import *
import datetime

class GameSetup:
	playerone = 0
	playertwo = 0
	playerthree = 0
	playerfour = 0
	master_user = 0

	def __init__(self,playerone,playertwo,playerthree,playerfour):
		masterUserAssets = UserAssets()
		self.master_user = masterUserAssets.intializeMasterAssets(),
		self.playerone = playerone,
		self.playertwo = playertwo,
		self.playerthree = playerthree,
		self.playerfour = playerfour

	def initializeGame(self):
		# Generate the game object for database write
		game = Game(game_id,playerone,playertwo,playerthree,playerfour)
		db.session.add(game)
		db.session.commit

class UserAssets:
	def __init__(self,user_id = 0,game_id = 0):
		self.user_id = user_id
		self.game_id = game_id

# Initialize the assets for a user. If it's a master user then the master user must 
# first be created. This will be user
	def intializeMasterAssets(self):
		# Initialize the game user
			user = User('Game at ' + str(datetime.datetime.now()),
				str(datetime.datetime.now()))
			db.session.add(user)
			db.session.commit()
			print(user.user_id)
			return user.user_id

	def initializeAssets(self):
		# Tie Assets to User
			
		return None

initialsetup = GameSetup(1,2,3,4)
print (GameSetup.master_user)