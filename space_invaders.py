#space invaders part 1
#by Johnnie Gilkerson

import turtle
import winsound
import math
import random

#set up screen
from turtle import _Screen
from typing import Any, Union

wn: Union[_Screen, Any] = turtle.Screen()

wn.bgcolor("black")
wn.title("Spaced Invaders")
wn.bgpic("space.gif")

winsound.PlaySound("game.wav", winsound.SND_ASYNC)




#register the shape
turtle.register_shape("player.gif")
turtle.register_shape("invaders.gif")


#draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(560)
    border_pen.lt(90)
border_pen.hideturtle()

# set score to zero
score = 0

#draw the score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 220)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align="left",font=("Arial", 14, "normal"))
score_pen.hideturtle()


#create the players
player = turtle.Turtle()
player.color("blue")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0 ,-250)
player.setheading(90)

playerspeed = 15







#choose number of enemies

number_of_enemies = 10
enemies = []

    #add enemies to the list
for i in range(number_of_enemies):
    enemies.append(turtle.Turtle())


for enemy in enemies:
    enemy.color("red")
    enemy.shape("invaders.gif")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)


enemyspeed = 3




#create the players bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 30

#bullet state
bulletstate = "ready"


#move player left and right
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

def fire_bullet():
    global bulletstate
    winsound.PlaySound("sound4.wav",winsound.SND_ASYNC)
    #delay = input("press enter to finish")
    x = player.xcor()
    y = player.ycor() + 10
    bullet.setposition(x, y)
    bullet.showturtle()

def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False



#create keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")


#main game loop
while True:
    for enemy in enemies:
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        #move enemy back and down
        if enemy.xcor() > 240:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemyspeed *= -1
        if enemy.xcor() < -290:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemyspeed *= -1

        if isCollision(bullet, enemy):
            winsound.PlaySound("explode.wav", winsound.SND_ASYNC)
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            x = random.randint(-200, 200)
            y = random.randint(100, 150)
            enemy.setposition(-200, 240)
            # update score
            score += 10
            scorestring = "Score: %s" % score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))

        if isCollision(player, enemy):
            player.hideturtle()
            enemy.hideturtle()
            winsound.PlaySound("explode.wav", winsound.SND_ASYNC)
            print("GAME OVER")
            break

        #move bullet

    #if bulletstate == "fire":
    y = bullet.ycor()
    y += bulletspeed
    bullet.sety(y)

    #check to see if bullet has gone off screen
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"

    if isCollision(bullet,enemy):
        bullet.hideturtle()
        bulletstate = "ready"
        bullet.setposition(0,-400)

        enemy.setposition(-200, 250)

    if isCollision(player,enemy):

        player.hideturtle()
        enemy.hideturtle()
        print ("GAME OVER")
        break













wn.mainloop()





