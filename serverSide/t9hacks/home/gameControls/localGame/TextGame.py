from . import map
import random

class Game:

	def __init__(self):
		self.x = 25
		self.y = 25

		self.m = map.Map(50)

		self.player_health = 100
		self.gold_coins = 0
		self.kill_count = 0

		self.player_damage = 0
		self.enemy_damage = 0

		self.gained_health = 0
		self.gained_coins = 0

		self.gotAttacked = False
		self.attackerName = ""
		self.outputCode = 1
		#self.outputCode is a determining factor in what the output message is:
		"""
			Here are the codes:
			0 - invalid input
			0.5 - move command, no direction parameter
			1 - move command, player is now in new room
			2 - player attacked, but there was no enemy
			3 - player attacked, killed enemy
			4 - player attacked, enemy still alive
			5 - show stats
			6 - loot the treasure
			7 - loot the treasure, but there is no treasure in here
		"""
		self.current_room = self.m.rooms[self.x][self.y]
		while (self.current_room == None):
			self.x += 1
			self.current_room = self.m.rooms[self.x][self.y]
		self.current_room.enemyAlive = False
		self.current_room.enemy = None

	def done(self):
		return self.player_health <= 0

	def update(self):
		# print("updating")
		self.current_room = self.m.rooms[self.x][self.y]

	def input(self, input):
		self.gotAttacked = False
		passive = False
		commands = []
		temp = ""
		#parse user commands as a string with commands separated by spaces
		for i, char in enumerate(input):
			if char == " ":
				commands.append(temp)
				temp = ""
			else:
				temp += char
				# print(temp)
		commands.append(temp.lower())

		#select action given the commands user gave
		#moving 
		if commands[0] == "move":
			if len(commands) == 1:
				self.outputCode = 0.5
			elif commands[1] == "north" and self.m.rooms[self.x][self.y-1] != None:
				self.y -= 1
				self.outputCode = 1
			elif commands[1] == "south" and self.m.rooms[self.x][self.y+1] != None:
				self.y += 1
				self.outputCode = 1
			elif commands[1] == "west" and self.m.rooms[self.x-1][self.y] != None:
				self.x -= 1
				self.outputCode = 1
			elif commands[1] == "east" and self.m.rooms[self.x+1][self.y] != None:
				self.x += 1
				self.outputCode = 1
			else: 
				self.outputCode = 0
		#attacking
		elif commands[0] == "attack":
			if (self.current_room.enemyAlive):
				self.player_damage = random.randint(10,40)
				self.current_room.enemy.health -= self.player_damage

				if self.current_room.enemy.health <= 0:
					self.outputCode = 3
					self.current_room.enemyAlive = False;
					self.kill_count += 1
				else:
					self.outputCode = 4
			else:
				self.outputCode = 2
		elif commands[0] == "treasure":
			if (self.current_room.treasure):
				self.outputCode = 6
				self.gained_health = 0
				self.gained_coins = 0
				if random.choice([True,False]):
					self.gained_health = random.randint(10,20)
				if random.choice([True,False]):
					self.gained_coins = random.randint(1,3)
				self.player_health += self.gained_health
				self.gold_coins += self.gained_coins
				self.current_room.treasure = False
			else:
				self.outputCode = 7

		#displaying stats
		elif commands[0] == "stats":
			self.outputCode = 5
			passive = True
		else:
			self.outputCode = False
		if (not passive and self.current_room.enemyAlive and self.outputCode != 0):
			self.gotAttacked = True
			self.enemy_damage = self.current_room.enemy.getDamage()
			self.player_health -= self.enemy_damage
			self.attackerName = self.current_room.enemy.name
		self.update()

	def getDoorsMsg(self):
		msg = "There are doors to the "
		directions = []
		if self.m.rooms[self.x+1][self.y] != None:
			directions.append("east")
		if self.m.rooms[self.x][self.y-1] != None:
			directions.append("north")
		if self.m.rooms[self.x-1][self.y] != None:
			directions.append("west")
		if self.m.rooms[self.x][self.y+1] != None:
			directions.append("south")
		for i, dir in enumerate(directions):
			if (i != len(directions) and i != len(directions) -1):
				msg += dir
				if len(directions) != 2:
					msg += ","
				msg += " "
			elif i == len(directions) - 1 and len(directions) != 1:
				msg += "and " + dir
			else:
				msg += dir + "."
		msg += "\n"
		return msg

	def getOutput(self):
		#we build the message based on different things
		msg =""
		if (self.outputCode == 1 or self.outputCode == 0.5):
			if self.current_room != None:
				if self.current_room.explored:
					msg += "You have been here before...\n"
				else:
					msg += "You have never been in this room.\n"
					self.current_room.explored = True

			#tell user which directions they can move
			msg+= self.getDoorsMsg()

			if (self.current_room.enemyAlive):
				msg += "Ah! There's a " + self.current_room.enemy.name + " in here!\n"

			if (self.current_room.treasure):
				msg += "There's a treasure chest in here!\n"

		# elif self.outputCode == 0.5:
		# 	msg += self.getDoorsMsg()

		#smaller outputCodes
		elif self.outputCode == 0:
			msg += "Invalid input.\n"
		elif self.outputCode == 2:
			msg += "There is nothing to attack here!\n"
		elif self.outputCode == 3:
			msg += "You killed the " + self.current_room.enemy.name + "!\n"
		elif self.outputCode == 4:
			msg += "You did {} damage to the {}!\n".format(self.player_damage, self.current_room.enemy.name)
			msg += "The {} still alive with {} health!\n".format(self.current_room.enemy.name, self.current_room.enemy.health) #... implememt this
		elif self.outputCode == 5:
			msg += "You have {} health and {} gold coins.".format(self.player_health, self.gold_coins)
		elif self.outputCode == 6:
			foundSomething = False
			if (self.gained_health != 0):
				msg += "You found a potion that healed you for {} health.\n".format(self.gained_health)
				foundSomething = True
			if (self.gained_coins != 0):
				msg += "You found {} gold coins.\n".format(self.gained_coins)
				foundSomething = True
			if not foundSomething:
				msg += "The treasure chest was empty... :(\n"
		elif self.outputCode == 7:
			msg += "There is no treasure in here!\n"
		if (self.gotAttacked):
			msg += "You took {} damage from the {}\n".format(self.enemy_damage, self.attackerName)
		return msg
