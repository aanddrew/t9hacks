import map


m = map.Map(50)

for x in range(0,50):
	for y in range(0, 50):
		if (m.rooms[x][y] != None):
			print(m.rooms[x][y].message)