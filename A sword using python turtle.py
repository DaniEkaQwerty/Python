import turtle

turtle.title("Frostpeak Glacierbane")
bg = turtle.Screen()
bg.bgcolor("light grey")
s = turtle.Turtle()
s.speed(10)
s.pensize(3)
class Holder:
    def __init__(self, size, color):
        self.size = size
        self.color = color
    def main_holder(self):
        s.pensize(self.size)
        s.left(45)
        for l in range(-160, -100, 5):
            s.penup()
            s.goto(0, l)
            s.pendown()
            s.fillcolor("#48494B")
            s.begin_fill()
            for j in range(4):
                s.forward(17)
                s.left(90)
            s.end_fill()

    def holders_down(self):
        s.penup()
        s.goto(0, -160)
        s.pendown()

        s.fillcolor(self.color)
        s.begin_fill()
        s.right(60 + 30)
        s.backward(20)
        s.right(60)
        s.forward(40)
        s.left(55)
        s.forward(40)
        s.left(55 * 2 - 5)
        s.forward(40)
        s.left(55 - 5)
        s.forward(40)
        s.left(120)
        s.forward(22)
        s.end_fill()

    def holder_up(self):
        s.penup()
        s.goto(0, -100)
        s.pendown()

        s.fillcolor(self.color)
        s.begin_fill()
        s.backward(60)
        s.right(45)
        s.forward(85)
        s.left(90 + 45)
        s.forward(60)
        s.end_fill()

class Accessories:
    def __init__(self,color1,color2,loop):
        self.color1 = color1
        self.color2 = color2
        self.loop = loop

    def right_and_left(self):

        s.penup() # Right
        s.goto(0, -60)
        s.pendown()

        s.fillcolor(self.color1)
        s.begin_fill()

        s.forward(80)
        s.left(45 + 105)
        s.forward(80)
        s.left(45)
        s.forward(20)
        s.left(45 + 45)
        s.forward(40)
        s.end_fill()

        s.penup() # Left
        s.goto(0, -60)
        s.pendown()

        s.fillcolor(self.color2)
        s.begin_fill()

        s.right(15)
        s.forward(80)
        s.right(60 + 90)
        s.forward(80)
        s.right(45)
        s.forward(20)
        s.right(45 + 45)
        s.forward(42)

        s.end_fill()

    def Acc_right(self):
        for i in range(self.loop):

            s.penup()
            s.goto(20, -30)
            s.pendown()

            c = ['royal blue','blue','dark blue']

            s.fillcolor(c[0])
            s.begin_fill()
            if i == 2:
                s.fillcolor(c[1])
            elif i == 1:
                s.fillcolor(c[2])

            s.right(15)
            s.forward(90)
            s.right(60 + 90)
            s.forward(90)
            s.right(45)
            s.forward(20)
            s.right(45 + 45)
            s.forward(42)

            s.end_fill()

class Sword:
    def __init__(self,first_color,second_color):
        self.first_color = first_color
        self.second_color = second_color
    def Sword(self):
        '''Sword'''
        s.fillcolor(self.first_color)
        s.left(60)
        s.penup()
        s.goto(35, -14)
        s.pendown()

        s.begin_fill()
        s.right(90)
        s.forward(270)
        s.left(45)
        s.forward(50)
        s.left(90)
        s.forward(50)
        s.left(45)
        s.forward(300)

        s.left(40 + 90)
        s.forward(20)
        s.right(40)
        s.forward(37)
        s.left(45)
        s.forward(30)
        s.end_fill()
        s.backward(25)

    def core_sword(self):
        s.fillcolor(self.second_color)
        s.begin_fill()
        s.left(45)
        s.forward(270)
        s.left(45)
        s.forward(30)
        s.left(90)
        s.forward(30)
        s.left(45)
        s.forward(275)
        s.left(90)
        s.forward(42)
        s.end_fill()

class Accessories2:
    def __init__(self,particle):
        self.particle = particle
    def Acc_left(self):
        for j in range(2):
            s.penup()
            s.goto(-20, -27)
            s.pendown()
            s.fillcolor('royal blue')
            s.begin_fill()
            if j == 2:
                s.fillcolor('blue')  # 1
            elif j == 0:
                s.fillcolor('royal blue')  # 1
            elif j == 1:
                s.fillcolor('dark blue')
            s.left(15)
            s.backward(90)
            s.left(60 + 90)
            s.backward(90)
            s.left(45)
            s.backward(20)
            s.left(45 + 45)
            s.backward(42)
            s.end_fill()

        "diamon"
        s.fillcolor(self.particle)
        s.penup()
        s.goto(-13, -60)
        s.pendown()
        s.backward(25)
        s.left(55)

        s.begin_fill()
        s.forward(25)
        s.right(52)
        s.forward(25)
        s.right(125)
        s.forward(25)
        s.end_fill()

class Particle(Accessories2):
    def __init__(self,particle,x1,x2,y1,y2):
        super().__init__(particle)
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def last_particle(self):
        s.fillcolor(self.particle) #particle left
        s.penup()
        s.goto(self.x1,self.y1)
        s.pendown()
        s.backward(25)
        s.left(55)
        s.begin_fill()
        s.forward(25)
        s.right(52)
        s.forward(25)
        s.right(125)
        s.forward(25)
        s.end_fill()

        s.fillcolor(self.particle) #particle right
        s.penup()
        s.goto(self.x2,self.y2)
        s.pendown()
        s.backward(25)
        s.left(55)
        s.begin_fill()
        s.forward(25)
        s.right(52)
        s.forward(25)
        s.right(125)
        s.forward(25)
        s.end_fill()

def FullSword():

    '''Holder'''
    holder = Holder(2,"#777B7E")
    holder.main_holder()
    holder.holders_down()
    holder.holder_up()

    '''Accessories'''
    accessories = Accessories("sky blue","blue",3)
    accessories.right_and_left()
    accessories.Acc_right()

    '''Sword'''
    sword = Sword("cyan","dark blue")
    sword.Sword()
    sword.core_sword()

    '''Accessories2'''
    accessories2 = Accessories2("cyan")
    accessories2.Acc_left()

    '''Particle'''
    particle = Particle("cyan",-30,40,-37,-60)
    particle.last_particle()

FullSword()

turtle.done()