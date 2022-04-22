from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title='make your bet', prompt='which turtle will win the race? Enter a colour ')

colors = ['red','orange','yellow','green','blue','purple']
turtles = ['pallu','jivu','pushpa','udaya','titoo','paji']
all_turtles = []

x = -230
y = -100
for i in range(0,len(colors)):
    t = turtles[i]
    t = Turtle(shape='turtle')
    all_turtles.append(t)
    t.color(colors[i])
    t.penup()
    t.goto(x=x, y=y)
    y += 50

if user_bet:
    is_race_on = True
    
while is_race_on:
    
    for turtle in all_turtles:
        rand_distance = random.randint(0,10)
        
        if turtle.xcor() > 230:
            is_race_on = False
            winning_colour = turtle.pencolor()
            
            if winning_colour == user_bet:
                print('you won. the winning color is {}'.format(winning_colour))
            else:
                print('you lost. the winning color is {}'.format(winning_colour))
        else:
            turtle.forward(rand_distance)



screen.exitonclick()