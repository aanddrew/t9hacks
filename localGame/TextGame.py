import map

class Game:

	def __init__(self):
		self.x = 25
		self.y = 25

		self.m = map.Map(50)

		self.player_health = 100
		self.gold_coins = 0

		self.outputCode = 1
		#self.outputCode is a determining factor in what the output message is:
		"""
			Here are the codes:
			0 - invalid input
			1 - move command, player is now in new room
			2 - player attacked, but there was no enemy
			3 - player attacked, killed enemy
			4 - player attacked, enemy still alive
			5 - show stats
		"""
		self.current_room = self.m.rooms[self.x][self.y]
		while (self.current_room == None):
			self.x += 1
			self.current_room = self.m.rooms[self.x][self.y]
		self.current_room.enemyAlive = False
		self.current_room.enemy = None

	def update(self):
		# print("updating")
		self.current_room = self.m.rooms[self.x][self.y]

	def input(self, input):
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
		if commands[0] == "move":
			if len(commands) == 1:
				self.outputCode = 0
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
		elif commands[0] == "attack":
			if (self.current_room.enemyAlive):
				self.outputCode = 3
				self.current_room.enemyAlive = False;
			else:
				self.outputCode = 2
		elif commands[0] == "stats":
			self.outputCode = 5
		else:
			self.outputCode = False
		self.update()


	def getOutput(self):
		#we build the message based on different things
		msg =""
		if (self.outputCode == 1):
			if self.current_room != None:
				if self.current_room.explored:
					msg += "You have been here before...\n"
				else:
					msg += "You have never been in this room.\n"
					self.current_room.explored = True

			#tell user which directions they can move
			msg += "There are doors to the "
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

			if (self.current_room.enemyAlive):
				msg += "Ah! There's a " + self.current_room.enemy.name + " in here!\n"

		#smaller outputCodes
		elif self.outputCode == 0:
			msg += "Invalid input."
		elif self.outputCode == 2:
			msg += "There is nothing to attack here!"
		elif self.outputCode == 3:
			msg += "You killed the " + self.current_room.enemy.name + "!"
		elif self.outputCode == 4:
			msg += "He's still alive" #... implememt this
		elif self.outputCode == 5:
			msg += "You have {} health and {} gold coins.".format(self.player_health, self.gold_coins)

		#this is temporary, tells which location in the map the player is at
		# msg += "You are now at {}, {}\n".format(self.x, self.y)
		# if self.m.rooms[self.x][self.y] != None:
		# 	msg += str(self.m.rooms[self.x][self.y].enemyAlive) + "\n"
		return msg
