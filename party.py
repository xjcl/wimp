import random

import boards
import chars
import mg

class Party(object):
    
    def __init__(self):
        self.board = boards.a.BoardA()
        self.chars = [chars.Char("Chugga", True),
                      chars.Char("NCS"   , True)]
                      # it's not creepy k i only use
                      # the names to differentiate them.
        
        self.turn_no = 0
        self.whose_turn = 0 # 0-3: players; 7: minigame; ...
        self.waiting_for = "roll"
        self.fields_to_move = 0

