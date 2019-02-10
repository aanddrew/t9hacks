from . import room
import random

class Map:

	def __init__(self, size):
		self.size = size
		self.rooms = []
		for y in range(0, size):
			self.rooms.append([])
			for x in range(0, size):
				if random.randint(0,3) == 1:
					self.rooms[y].append(None)
				else:
					self.rooms[y].append(room.Room())