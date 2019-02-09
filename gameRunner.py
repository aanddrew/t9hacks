from TextGame import *

g = Game()

s = ''
print(g.getOutput())
while s != 'done':
	while True:
		s = raw_input ('what do you do?\n')
		g.input(s)
		print(g.getOutput())