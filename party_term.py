import party

class PartyTerm(object):
    def __init__(self):
        self.party = party.Party()
        
    def pprint_standings(self):
        print("\n    standings:")
        for c in self.party.chars:
            print(str(c)+": "+str(c.stars)+" stars and "+str(c.coins)+" coins")
            
    def run(self):
        while True:
            npt = raw_input("> ")
            if npt == "r":
                self.party.roll_event()
            if npt in ["left", "up", "right", "down"]:
                self.party.choice_event(npt)
            if npt in ["y", "n"]:
                self.party.star_choice_event(npt)
            if npt == "s": # standings
                self.pprint_standings()
                print(self.party.turn_no)
                print(self.party.whose_turn)
                print(self.party.waiting_for)
                print(self.party.fields_to_move)

if __name__=="__main__":
    p = PartyTerm()
    p.run()
