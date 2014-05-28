"""BA DA DAM DAM DA DA DAM - DAM -- DAM
    DA DAM DAM DA DA DA DAM DAM DAMM- DAMM- DAM
    DA DA NUNU NU NU... DADADADADANUNUNUNUNU
    DUM DUM -- DUM DUM (repeat)
    it's the mp7 mg theme okay!?
    """
import test

class MgContainer(object):
    def __init__(self, chars):
        self.state = "rules" # "rules", "game", "score"
        self.game = test.Test(chars)
    
    def start_event(self):
        if self.state == "rules":
            self.state = "game"
        if self.state == "score":
            from sys import exit
            exit(1)
    
    def undir_event(self, cmd):
        lchar = self.game.mg_chars[0]
        if cmd in lchar.dirs:
            lchar.dirs.remove(cmd)
    
    def get_opposite(self, cmd):
        if cmd == "left" : return "right"
        if cmd == "right": return "left"
        if cmd == "up"   : return "down"
        if cmd == "down" : return "up"
        
    def dir_event(self, cmd):
        lchar = self.game.mg_chars[0]
        if len(lchar.dirs)==0:
            lchar.dirs = [cmd]
        if len(lchar.dirs)>=1:
            if cmd not in lchar.dirs:
                lchar.dirs.append(cmd)
    
    def update(self):
        if self.state == "game":
            lchar = self.game.mg_chars[0]
            strength = 0.2
            try:
                multi = 2**(1.0/len(lchar.dirs)) # take sqrt(2) if diagonal
                # side effect: left+up+right does the same thing as up,
                # but much slower!
            except ZeroDivisionError:
                pass
            for d in lchar.dirs:
                if "left"  == d : lchar.vx -= strength*multi
                if "right" == d : lchar.vx += strength*multi
                if "up"    == d : lchar.vy += strength*multi
                if "down"  == d : lchar.vy -= strength*multi
            for c in self.game.mg_chars:
                c.vx *= 0.95
                c.vy *= 0.95
                c.x += c.vx
                c.y += c.vy
            
            # check for collisions
            if ((self.game.mg_chars[0].x - self.game.mg_chars[1].x)**2 +
                (self.game.mg_chars[0].y - self.game.mg_chars[1].y)**2
                < 30**2):
                    self.game.mg_chars[0].score = 7
                    self.state = "score"
                
            
