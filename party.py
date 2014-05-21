import boards.a as ba
import random

class Party(object):
    
    class Char(object):
    
        def __init__(self, party, name, is_hmn=True):
            self.party = party
            self.stars = 0
            self.coins = 10
            self.name = str(name)
            self.is_on = None
            self.is_hmn = bool(is_hmn)
        def __str__(self):
            return self.name
            
        def get_roll(self):
            if self.is_hmn: # should I instead make a child class for CPUs?
                npt = ""
                while npt not in ["roll"]: #"show map" etc.
                    npt = raw_input("\n"+str(self)+" Start!\n> ")
                if npt == "roll":
                    roll = random.randint(1,8)
                    print(str(self)+" rolled a "+str(roll)+" (out of 8)")
                    return roll
                    
        def get_choice(self, junction):
            if self.is_hmn:
                npt = ""
                while not junction.is_valid(npt): #"show map" etc.
                    npt = raw_input("Choose way at junction "+
                                    junction.get_pretty_coord()+": \n> ")
                return junction.get_next(npt)
            



        
    def __init__(self):
        self.board = ba.BoardA()
        self.chars = [self.Char(self, "p0", True), self.Char(self, "p1", True)]
        for c in self.chars:
            self.land(c, self.board.init_field)



    def land(self, char, to_field):
        
        print(str(char)+" landed on "+to_field.get_pretty_coord()+
                " ("+to_field.ftype+")")
        
        if to_field.ftype == "blue":
            char.coins += 3
            #addcoins(char, 3) # animation! one by one!
            print(str(char)+" got 3 coins")
            print("Total: "+str(char.coins))
            
        if to_field.ftype == "red":
            lc = char.coins
            if char.coins < 3:
                char.coins = 0
            else:
                lc = 3    
                char.coins -= 3
            print(str(char)+" lost 3 coins")
            print("Total: "+str(char.coins))
        
        if to_field.ftype == "chance":
            print("CHANCE TIME!")
            from_char = self.chars[1]
            action = "transfer 20 coins"
            to_char = self.chars[0]
            if action.startswith("transfer"):
                if "20 coins" in action:
                    lc = from_char.coins
                    if from_char.coins < 20:
                        to_char.coins += from_char.coins
                        from_char.coins = 0
                    else:
                        lc = 20
                        to_char.coins += 20
                        from_char.coins -= 20
                    print(str(from_char)+" gave "+str(lc)+
                            " coins to "+str(to_char))
                        
            
        to_field.chars_on.append(char)
        char.is_on = to_field
    
    
        
    def move_by(self, char, n):
        from_field = char.is_on
        from_field.chars_on.remove(char)
        while n > 0:
            to_field = from_field.next
            if to_field.ftype == "junction":
                to_field = char.get_choice(to_field)
            n -= 1
            from_field = to_field
        self.land(char, to_field)
    
    def advance_turn(self):
        for c in self.chars:
            roll = c.get_roll()
            self.move_by(c, roll)
        print("\ncoin totals:")
        for c in self.chars:
            print(str(c)+": "+str(c.coins))
    
    def run(self):
        for i in range(3):
            self.turn = i
            p.advance_turn()
            #self.save() # save current standings to file
            # also positions, happening spaces, minigame money etc.


    
p = Party()
p.run()

