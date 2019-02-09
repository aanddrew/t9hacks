import map

class Game:

	def __init__(self, playerName):
		self.name = playerName

		self.x = 25
		self.y = 25

		self.m = map.Map(50)
		self.current_room = self.m.rooms[self.x][self.y]

		# for x in self.m.rooms:
		# 	for y in x:
		# 		if y != None:
		# 			y.explored = True
		# 			print(y.explored)

	def update(self):
		print("updating")
		self.current_room = self.m.rooms[self.x][self.y]
		if self.current_room.explored == False:
			# print("room not explored")
			self.current_room.explored = True

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
		
		self.update()


	def getGameMsg(self):
		msg =""
		if self.current_room != None:
			if self.current_room.explored:
				msg += "You have been here before...\n"
			else:
				msg += "You have never been in this room.\n"

		msg += "You are now at {}, {}\n".format(self.x, self.y)
		if self.m.rooms[self.x][self.y] != None:
			msg += str(self.m.rooms[self.x][self.y].enemyAlive) + "\n"
		return msg
