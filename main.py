
from turtle import Turtle, Screen
from rgb import Rgb
import random as rnd

rgb = Rgb()
race_on = False
screen = Screen()
screen.colormode(255)

maxxi = Turtle("arrow")
maxxi.penup()
maxxi.goto(250,250)
maxxi.pendown()
maxxi.setheading(270)
maxxi.forward(500)
maxxi.hideturtle()

screen.screensize(500, 500)
colors = ["Red", "Green", "Blue", "yellow", "purple", "orange", "black"]
# user_choice = input("Enter Your Guess color!")
user_choice = screen.textinput("choice", "Enter Your Choice Color")
speed = [0, 10]


y = -250
turtles = []
for i in range(0,7):
    #hon.color(rgb.random_rgb2())
    hon = Turtle("turtle")
    hon.penup()
    # hon.color(rnd.choice(colors))
    hon.color(colors[i])
    y += 60
    hon.goto(x=-230, y=y)
    # turtle.speed(rnd.choice(speed))
    turtles.append(hon)

if user_choice:
    race_on = True

while race_on:
    for turtle in turtles:
        if turtle.xcor() > 240:
            race_on = False
            #turtle.speed(rnd.choice(speed))
            # turtle.forward(move)
            win_color = turtle.pencolor()
            if win_color == user_choice:
                print("You Won The Race!")
                turtle.goto(0,0)
                turtle.write(f"You Won The Race", align="center", font=("Cooper Black", 25, "italic"))
            else:
                print(f"You Lost! Winner is {win_color} turtle")
                turtle.goto(0, 0)
                turtle.write(f"You Lost The Race, Winner is {win_color} Color", align="center", font=("Cooper Black", 25, "italic"))
        turtle.speed(rnd.choice(speed))
        turtle.forward(rnd.randint(0, 10))
screen.exitonclick()