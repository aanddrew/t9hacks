import sender
from localGame.TextGame import Game
import readEmail

#put recipients email here.
email = "andrewweller.oc@gmail.com"
sendbot = sender.Sender('sendgame10@gmail.com', email)

test = readEmail.readEmailMaster()
test.Authentication()
# print(test.actuallyRead())
g = Game()

output = g.getOutput()
sendbot.send('Sendgame Output', output)

lastId = 0
first = True
while not g.done():
	read = test.actuallyRead()
	read = read.strip()

	formatted = read.decode('utf-8')

	if (test.getLastId() != lastId):
		if (not first):
			print("new email")
			print(test.lastAddress)
			g.input(formatted)
			output = g.getOutput()
			if (output != "Invalid input.\n"):
				sendbot.send('Sendgame Output', output)
			lastId = test.getLastId()
		else:
			lastId = test.getLastId()
			first = False