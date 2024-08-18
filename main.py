from turtle import Screen, Turtle
from flappybird import FlappyBird
from pipe import Pipe, Pipe2
from score import Score
import random
from menu import MainMenu, MenuSelect


screen = Screen()
screen.setup(600, 600)
screen.colormode(255)
screen.bgcolor(148, 229, 243)
screen.register_shape('Nyan-Cat.gif')


y=0
bird = FlappyBird()
bird.shape("Nyan-Cat.gif")


# SCORE
score = Score()


# pipe locations
y_loc = [85, 140, 425, 275, 500]



screen.register_shape('pipe.gif')
screen.register_shape('pipe2.gif')



# Jump key
screen.listen()
screen.onkey(bird.jump, "w")

# PIPES
top_pipe_list = []
bottom_pipe_list = []


def create_pipes():
    for _ in range(2):
        _ = Pipe()
        top_pipe_list.append(_)
        _ = Pipe2()
        bottom_pipe_list.append(_)



def set_pipe_locations():
    top_pipe_list[1].setx(900)
    bottom_pipe_list[1].setx(top_pipe_list[1].xcor())

    top_pipe_list[1].sety(random.choice(y_loc))
    bottom_pipe_list[1].sety(top_pipe_list[1].ycor() - 650)

def gameplay():
    top_pipe_list[0].pipe_movement()
    bottom_pipe_list[0].pipe_movement()
    top_pipe_list[1].pipe_movement()
    bottom_pipe_list[1].pipe_movement()



    if top_pipe_list[0].xcor() < -450:
        top_pipe_list[0].hideturtle()
        bottom_pipe_list[0].hideturtle()
        top_pipe_list[0].goto(x=top_pipe_list[1].xcor()+450, y=random.choice(y_loc))
        bottom_pipe_list[0].goto(x=top_pipe_list[1].xcor()+450,y= top_pipe_list[0].ycor() - 650)
        top_pipe_list[0].showturtle()
        bottom_pipe_list[0].showturtle()



    if top_pipe_list[1].xcor() < -450:
        top_pipe_list[1].hideturtle()
        bottom_pipe_list[1].hideturtle()
        top_pipe_list[1].goto(x=top_pipe_list[0].xcor()+450, y=random.choice(y_loc))
        bottom_pipe_list[1].goto(x=top_pipe_list[0].xcor()+450,y=top_pipe_list[1].ycor() - 650)
        top_pipe_list[1].showturtle()
        bottom_pipe_list[1].showturtle()


play = True
play_again = False

def restart():
    global play_again
    if menu_select.ycor() == 125:
        play_again = True
    elif menu_select.ycor() == -80:
        screen.bye()


menu_select = MenuSelect()
menu = MainMenu()


screen.onkey(menu_select.move_down,key='Down')
screen.onkey(menu_select.move_up,key='Up')

def Game_over():
    if play_again == False:
        menu.showmenu()
        menu_select.showturtle()
        bird.hideturtle()
        top_pipe_list[0].goto(450, 350)
        bottom_pipe_list[0].goto(450, -300)
        set_pipe_locations()
    else:
        return


def Game_on():
    score.points = 0
    score.clear()
    menu.clear()
    bird.home()
    bird.showturtle()
    score.write_score()









def program():
    menu_select.hideturtle()
    is_collide = False
    counter = 0
    create_pipes()
    set_pipe_locations()

    while not is_collide:
        counter += 0.06
        point_counter = round(counter,1)
        print(point_counter)
        bird.gravity()
        gameplay()

        for _ in top_pipe_list:
            x = _.xcor()
            y = _.ycor()
            bird_x = bird.xcor() - x
            bird_y = bird.ycor() - y
            if bird_x > -140 and bird_x < 140 and bird_y > -270 and bird_y < 270:
                is_collide = True




        for _ in bottom_pipe_list:
            x = _.xcor()
            y = _.ycor()
            bird_x = bird.xcor() - x
            bird_y = bird.ycor() - y
            if bird_x > -140 and bird_x < 140 and bird_y > -270 and bird_y < 270:
                is_collide = True



        if point_counter == 5:
            score.points += 1
            counter = 0
            score.clear()
            score.write_score()















while play:
    if play_again == True:
        Game_on()
        program()
        score.reset()
        play_again = False

    elif play_again == False:
        screen.onkey(fun=restart, key='r')
        create_pipes()
        Game_over()






    







