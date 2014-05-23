wimp
====

"WIMP is not Mario Party". Instead, it's a fun board game of strategy and luck.

dev
===

WIMP is written in Python2 (2 required by Pyglet), which should allow for easy
modification and addition of minigames, boards and modes.

Progress can (hopefully) be tracked in the "milestones" file. ATM, it's still
terminal-based. If the project has been abandoned for some time as you read
this, don't fret to at least take a look at the code. It will depend on a
minimum of libraries and as it is pure Python, it should be easy to get into.

PROGRESS IMAGE/VIDEO OF THE MONTH:

/May isn't over yet/


usage
=====

`git clone https://github.com/xjcl/wimp.git`

`python party_term.py` or `python party_gui.py`

blitz how-to-play guide
=======================

ATM you play two human players going around the board drawn
in 'boards/a.png'. the terminal-based program will spit out
coordinates in the form (y, x) to help you find out where
you are.

the one minigame that's there ATM is a token minigame. you
just enter the final score of each character.

'roll' to roll your die.

'left', 'up', 'right', 'down' to choose a path at a junction.

'y', 'n' to choose whether to purchase a star.

-------------------------

'party_gui.py' is now partially functional!

run it (pyglet is required) and roll with 'r';

choose junction with left/up/right/down
(the board is turned 90 degrees ATM though)

accept/decline a star with 'y'/'n'
