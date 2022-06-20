import random

class Die():

    def __init__(self, sides = 6):
        self.sides = sides

    def roll_die(self):
        print(random.randint(1, self.sides))
    
cube_6 = Die()
cube_6.roll_die()

cube_10 = Die(10)
cube_10.roll_die()

cube_20 = Die(20)
cube_20.roll_die()