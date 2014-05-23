import random

import boards
import chars
import mg

class Party(object):
    
    def __init__(self):
        self.board = boards.a.BoardA()
        self.chars = [chars.Char("Chugga", True),
                      chars.Char("NCS"   , True)]
                      # it's not creepy k i only use
                      # the names to differentiate them.
        for c in self.chars:
            self.land(c, self.board.init_field)
        self.new_star_field()
        
        self.turn_no = 0
        self.whose_turn = 0 # 0-3: players; 7: minigame; ...
        self.waiting_for = "roll"
        self.fields_to_move = 0


    def new_star_field(self):
        if self.board.star_field:
            # revert old field
            self.board.star_field.ftype = "blue"
        self.board.star_field = random.choice(self.board.blue_fields)
        self.board.star_field.ftype = "star"
        print("star appeared at "+self.board.star_field.get_pretty_coord())


    def land(self, char, to_field):
        
        print(str(char)+" landed on "+to_field.get_pretty_coord()+
                " ("+to_field.ftype+")")
        
        if to_field.ftype == "blue":
            self.delta_coins(char, +3)
            
        if to_field.ftype == "red":
            self.delta_coins(char, -3)
        
        if to_field.ftype == "chance":
            print("CHANCE TIME!")
            from_char = self.chars[1]
            action = "transfer 20 coins"
            to_char = self.chars[0]
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
        to_field.chars_on.append(char)
    
    # TODO BUT: move_one_field() and move() still do not
    # allow for animations! calling move_one_field() from
    # a new move_animated() might work.
    def move_one_field(self, char, to_field=None):
        from_field = char.is_on
        from_field.chars_on.remove(char)
        if not to_field:
            to_field = from_field.next
        char.is_on = to_field
        to_field.chars_on.append(char)
        if to_field.ftype == "junction":
            print("choose way at junction")
            self.waiting_for = "choice"
        elif to_field.ftype == "star":
            if char.coins < 20:
                print("sorry, you can't get this star")
            else:
                print("you want this ~*~*STAR*~*~")
                self.waiting_for = "star choice"
        else:
            self.fields_to_move -= 1
    
    def advance_turn(self):
        self.whose_turn += 1
        self.waiting_for = "roll"
        if self.whose_turn == len(self.chars):
            self.whose_turn = 0
            self.turn_no += 1 # TODO check if game has finished
        print(str(self.chars[self.whose_turn])+" start!")
        
    def move(self, char, to_field=None):
        while self.fields_to_move > 0:
            self.move_one_field(char, to_field=to_field)
            to_field = None # only use to_field the first time
            if self.waiting_for != "nothing":
                break
        if self.fields_to_move == 0:
            self.land(char, char.is_on)
            self.advance_turn()
    
    def roll_event(self):
        if self.waiting_for == "roll":
            if self.whose_turn >= 0 and self.whose_turn <= 3: # assert 
                self.waiting_for = "nothing"
                lchar = self.chars[self.whose_turn]
                roll = random.randint(1,8)
                self.fields_to_move = roll
                print(str(lchar)+" rolled a "+str(roll)+" (out of 8)")
                self.move(lchar) # MIGHT hit a junction
    
    def choice_event(self, cmd):
        if self.waiting_for == "choice":
            self.waiting_for = "nothing"
            lchar = self.chars[self.whose_turn]
            junction = lchar.is_on
            if junction.is_valid(cmd): #"show map" etc. 
                print("so valid")
                self.move(lchar, to_field=junction.get_next(cmd))
        
    def star_choice_event(self, cmd):
        if self.waiting_for == "star choice":
            lchar = self.chars[self.whose_turn]
            self.waiting_for = "nothing"
            if cmd == "y":
                print("congrats you got a star")
                lchar.coins -= 20
                lchar.stars += 1
                self.new_star_field()
            elif cmd == "n":
                print("okay then you're weird lol")
            self.move(lchar)
    
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
    
    def land_depr(self, char, to_field):
        
        print(str(char)+" landed on "+to_field.get_pretty_coord()+
                " ("+to_field.ftype+")")
        
        if to_field.ftype == "blue":
            self.delta_coins(char, +3)
            
        if to_field.ftype == "red":
            self.delta_coins(char, -3)
        
        if to_field.ftype == "chance":
            print("CHANCE TIME!")
            from_char = self.chars[1]
            action = "transfer 20 coins"
            to_char = self.chars[0]
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
        
        to_field.chars_on.append(char)
        char.is_on = to_field
    
    
        
    def move_by_depr(self, char, n):
        from_field = char.is_on
        from_field.chars_on.remove(char)
        while n > 0:
            to_field = from_field.next
            if to_field.ftype == "junction":
                to_field = char.get_choice(to_field)
            if to_field.ftype == "star":
                if char.coins < 20:
                    print("sorry, you can't get this star")
                else:
                    if char.get_star_choice():
                        print("congrats you got a star")
                        self.new_star_field()
                    else:
                        print("okay then you're weird lol")
                to_field = to_field.next
            n -= 1
            from_field = to_field
        self.land_depr(char, to_field)
    
    def advance_turn_depr(self):
        for c in self.chars:
            roll = c.get_roll()
            self.move_by_depr(c, roll)
        self.pprint_coin_totals()
            
    
    def run_depr(self):
        for i in range(10):
            self.turn = i
            p.advance_turn()
            game = mg.test.Test()
            for c in mg.mg_container.play(self.chars, game):
                print(str(c)+" won! +10 coins.")
                c.coins += 10
            self.pprint_coin_totals()
            #self.save() # save current standings to file
            # also positions, happening spaces, minigame money etc.


if __name__=="__main__":
    pass # RIP bad programming



