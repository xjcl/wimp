import field

class BoardA(object):
    def __init__(self):
        self.img_path = "a.png"
        # board is a directed graph
        
        # RIGHT PART
        f93 = field.Field(950, 350, ftype="blue", next=None) # CHANGED LATER IN THE CODE
        f94 = field.Field(950, 450, ftype="blue", next=f93)
        f84 = field.Field(850, 450, ftype="blue", next=f94)
        f74 = field.Field(750, 450, ftype="blue", next=f84)
        f64 = field.Field(650, 450, ftype="blue", next=f74)
        f54 = field.Field(550, 450, ftype="blue", next=f64)
        f44 = field.Field(450, 450, ftype="blue", next=f54)
        f34 = field.Field(350, 450, ftype="blue", next=f44)
        f24 = field.Field(250, 450, ftype="red" , next=f34)
        f14 = field.Field(150, 450, ftype="blue", next=f24)
        f04 = field.Field( 50, 450, ftype="blue", next=f14)
        f03 = field.Field( 50, 350, ftype="blue", next=f04)
        f02 = field.Field( 50, 250, ftype="blue", next=f03)
        
        # LEFT PART
        f01 = field.Field( 50, 150, ftype="blue", next=f02)
        f00 = field.Field( 50,  50, ftype="blue", next=f01)
        f10 = field.Field(150,  50, ftype="blue", next=f00)
        f20 = field.Field(250,  50, ftype="blue", next=f10)
        f30 = field.Field(350,  50, ftype="blue", next=f20)
        f40 = field.Field(450,  50, ftype="blue", next=f30)
        f50 = field.Field(550,  50, ftype="blue", next=f40)
        f60 = field.Field(650,  50, ftype="blue", next=f50)
        f70 = field.Field(750,  50, ftype="blue", next=f60)
        f80 = field.Field(850,  50, ftype="red" , next=f70)
        f90 = field.Field(950,  50, ftype="red" , next=f80)
        f91 = field.Field(950, 150, ftype="red" , next=f90)
        
        # MIDDLE PART
        f12 = field.Field(150, 250, ftype="chance", next=f02)
        f22 = field.Field(250, 250, ftype="chance", next=f12)
        f32 = field.Field(350, 250, ftype="red"   , next=f22)
        f42 = field.Field(450, 250, ftype="red"   , next=f32)
        f52 = field.Field(550, 250, ftype="red"   , next=f42)
        f62 = field.Field(650, 250, ftype="chance", next=f52)
        f72 = field.Field(750, 250, ftype="blue"  , next=f62)
        f82 = field.Field(850, 250, ftype="blue"  , next=f72)
        
        # JUNCTION - BOTTOM
        f92 = field.Junction(950, 250, down_next=f91, left_next=f82)
        
        # JOIN INTO A CIRCLE
        f93.next = f92
        
        finit = field.Field(450, 350, ftype="start", next=f44)
        self.init_field = finit
        self.star_field = None
        
        # ENUMERATE FIELDS -- NEEDED FOR STAR FIELD
        self.fields = [f93, f94, f84, f74, f64, f54, f44, f34, f24, f14,
                       f04, f03, f02, f01, f00, f10, f20, f30, f40, f50,
                       f60, f70, f80, f90, f91, f12, f22, f32, f42, f52,
                       f62, f72, f82, f92]
        self.blue_fields = []
        for f in self.fields:
            if f.ftype == "blue":
                self.blue_fields.append(f)


    
"""
    def __init__(self):
        # board is a directed graph
        f3 = field.Field(3,0, ftype="red", next=None) # CHANGED LATER IN THE CODE
        f2 = field.Field(2,0, ftype="blue", next=f3)
        f1 = field.Field(1,0, ftype="blue", next=f2)
        f0 = field.Field(0,0, ftype="start", next=f1)
        f3.next = f1 # CHANGED HERE; yay circles
        self.init_field = f0
"""
