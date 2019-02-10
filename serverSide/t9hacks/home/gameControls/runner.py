import sender
from localGame.TextGame import Game

#put recipients email here.
email = "test@example.com"
sendbot = sender.Sender('sendgame10@gmail.com', email)

g = Game()

while not g.done():
	command = input('Enter your command\n')
	g.input(command)
	output = g.getOutput()
	sendbot.send('Sendgame Output', output)