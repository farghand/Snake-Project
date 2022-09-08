from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__(visible=False)
        self.score = 0
        self.pu()
        self.color("cyan")
        self.goto(0, 270)
        self.refresh_score()

    def update_score(self):
        self.score += 1
        self.refresh_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

    def refresh_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
