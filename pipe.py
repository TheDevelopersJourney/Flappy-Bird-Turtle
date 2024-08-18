from turtle import Turtle



class Pipe(Turtle):
    def __init__(self):
        super().__init__()
        self.color('green')
        self.movement = 6
        self.speed(0)
        self.hideturtle()
        self.penup()
        self.shape("pipe2.gif")
        self.goto(450, 350)
        self.showturtle()



    def pipe_movement(self):
        x = self.xcor()
        self.setx(x - self.movement)

    def increase_speed(self):
        self.movement = 7


class Pipe2(Turtle):
    def __init__(self):
        super().__init__()
        self.color('green')
        self.movement = 6
        self.speed(0)
        self.hideturtle()
        self.penup()
        self.shape("pipe.gif")
        self.goto(450, -350)
        self.showturtle()

    def pipe_movement(self):
        x = self.xcor()
        self.setx(x - self.movement)

    def increase_speed(self):
        self.movement = 7
