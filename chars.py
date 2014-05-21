from random import randint

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
            print("")
            npt = ""
            while npt not in ["roll"]: #"show map" etc.
                npt = raw_input(str(self)+" start!\n> ")
            if npt == "roll":
                roll = randint(1,8)
                print(str(self)+" rolled a "+str(roll)+" (out of 8)")
                return roll
                    
    def get_choice(self, junction):
        if self.is_hmn:
            npt = ""
            while not junction.is_valid(npt): #"show map" etc.
                npt = raw_input("Choose way at junction "+
                                junction.get_pretty_coord()+":\n> ")
            return junction.get_next(npt)

    def get_star_choice(self):
        if self.is_hmn:
            npt = ""
            while not npt in ["y", "n"]:
                npt = raw_input("do you want this star? (y/n)\n> ")
            if npt == "y": return True
            if npt == "n": return False
