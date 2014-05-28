import pyglet

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
    def __init__(self, chars, w):
        self.mg_chars = []
        self.w = w
        for i in range(len(chars)):
            lchar = MgChar(chars[i], i)
            self.mg_chars.append(lchar)
        self.state = "game" # communicate state back to container
        # ------------------ IMAGES --------------------#
        lbg = pyglet.resource.image("mg/test_bg.png")
        self.bg = pyglet.sprite.Sprite(lbg)
        lplayer0 = pyglet.resource.image("static/p0.png")
        lplayer1 = pyglet.resource.image("static/p1.png")
        self.player0 = pyglet.sprite.Sprite(lplayer0)
        self.player1 = pyglet.sprite.Sprite(lplayer1)
        # ------------------ END --------------------#
            
    def undir_event(self, cmd):
        lchar = self.mg_chars[0]
        if cmd in lchar.dirs:
            lchar.dirs.remove(cmd)
    
    def get_opposite(self, cmd):
        if cmd == "left" : return "right"
        if cmd == "right": return "left"
        if cmd == "up"   : return "down"
        if cmd == "down" : return "up"
        
    def dir_event(self, cmd):
        lchar = self.mg_chars[0]
        if len(lchar.dirs)==0:
            lchar.dirs = [cmd]
        if len(lchar.dirs)>=1:
            if cmd not in lchar.dirs:
                lchar.dirs.append(cmd)
    
    def update(self):
        if True:
            lchar = self.mg_chars[0]
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
            for c in self.mg_chars:
                c.vx *= 0.95
                c.vy *= 0.95
                c.x += c.vx
                c.y += c.vy
            
            # check for collisions
            if ((self.mg_chars[0].x - self.mg_chars[1].x)**2 +
                (self.mg_chars[0].y - self.mg_chars[1].y)**2
                < 30**2):
                    self.mg_chars[0].score = 7
                    self.state = "score"
                

    # ------------------ INPUTS --------------------#
    def on_key_release(self, symbol, modifiers):
        if symbol in [pyglet.window.key.LEFT, pyglet.window.key.UP,
                      pyglet.window.key.RIGHT, pyglet.window.key.DOWN]:
            if symbol == pyglet.window.key.LEFT : cmd = "left"
            if symbol == pyglet.window.key.UP   : cmd = "up"
            if symbol == pyglet.window.key.RIGHT: cmd = "right"
            if symbol == pyglet.window.key.DOWN : cmd = "down"
            self.undir_event(cmd)
    
    def on_key_press(self, symbol, modifiers):
        if symbol in [pyglet.window.key.LEFT, pyglet.window.key.UP,
                      pyglet.window.key.RIGHT, pyglet.window.key.DOWN]:
            if symbol == pyglet.window.key.LEFT : cmd = "left"
            if symbol == pyglet.window.key.UP   : cmd = "up"
            if symbol == pyglet.window.key.RIGHT: cmd = "right"
            if symbol == pyglet.window.key.DOWN : cmd = "down"
            self.dir_event(cmd)
            
        if symbol == pyglet.window.key.K:
            self.mg_container.start_event()
    
    def on_draw(self, *args, **kwargs):
        self.update()
        #
        self.w.width = 600
        self.w.height = 600
        self.bg.x, self.bg.y = 0, 0
        self.bg.draw()
        self.player0.x = self.mg_chars[0].x//1 -15
        self.player0.y = self.mg_chars[0].y//1 -15
        self.player1.x = self.mg_chars[1].x//1 -15
        self.player1.y = self.mg_chars[1].y//1 -15
        self.player0.draw()
        self.player1.draw()
        
