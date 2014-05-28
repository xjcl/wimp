from random import randint

class Char(object):
    
    def __init__(self, name, is_hmn=True):
        self.stars = 0
        self.coins = 10
        self.name = str(name)
        self.is_on = None
        self.go_to = None
        self.is_hmn = bool(is_hmn)
    def __str__(self):
        return self.name


