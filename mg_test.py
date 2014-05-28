# native libs
#import random
#import time

# non-native libs
import pyglet

# local libs
import mg.mg_container
import chars

class Window(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(width=1000, height=500,
                                     *args, **kwargs)
        self.chars = [chars.Char("Chugga", True),
                      chars.Char("NCS"   , True)]
        self.mg_container = mg.mg_container.MgContainer(self.chars)
        # ------------------ CLOCK --------------------#
        pyglet.clock.schedule_interval(self.on_draw, 1.0/30.0)
        pyglet.clock.set_fps_limit(30)
        # ------------------ IMAGES --------------------#
        lbg = pyglet.resource.image("mg/test_bg.png")
        self.bg = pyglet.sprite.Sprite(lbg)
        lplayer0 = pyglet.resource.image("static/p0.png")
        lplayer1 = pyglet.resource.image("static/p1.png")
        self.player0 = pyglet.sprite.Sprite(lplayer0)
        self.player1 = pyglet.sprite.Sprite(lplayer1)
        # ------------------ LABELS --------------------#
        self.label_xxx = pyglet.text.Label('Hello, world', font_name='Arial',
                          font_size=36, x=self.width//2, y=self.height//2,
                          color=(255,255,0,255),
                          anchor_x="center", anchor_y="center")
        # ------------------ MOAR --------------------#
    def on_key_release(self, symbol, modifiers):
        if symbol in [pyglet.window.key.LEFT, pyglet.window.key.UP,
                      pyglet.window.key.RIGHT, pyglet.window.key.DOWN]:
            if symbol == pyglet.window.key.LEFT : cmd = "left"
            if symbol == pyglet.window.key.UP   : cmd = "up"
            if symbol == pyglet.window.key.RIGHT: cmd = "right"
            if symbol == pyglet.window.key.DOWN : cmd = "down"
            self.mg_container.undir_event(cmd)
    
    def on_key_press(self, symbol, modifiers):
        if symbol in [pyglet.window.key.LEFT, pyglet.window.key.UP,
                      pyglet.window.key.RIGHT, pyglet.window.key.DOWN]:
            if symbol == pyglet.window.key.LEFT : cmd = "left"
            if symbol == pyglet.window.key.UP   : cmd = "up"
            if symbol == pyglet.window.key.RIGHT: cmd = "right"
            if symbol == pyglet.window.key.DOWN : cmd = "down"
            self.mg_container.dir_event(cmd)
            
        if symbol == pyglet.window.key.K:
            self.mg_container.start_event()
        
        
    def on_draw(self, *args, **kwargs):
        # ------------ UPDATE MODEL -------------
        self.mg_container.update()
        # ------------ UPDATE VIEW -------------
        
        self.clear()
        
        if self.mg_container.state == "rules":
            self.label_xxx.font_size = 36
            self.label_xxx.text = \
                "here are the rules press k"
            self.label_xxx.draw()
            
        if self.mg_container.state == "game":
            self.width = 600
            self.height = 600
            self.bg.x, self.bg.y = 0, 0
            self.bg.draw()
            self.player0.x = self.mg_container.game.mg_chars[0].x//1 -15
            self.player0.y = self.mg_container.game.mg_chars[0].y//1 -15
            self.player1.x = self.mg_container.game.mg_chars[1].x//1 -15
            self.player1.y = self.mg_container.game.mg_chars[1].y//1 -15
            self.player0.draw()
            self.player1.draw()
            
        if self.mg_container.state == "score":
            self.label_xxx.text = \
                "is over"
            self.label_xxx.font_size = 18
            self.label_xxx.draw()
        

def main():
    print("init window...")
    window = Window()
    print("done! init app...")
    pyglet.app.run()


if __name__=="__main__":
    main()
