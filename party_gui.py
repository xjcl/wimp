# native libs
import random

# non-native libs
import pyglet

# local gui libs
import chars_gui
# local libs
import party
import boards
import chars
import mg

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500

class Window(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(width=SCREEN_WIDTH, height=SCREEN_HEIGHT,
                                     *args, **kwargs)
        # ------------------ DATA --------------------#
        self.party = party.Party()
        self.chars_gui = []
        for char in self.party.chars:
            self.chars_gui.append(chars_gui.CharGui(char))
        self.state = "roll" # "roll", "choice", "star_choice"
        self.whose_turn = self.chars_gui[0]
        # ------------------ IMAGES --------------------#
        self.board = pyglet.resource.image("boards/"+self.party.board.img_path)
        # i've got a tiny ass-screen so i'll with x and y for now! TODO
        self.board = self.board.get_transform(rotate=270) 
        self.label1 = pyglet.text.Label('Hello, world', font_name='Arial',
                          font_size=36, x=self.width//2, y=self.height//2,
                          anchor_x='center', anchor_y='center')
        self.player0 = pyglet.resource.image("p0.png")
        self.player1 = pyglet.resource.image("p1.png")
        # ------------------ MOAR --------------------#
    
    def on_key_press(self, symbol, modifiers):
        print("..")
        if symbol == pyglet.window.key.LEFT:
            print("check it out")
        print("wat")
        if self.state == "roll" and symbol == pyglet.window.key.R:
            # roll
            roll = random.randint(1,8)
            print(str(self.whose_turn.char)+" rolled a "+str(roll)+" (out of 8)")
            self.party.move_by(self.whose_turn.char, roll)
            self.whose_turn.update_pos()
            # change whose turn it is
            #self.state = ""
            i = self.chars_gui.index(self.whose_turn)
            if i+1 == len(self.chars_gui):
                i = 0
            else:
                i += 1
            self.whose_turn = self.chars_gui[i]
        
    def on_draw(self):
        self.clear()
        self.board.blit(SCREEN_WIDTH, 0) # y-values are upside-down!
        self.player0.blit(self.chars_gui[0].y-15, self.chars_gui[0].x-15)
        self.player1.blit(self.chars_gui[1].y-15, self.chars_gui[1].x-15)
        self.label1.draw()

def main():
    print(-3)
    window = Window()
    print(-2)
    #pyglet.resource.image('denmark.png').blit(0,0)
    pyglet.app.run()


if __name__=="__main__":
    main()
