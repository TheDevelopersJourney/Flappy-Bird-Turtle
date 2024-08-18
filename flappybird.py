from turtle import Turtle

class FlappyBird(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.speed(5)
        self.weight = 10
        self.jump_height = 60
        self.penup()
        self.shape("square")
        self.color("black")


    def jump(self):
        yloc = self.ycor()
        xloc = self.xcor()
        self.setpos(x=xloc, y=yloc+self.jump_height)
        self.setx(0)



    def gravity(self):
        y = self.ycor()
        self.sety(y - self.weight)



    def increased_gravity(self):
        self.weight = 12





