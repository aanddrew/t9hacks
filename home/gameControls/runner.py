import sender
from localGame.TextGame import Game
import readEmail

#put recipients email here.
email = "test@example.com"
sendbot = sender.Sender('sendgame10@gmail.com', email)

test = readEmail.readEmailMaster()
test.Authentication()
# print(test.actuallyRead())
g = Game()

while not g.done():
	formatted = ""
	read = test.actuallyRead()
	read = read.strip()
	formatted = read.decode('utf-8')

	print(formatted)
	# g.input(command)
	# output = g.getOutput()
	# sendbot.send('Sendgame Output', output)