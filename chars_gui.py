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
        # to move per animation frame
        self.dy = 0
        self.dx = 0
    
    def update_pos(self):
        self.y = self.char.is_on.y
        self.x = self.char.is_on.x
    
    def update(self):
        # DOESN'T WORK
        if self.y != self.char.is_on.y or self.x != self.char.is_on.x:
            if self.dy != 0 or self.dx != 0:
                self.y += self.dy
                self.x += self.dx
            else:
                self.dy = 0.1*(self.char.is_on.y-self.y)
                self.dx = 0.1*(self.char.is_on.y-self.x)
        else:
            self.dy = 0
            self.dx = 0
            
