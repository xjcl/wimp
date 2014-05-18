import field

class Board(object):

    def __init__(self):
        # board is a directed graph
        f2 = field.Field("blue", None)
        f1 = field.Field("blue", f2)
        f0 = field.Field("blue", f1)
        f2.next = f0
        self.init_field = f0
        
