class Junction(object):

    def __init__(self, y, x, left_next=None, up_next=None,
                             right_next=None, down_next=None):
        self.y = y
        self.x = x # used for drawing lateron
        # also for loading -- query by x,y coord
        self.ftype = "junction"
        self.left_next = left_next
        self.up_next = up_next
        self.right_next = right_next
        self.down_next = down_next
        
        self.chars_on = []
        
    def is_valid(self, cmd):
        if cmd in ["left", "up", "right", "down"]:
            if cmd == "left"  and self.left_next:  return True
            if cmd == "up"    and self.up_next:    return True
            if cmd == "right" and self.right_next: return True
            if cmd == "down"  and self.down_next:  return True
                
    def get_next(self, cmd):
        if cmd == "left":  return self.left_next
        if cmd == "up":    return self.up_next
        if cmd == "right": return self.right_next
        if cmd == "down":  return self.down_next
    
    def get_pretty_coord(self):
        return str(self.y)+", "+str(self.x)


class Field(object):

    def __init__(self, y, x, ftype="blue", next=None):
        self.y = y
        self.x = x # used for drawing lateron
        # also for loading -- query by x,y coord
        self.ftype = ftype
        self.next = next
        # chars_on is needed in addition to char.is_on
        # to draw chars 0,1,2 when it is 3's turn
        self.chars_on = []
    
    def get_pretty_coord(self):
        return str(self.y)+", "+str(self.x)


        
