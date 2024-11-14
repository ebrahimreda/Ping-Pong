from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(0.8)
   
        self.speed_x = 10
        self.speed_y = 10
        self.x_move = self.speed_x
        self.y_move = self.speed_y
        

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def Speed(self, speed_increase):
        
        if self.x_move > 0:
            self.x_move = self.speed_x + speed_increase
        else:
            self.x_move = -self.speed_x - speed_increase

        if self.y_move > 0:
            self.y_move = self.speed_y + speed_increase
        else:
            self.y_move = -self.speed_y - speed_increase
