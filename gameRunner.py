from TextGame import *

g = Game('player')

s = ''
while s != 'done':
	valid = False
	while not valid:
		s = raw_input ('what do you do?')
		valid = g.input(s)
	print(g.getGameMsg())