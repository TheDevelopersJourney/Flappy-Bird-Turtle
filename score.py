from turtle import Turtle
class Score(Turtle):
    def __init__(self,):
        super().__init__()
        self.points = 0
        with open('data.txt') as data:
            self.highscore = int(data.read())
        self.speed(0)
        self.hideturtle()
        self.penup()
        self.color("White")
        self.goto(-250, 215)


    def write_score(self,):
        self.write(f"Score: {self.points}\nHighScore: {self.highscore}", font=('Arial', 30, 'normal'))


    def reset(self):
        if self.points >= self.highscore:
            self.highscore = self.points
            with open('data.txt',mode='w') as data:
                data.write(str(self.highscore))



