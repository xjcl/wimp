"""BA DA DAM DAM DA DA DAM - DAM -- DAM
    DA DAM DAM DA DA DA DAM DAM DAMM- DAMM- DAM
    DA DA NUNU NU NU... DADADADADANUNUNUNUNU
    DUM DUM -- DUM DUM (repeat)
    it's the mp7 mg theme okay!?
    """
# non-native libs
import pyglet

# local libs
import test

class MgContainer(object):
    def __init__(self, chars, w):
        self.state = "rules" # "rules", "game", "score"
        self.game = test.Test(chars, w)
    
    def start_event(self):
        if self.state == "rules":
            self.state = "game"
        if self.state == "score":
            from sys import exit
            exit(1)
    

class MgContainerView(object):
    def __init__(self, chars, w):
        self.mg_container = MgContainer(chars, w)
        self.w = w
        # ------------------ LABELS --------------------#
        self.label_xxx = pyglet.text.Label('Hello, world', font_name='Arial',
                          font_size=36, x=self.w.width//2, y=self.w.height//2,
                          color=(255,255,0,255),
                          anchor_x="center", anchor_y="center")
        # ------------------ MOAR --------------------#
        
    # ------------------ INPUTS --------------------#
    def on_key_release(self, symbol, modifiers):
        self.mg_container.game.on_key_release(symbol, modifiers)
    
    def on_key_press(self, symbol, modifiers):
        if symbol == pyglet.window.key.K:
            self.mg_container.start_event()
        else:
            self.mg_container.game.on_key_press(symbol, modifiers)
    
    def on_draw(self, *args, **kwargs):
        if self.mg_container.state == "rules":
            self.label_xxx.font_size = 36
            self.label_xxx.text = \
                "here are the rules press k"
            self.label_xxx.draw()
        
        if self.mg_container.state == "game":
            if self.mg_container.game.state == "game":
                self.mg_container.game.on_draw(*args, **kwargs)
            else:
                self.mg_container.state = "score"
            
        if self.mg_container.state == "score":
            self.label_xxx.text = \
                "is over"
            self.label_xxx.font_size = 18
            self.label_xxx.draw()
            
            
