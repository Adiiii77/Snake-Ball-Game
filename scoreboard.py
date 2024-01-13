from turtle import Turtle
FONT_COLOR = "white"
FONT = ('Courier', 24, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.print_score()
        self.color(FONT_COLOR)
        self.hideturtle()

    def print_score(self):
        self.penup()
        self.goto(-85, 265)
        self.clear()
        self.write(f"Score: {self.score}", move=False, font=FONT)

    def incr_score(self):
        self.score += 1

    def game_over(self):
        self.goto(-98, 0)
        self.write("GAME OVER!", move=False, font=FONT)

