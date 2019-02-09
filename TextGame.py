import map

class Game:

	def __init__(self, playerName):
		self.name = playerName

		self.x = 25
		self.y = 25

		self.m = map.Map(50)
		self.current_room = self.m.rooms[self.x][self.y]
		while (self.current_room == None):
			self.x += 1
			self.current_room = self.m.rooms[self.x][self.y]

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
		commands.append(temp)

		#select action given the commands user gave
		if commands[0] == "move":
			if len(commands) == 1:
				return False
			elif commands[1] == "north" and self.m.rooms[self.x][self.y-1] != None:
				self.y -= 1
				return True
			elif commands[1] == "south" and self.m.rooms[self.x][self.y+1] != None:
				self.y += 1
				return True
			elif commands[1] == "west" and self.m.rooms[self.x-1][self.y] != None:
				self.x -= 1
				return True
			elif commands[1] == "east" and self.m.rooms[self.x+1][self.y] != None:
				self.x += 1
				return True
			else: 
				return False
		else:
			return False


	def getOutput(self):
		#we build the message based on different things
		msg =""
		#this does not work for some reason....
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

		#this is temporary, tells which location in the map the player is at
		# msg += "You are now at {}, {}\n".format(self.x, self.y)
		# if self.m.rooms[self.x][self.y] != None:
		# 	msg += str(self.m.rooms[self.x][self.y].enemyAlive) + "\n"
		return msg
