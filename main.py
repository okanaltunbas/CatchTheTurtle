import random
import time
import turtle

global score, randomPosx, randomPosy, gameBool
gameBool = True
score = 0

#Screen Settings
myScreen = turtle.Screen()
myScreen.setup(width=1000, height=1000)
myScreen.bgcolor("light blue")
myScreen.title("Catch The Turtle")

#Turtle Settings
myTurtle = turtle.Turtle()
myTurtle.shape("turtle")
myTurtle.color("green")
myTurtle.shapesize(2, 2, 3)
myTurtle.penup()
myTurtle.speed(0)

#scoreTurtle Settings
scoreTurtle = turtle.Turtle()
scoreTurtle.hideturtle()
scoreTurtle.color("blue")
scoreTurtle.penup()
scoreTurtle.speed(0)
scoreTurtle.goto(0, 450)
scoreTurtle.write(f"Score : {score}", font=("Arial", 24, "normal"), align="center")

#timeTurtle Settings
timeTurtle = turtle.Turtle()
timeTurtle.hideturtle()
timeTurtle.color("black")
timeTurtle.penup()
timeTurtle.speed(0)
timeTurtle.goto(0, 400)
timeTurtle.write(f"Time : {20} ", font=("Arial", 24, "normal"), align="center")

def RandomPosition():
    global randomPosx, randomPosy
    randomPosx = random.randint(-475,450)
    randomPosy = random.randint(-450,450)
    myTurtle.goto(randomPosx, randomPosy)

def TimeWrite(t):
    timeTurtle.clear()
    timeTurtle.write(f"Time : {t} ", font=("Arial", 24, "normal"), align="center")

def TimeCounter(gameTime):
    global gameBool

    while gameTime > 0:
        print(gameTime)
        time.sleep(1)  #1 saniye beklet
        gameTime -= 1
        TimeWrite(gameTime)
        if gameTime == 0:
            gameBool = False
            myTurtle.color("red")
        RandomPosition()


def ClickScreen(x, y):
    global score

    if (abs(randomPosx - x) < 50) & (abs(randomPosy - y) < 50) & gameBool :
        score += 1
        scoreTurtle.clear()
        scoreTurtle.write(f"Score : {score}", font=("Arial", 24, "normal"), align="center")


turtle.onscreenclick(ClickScreen)

TimeCounter(20)

turtle.mainloop()