# sendgame
t9 hacks project, an email based text rpg.

How to use this game:

add these files to your directory.
import TextGame in your client file

create an instance of game with:
  game = TextGame.Game('player name')

You should display game.getOutput() before you enter the game's loop then:

/loop begins
  you must call game.input("your input here")
  before then displaying the output with game.getOutput()
/loop ends

where "your input here" is the command the player gives

/end tutorial

and just loop between these to play the game
