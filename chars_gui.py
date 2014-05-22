from random import randint

class CharGui(object):
    
    def __init__(self, char):
        self.char = char
        """here a second set of coordinates is needed
            to move the character /some/ pixels forward
            every frame instead of 'jumping' to the next
            field directly"""
        # call /after/ char has been placed on start
        self.y = char.is_on.y
        self.x = char.is_on.x
    
    def update_pos(self):
        self.y = self.char.is_on.y
        self.x = self.char.is_on.x
        
