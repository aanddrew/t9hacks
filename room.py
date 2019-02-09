import random

class Room:

	#direction is the direction this room is being created from.
	#i.e if the player moved into the room by moving west,
	#	the direction would be east
	def __init__(self):
		self.explored = False
		self.enemyAlive = random.choice([True,False])
		self.treasure = random.choice([True,False])
		self.message = "There's "
		if (self.enemyAlive):
			self.message += "an enemy in the room"
		else:
			self.message += "nothing in the room"