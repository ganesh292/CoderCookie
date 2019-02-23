from turtle import *
import random

if __name__ == "__main__":
    bgcolor('black')
    turtle1 = Turtle()
    turtle1.speed("fastest")
    turtle1.color("red")
    turtle1.setposition(0,200)
    turtle2 = Turtle()
    turtle2.speed("fastest")
    turtle2.color("green")
    turtle2.setposition(0,-200)

    colors = ["red", "green", "blue" , "yellow", "purple", "pink", "orange", "white"]
    for i in range(1, 12):
        turtle1.color(random.choice(colors))
        for j in range(1, 60):     #turtle1 draws circles from smallest to biggest
            turtle1.circle(j)
        for j in range(60,1, -1):  #turtle2 draws circles from biggest to smallest
            turtle2.circle(j)
        turtle1.right(36)
        turtle2.right(36)

    exitonclick()
