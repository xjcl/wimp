
class MgChar(object):
    def __init__(self, char, n):
        self.char = char
        self.n = n # number: 0-3
        self.x = 100.0
        self.y = 100.0
        self.vx = 0.0
        self.vy = 0.0
        self.dirs = [] # 2 out of ["left", "up", "right", "down"]
        if n%2 == 1:
            self.x = 500.0
        if n//2 == 1:
            self.y = 500.0
        
        self.score = 0

class Test(object):
    def __init__(self, chars):
        self.mg_chars = []
        for i in range(len(chars)):
            lchar = MgChar(chars[i], i)
            self.mg_chars.append(lchar)
            

