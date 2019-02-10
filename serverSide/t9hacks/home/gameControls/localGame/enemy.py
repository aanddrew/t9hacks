import random

class Enemy:
	def __init__(self):
		self.name = random.choice(['skeleton', \
									'spider', \
									'ghoul',\
									'zombie'])
		self.health = 50

	def getDamage(self):
		return random.randint(6,20)