class Field(object):

    def __init__(self, ftype, next):
        self.ftype = ftype
        self.ftype = "blue"
        self.next = next
        self.chars_on = []
        
    def land(self, char):
        #addcoins(char, 3)
        print(str(char)+" got 3 coins")
        char.coins += 3
        self.chars_on.append(char)
        char.is_on = self
    
