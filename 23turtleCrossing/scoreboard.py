from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-290, 260)
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()   
        self.write(f"Level:{self.level}", align="left", font=FONT)   
    
    def level_up(self):
        self.level += 1
        self.update_scoreboard()
        
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)