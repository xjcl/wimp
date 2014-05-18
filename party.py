import boards.a as ba

class Party(object):
    
    class Char(object):
        def __init__(self, name):
            self.coins = 10
            self.name = str(name)
            self.is_on = None
        def __str__(self):
            return self.name
        
    def __init__(self):
        self.board = ba.Board()
        self.chars = [self.Char(0), self.Char(1), self.Char(2), self.Char(3)]
        for c in self.chars:
            c.is_on = self.board.init_field
        
    def move_by(self, char, n):
        from_field = char.is_on
        while n > 0:
            to_field = from_field.next
            n -= 1
        to_field.land(char)


p = Party()
p.move_by(p.chars[0], 1)
p.move_by(p.chars[0], 1)
p.move_by(p.chars[0], 1)
p.move_by(p.chars[0], 1)
p.move_by(p.chars[0], 1)
p.move_by(p.chars[0], 1)

print("coin totals:")
for c in p.chars:
    print(c.coins)

