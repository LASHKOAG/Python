#главный класс
class Things:
    pass

#первый потомок главного класса
class Inanimate(Things):
    pass

class Animate(Things):
    pass

class Sidewalks(Inanimate):
    pass

class Animals(Animate):
    def breathe(self):
        print("дышит\n")
    def move(self):
        print("передвигается\n")
    def eat_food(self):
        print("кушает\n")
    

class Mammals(Animals):
    def feed_young_with_milk(self):
        print("кормит детенышей молоком\n")
        
class Giraffes(Mammals):
    def eat_leaves_from_trees(self):
        print("кушает листья\n")


reginald = Giraffes()
reginald.move()
reginald.eat_leaves_from_trees()

harold = Giraffes()
harold.move()

import turtle
avery = turtle.Pen()
kate = turtle.Pen()

avery.forward(50)
avery.right(90)
avery.forward(20)

import time
time.sleep (10)

kate.left(90)
kate.forward(100)

time.sleep(10)

jacob = turtle.Pen()
jacob.left(180)
jacob.forward(80)

time.sleep(10)
