import random

import party

class PartyTerm(object):
    def __init__(self):
        self.party = party.Party()
        for c in self.party.chars:
            self.land(c, self.party.board.init_field)
        self.new_star_field()
        
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
        #char.to_go = ???
        #to_field.chars_on.append(char)
    
    # TODO BUT: move_one_field() and move() still do not
    # allow for animations! calling move_one_field() from
    # a new move_animated() might work.
    def move_one_field(self, char, to_field=None):
        from_field = char.is_on
        #from_field.chars_on.remove(char)
        if not to_field:
            to_field = from_field.next
        char.is_on = to_field
        #to_field.chars_on.append(char)
        if to_field.ftype == "junction":
            print("choose way at junction")
            self.party.waiting_for = "choice"
        elif to_field.ftype == "star":
            if char.coins < 20:
                print("sorry, you can't get this star")
            else:
                print("you want this ~*~*STAR*~*~")
                self.party.waiting_for = "star choice"
        else:
            self.party.fields_to_move -= 1
    
    def advance_turn(self):
        self.party.whose_turn += 1
        self.party.waiting_for = "roll"
        if self.party.whose_turn == len(self.party.chars):
            self.party.whose_turn = 0
            self.party.turn_no += 1 # TODO check if game has finished
        print(str(self.party.chars[self.party.whose_turn])+" start!")
        
    def move(self, char, to_field=None):
        while self.party.fields_to_move > 0:
            self.move_one_field(char, to_field=to_field)
            to_field = None # only use to_field the first time
            if self.party.waiting_for != "nothing":
                break
        if self.party.fields_to_move == 0:
            self.land(char, char.is_on)
            self.advance_turn()
    
    def roll_event(self):
        if self.party.waiting_for == "roll":
            if self.party.whose_turn >= 0 and self.party.whose_turn <= 3: # assert 
                self.party.waiting_for = "nothing"
                lchar = self.party.chars[self.party.whose_turn]
                roll = random.randint(1,8)
                self.party.fields_to_move = roll
                print(str(lchar)+" rolled a "+str(roll)+" (out of 8)")
                self.move(lchar) # MIGHT hit a junction
    
    def choice_event(self, cmd):
        if self.party.waiting_for == "choice":
            self.party.waiting_for = "nothing"
            lchar = self.party.chars[self.party.whose_turn]
            junction = lchar.is_on
            if junction.is_valid(cmd): #"show map" etc. 
                print("so valid")
                self.move(lchar, to_field=junction.get_next(cmd))
        
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

    def pprint_standings(self):
        print("\n    standings:")
        for c in self.party.chars:
            print(str(c)+": "+str(c.stars)+" stars and "+str(c.coins)+" coins")
            
    def run(self):
        while True:
            npt = raw_input("> ")
            if npt == "r":
                self.roll_event()
            if npt in ["left", "up", "right", "down"]:
                self.choice_event(npt)
            if npt in ["y", "n"]:
                self.star_choice_event(npt)
            if npt == "s": # standings
                self.pprint_standings()
                print(self.party.turn_no)
                print(self.party.whose_turn)
                print(self.party.waiting_for)
                print(self.party.fields_to_move)

if __name__=="__main__":
    p = PartyTerm()
    p.run()
