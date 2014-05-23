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
    def __init__(self, window):
        self.party = party.Party()
        self.window = window
        self.chars_gui = []
        for char in self.party.chars:
            self.land(char, self.party.board.init_field)
            self.chars_gui.append(chars_gui.CharGui(char))
            char.go_to = char.is_on
        self.new_star_field()
        
        self.animation_phase = "nothing"
        
            
    def new_label_text(self, c):
        return str(c)+": "+str(c.stars)+" stars and "+str(c.coins)+" coins"



    
    # TODO BUT: move_one_field() and move() still do not
    # allow for animations! calling move_one_field() from
    # a new move_animated() might work.

    def new_star_field(self):
        if self.party.board.star_field:
            # revert old field
            self.party.board.star_field.ftype = "blue"
        self.party.board.star_field = random.choice(self.party.board.blue_fields)
        self.party.board.star_field.ftype = "star"
        print("star appeared at "+self.party.board.star_field.get_pretty_coord())


    def land(self, char, to_field):
        
        print(str(char)+" landed on "+to_field.get_pretty_coord()+
                " ("+to_field.ftype+")")
        
        if to_field.ftype == "blue":
            self.delta_coins(char, +3)
            
        if to_field.ftype == "red":
            self.delta_coins(char, -3)
        
        if to_field.ftype == "chance":
            print("CHANCE TIME!")
            from_char = self.party.chars[1]
            action = "transfer 20 coins"
            to_char = self.party.chars[0]
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
        
        char.is_on = to_field
    
        
    def advance_turn(self):
        self.party.whose_turn += 1
        self.party.waiting_for = "roll"
        if self.party.whose_turn == len(self.party.chars):
            self.party.whose_turn = 0
            self.party.turn_no += 1 # TODO check if game has finished
        print(str(self.party.chars[self.party.whose_turn])+" start!")
    
    def roll_event(self):
        if self.party.waiting_for == "roll":
            if self.party.whose_turn >= 0 and self.party.whose_turn <= 3: # assert 
                self.party.waiting_for = "nothing"
                lchar = self.party.chars[self.party.whose_turn]
                roll = random.randint(1,8)
                self.party.fields_to_move = roll
                print(str(lchar)+" rolled a "+str(roll)+" (out of 8)")
    
    def choice_event(self, cmd):
        if self.party.waiting_for == "choice":
            self.party.waiting_for = "nothing"
            lchar = self.party.chars[self.party.whose_turn]
            junction = lchar.is_on
            if junction.is_valid(cmd): #"show map" etc. 
                print("so valid")
                lchar.go_to = junction.get_next(cmd)
        
    def star_choice_event(self, cmd):
        if self.party.waiting_for == "star choice":
            lchar = self.party.chars[self.party.whose_turn]
            self.party.waiting_for = "nothing"
            if cmd == "y":
                print("congrats you got a star")
                lchar.coins -= 20
                lchar.stars += 1
                self.new_star_field()
            elif cmd == "n":
                print("okay then you're weird lol")

# -----------------------------------------------------------------

    def delta_coins(self, char, n): # add or take stars/coins
        if n >= 0:
            lc = n
            char.coins += n
            #addcoins(char, 3) # animation! one by one!
            print(str(char)+" got "+str(n)+" coins")
        else:
            lc = char.coins
            if char.coins < n:
                char.coins = 0
            else:
                lc = n
                char.coins -= n
            print(str(char)+" lost "+str(lc)+" coins")
        print("total: "+str(char.coins))
        return lc # lc = actually moved coins
    
# -----------------------------------------------------------------    
    
    def init_animation(self, lchar, from_field, to_field):
        if from_field == to_field: # sort out junctions
            lchar.char.go_to = lchar.char.is_on.next
            to_field = from_field.next
        lchar.dy = (to_field.y-from_field.y)//10
        lchar.dx = (to_field.x-from_field.x)//10
        self.animation_phase = "moving"
    
    def update(self):
        if self.party.waiting_for == "nothing":
            lchar = self.chars_gui[self.party.whose_turn]
            from_field = lchar.char.is_on
            to_field = lchar.char.go_to
            
            if self.animation_phase == "nothing":
                if self.party.fields_to_move > 0:
                    if from_field.ftype == "junction" and from_field == to_field:
                        print("choose way at junction")
                        self.party.waiting_for = "choice"
                    elif from_field.ftype == "star":
                        if lchar.char.coins < 20:
                            print("sorry, you can't get this star")
                            self.init_animation(lchar, from_field, to_field)
                        else:
                            print("you want this ~*~*STAR*~*~")
                            self.party.waiting_for = "star choice"
                    else:
                        self.init_animation(lchar, from_field, to_field)
                if self.party.fields_to_move == 0:
                    print("field lights up "+to_field.get_pretty_coord())
                    self.land(lchar.char, lchar.char.go_to)
                    self.advance_turn()

            if self.animation_phase == "moving":
                lchar.y += lchar.dy
                lchar.x += lchar.dx
                if lchar.x == to_field.x and lchar.y == to_field.y:
                    lchar.dy = 0
                    lchar.dx = 0
                    self.animation_phase = "nothing"
                    if (lchar.char.go_to.ftype != "star" and
                       lchar.char.go_to.ftype != "junction"):
                        self.party.fields_to_move -= 1
                    lchar.char.is_on = lchar.char.go_to
                
    
# -----------------------------------------------------------------    



class Window(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(width=1000, height=500,
                                     *args, **kwargs)
        self.party_gui = PartyGui(self)
        # ------------------ CLOCK --------------------#
        pyglet.clock.schedule_interval(self.on_draw, 1.0/30.0)
        pyglet.clock.set_fps_limit(30)
        # ------------------ IMAGES --------------------#
        self.board   = pyglet.resource.image("boards/"+self.party_gui.party.board.img_path)
        self.player0 = pyglet.resource.image("static/p0.png")
        self.player1 = pyglet.resource.image("static/p1.png")
        self.star    = pyglet.resource.image("static/star.png")
        # ------------------ LABELS --------------------#
        self.label0 = pyglet.text.Label('Hello, world', font_name='Arial',
                          font_size=18, x=30, y=0)
        self.label1 = pyglet.text.Label('Hello, world', font_name='Arial',
                          font_size=18, x=self.width//2, y=0)
        # ------------------ MOAR --------------------#
    
    def on_key_press(self, symbol, modifiers):
        if symbol == pyglet.window.key.R:
            self.party_gui.roll_event()
        if symbol in [pyglet.window.key.LEFT, pyglet.window.key.UP,
                      pyglet.window.key.RIGHT, pyglet.window.key.DOWN]:
            if symbol == pyglet.window.key.LEFT: cmd = "left"
            if symbol == pyglet.window.key.UP: cmd = "up"
            if symbol == pyglet.window.key.RIGHT: cmd = "right"
            if symbol == pyglet.window.key.DOWN: cmd = "down"
            self.party_gui.choice_event(cmd)
        if symbol in [pyglet.window.key.Y, pyglet.window.key.N]:
            if symbol == pyglet.window.key.Y: cmd = "y"
            if symbol == pyglet.window.key.N: cmd = "n"
            self.party_gui.star_choice_event(cmd)
        
    def on_draw(self, *args, **kwargs):
        # ------------ UPDATE MODEL -------------
        self.party_gui.update()
        
        # ------------ UPDATE VIEW -------------
        self.clear()
        self.board.blit(0, 0) # y-values are upside-down! # or sth
        self.label0.text = self.party_gui.new_label_text(self.party_gui.party.chars[0])
        self.label1.text = self.party_gui.new_label_text(self.party_gui.party.chars[1])
        self.label0.draw()
        self.label1.draw()
        self.star.blit(self.party_gui.party.board.star_field.x-45,
                       self.party_gui.party.board.star_field.y-45)
        self.player0.blit(self.party_gui.chars_gui[0].x-15, self.party_gui.chars_gui[0].y-15)
        self.player1.blit(self.party_gui.chars_gui[1].x-15, self.party_gui.chars_gui[1].y-15)
        

def main():
    print("init window...")
    window = Window()
    print("done! init app...")
    pyglet.app.run()


if __name__=="__main__":
    main()
