# native libs
import random
import time

# non-native libs
import pyglet

# local gui libs
import chars_gui
# local libs
import party


class PartyGui(object):
    def __init__(self):
        self.party = party.Party()
        self.chars_gui = []
        for char in self.party.chars:
            self.chars_gui.append(chars_gui.CharGui(char))
            
    def new_label_text(self, c):
        return str(c)+": "+str(c.stars)+" stars and "+str(c.coins)+" coins"

class Window(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(width=1000, height=500,
                                     *args, **kwargs)
        self.party_gui = PartyGui()
        # ------------------ IMAGES --------------------#
        self.board = pyglet.resource.image("boards/"+self.party_gui.party.board.img_path)
        self.player0 = pyglet.resource.image("static/p0.png")
        self.player1 = pyglet.resource.image("static/p1.png")
        # ------------------ LABELS --------------------#
        self.label0 = pyglet.text.Label('Hello, world', font_name='Arial',
                          font_size=18, x=30, y=0)
        self.label1 = pyglet.text.Label('Hello, world', font_name='Arial',
                          font_size=18, x=self.width//2, y=0)
        # ------------------ MOAR --------------------#
            
    
    def on_key_press(self, symbol, modifiers):
        if symbol == pyglet.window.key.R:
            self.party_gui.party.roll_event()
        if symbol in [pyglet.window.key.LEFT, pyglet.window.key.UP,
                      pyglet.window.key.RIGHT, pyglet.window.key.DOWN]:
            if symbol == pyglet.window.key.LEFT: cmd = "left"
            if symbol == pyglet.window.key.UP: cmd = "up"
            if symbol == pyglet.window.key.RIGHT: cmd = "right"
            if symbol == pyglet.window.key.DOWN: cmd = "down"
            self.party_gui.party.choice_event(cmd)
        if symbol in [pyglet.window.key.Y, pyglet.window.key.N]:
            if symbol == pyglet.window.key.Y: cmd = "y"
            if symbol == pyglet.window.key.N: cmd = "n"
            self.party_gui.party.star_choice_event(cmd)
        
    def on_draw(self):
        for c in self.party_gui.chars_gui:
            c.update_pos()
        self.label0.text = self.party_gui.new_label_text(self.party_gui.party.chars[0])
        self.label1.text = self.party_gui.new_label_text(self.party_gui.party.chars[1])
        
        self.clear()
        self.board.blit(0, 0) # y-values are upside-down! # or sth
        self.player0.blit(self.party_gui.chars_gui[0].x-15, self.party_gui.chars_gui[0].y-15)
        self.player1.blit(self.party_gui.chars_gui[1].x-15, self.party_gui.chars_gui[1].y-15)
        self.label0.draw()
        self.label1.draw()

def main():
    print("init window...")
    window = Window()
    print("done! init app...")
    pyglet.app.run()


if __name__=="__main__":
    main()
