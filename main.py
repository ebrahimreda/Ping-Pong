from turtle import Screen, Turtle
from ball import Ball
from paddle import Paddle
import time

# إعداد المتغيرات الخاصة بالنقاط

def display_score():
    score_display.clear()  
    score_display.write(f"Score: {score_1}  Score: {score_2}", align="center", font=("Arial", 16, "normal"))

def reset_scores():
    global score_1, score_2
    score_1 = 0
    score_2 = 0
    display_score()  

windo = Screen()
windo.setup(width=800, height=600)
windo.bgcolor("black")
windo.title("Ping Pong")
windo.tracer(0)

ball = Ball()
sam_R = Paddle(380, 0)
sam_L = Paddle(-380, 0)

windo.listen()
windo.onkey(sam_L.run_up, "1")
windo.onkey(sam_L.run_down, "2")
windo.onkey(sam_R.run_up, "Up")
windo.onkey(sam_R.run_down, "Down")

score_display = Turtle()
score_display.hideturtle()
score_display.color("white")
score_display.penup() 
score_display.goto(0, 260) 

score_1 = 0
score_2 = 0
display_score()



game_on = True
while game_on:
    windo.update()
    ball.move()
    time.sleep(0.02)  

    if (ball.ycor() > 280) or (ball.ycor() < -280):
        ball.bounce_y()

    if (ball.distance(sam_L) < 60) and (ball.xcor() < -230 and ball.x_move < 0):
        ball.bounce_x()
        ball.Speed(1) 
        
    elif (ball.distance(sam_R) < 60) and (ball.xcor() > 230 and ball.x_move > 0):
        ball.bounce_x()
        ball.Speed(1) 

    if ball.xcor() > 400:
        ball.goto(0, 0)
        ball.x_move, ball.y_move = 10, 10
        ball.x_move *= -1 
        score_2 += 1
        display_score() 

    if ball.xcor() < -400:
        ball.goto(0, 0)
        ball.x_move, ball.y_move = 10, 10
        ball.y_move *= -1 
        score_1 += 1
        display_score()  

windo.exitonclick()

