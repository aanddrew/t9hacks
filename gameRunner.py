from TextGame import *

g = Game('player')

s = ''
print(g.getOutput())
while s != 'done':
	valid = False
	while not valid:
		s = raw_input ('what do you do?')
		valid = g.input(s)
		g.update()
	print(g.getOutput())