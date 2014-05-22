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


    def new_star_field(self):
        if self.board.star_field:
            # revert old field
            self.board.star_field.ftype = "blue"
        self.board.star_field = random.choice(self.board.blue_fields)
        self.board.star_field.ftype = "star"
        print("star appeared at "+self.board.star_field.get_pretty_coord())

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
        
        to_field.chars_on.append(char)
        char.is_on = to_field
    
    
        
    def move_by(self, char, n):
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
        self.land(char, to_field)
    
    def advance_turn(self):
        for c in self.chars:
            roll = c.get_roll()
            self.move_by(c, roll)
        self.pprint_coin_totals()
            
    def pprint_coin_totals(self):
        print("\ncoin totals:")
        for c in self.chars:
            print(str(c)+": "+str(c.coins))
    
    def run(self):
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
    print("\n\n\n")    
    p = Party()
    p.run()

