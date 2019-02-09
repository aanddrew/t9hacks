from TextGame import *

g = Game()

s = ''
print(g.getOutput())
while s != 'done':
	while True:
		print("choices: move (east, west, north, south), attack, treasure, stats")
		s = raw_input ('what do you do?\n')
		g.input(s)
		print(g.getOutput())