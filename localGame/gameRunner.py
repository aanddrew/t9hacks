from TextGame import *

g = Game()

s = ''
print(g.getOutput())
while not g.done():
	print("choices: move (east, west, north, south), attack, treasure, stats")
	s = raw_input ('what do you do?\n')
	g.input(s)
	print(g.getOutput())

print("Nice run!")
print("You acquired {} gold coins and killed {} enemies!".format(g.gold_coins, g.kill_count))