wimp
====

"WIMP is not Mario Party". Instead, it's a fun board game of strategy and luck.

##dev

WIMP is written in Python2 (2 required by Pyglet), which should allow for easy
modification and addition of minigames, boards and modes.

Progress can be tracked in the "milestones" file. If the project has been
abandoned for some time as you read this, don't fret to at least take a look
at the code. It will depend on a minimum of libraries and as it is pure Python,
it should be easy to get into.

PROGRESS IMAGE/VIDEO OF THE MONTH:

/May isn't over yet/

##usage

`git clone https://github.com/xjcl/wimp.git`

Run with `python party_term.py` or `python party_gui.py`

###blitz how-to-play guide

terminal-version('party_term.py'): usually more stable, less user-friendly;
might not make sense if you haven't looked at static/a.png or the gui version yet.

* 'r' to roll your 8-sided die.
* 'left', 'up', 'right', 'down' to choose a path at a junction.
* 'y', 'n' to choose whether to purchase a star.

-------------------------

gui-version: use this k. if the current one is broken,
look out for the last v0.x release.

* run 'party_gui.py' (pyglet is required) and roll with 'r';
* choose junction with left/up/right/down;
* accept/decline a star with 'y'/'n'.
* press 'k' on the message "you don't have enough coins for this star"

prompts aren't always clearly marked. it is your turn when
nothing is moving, so try all of the above commands.

##Other

'milestones', 'idee' and 'workload' are meta-files;
used for note-taking, progress-tracking etc.

LICENSE IS GPL SO COPY AWAY!
