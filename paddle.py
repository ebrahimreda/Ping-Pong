from turtle import Turtle

class Paddle(Turtle):    
    def __init__(self,pos_X,pos_Y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(pos_X,pos_Y)
        self.shapesize(6,1)

    def run_up (self):
        new_y = self.ycor() + 40  
        if new_y < 280: 
            self.goto(self.xcor(), new_y)



    def run_down (self):
        new_y = self.ycor() - 40
        if new_y > -280: 
            self.goto(self.xcor(), new_y) 
    
        