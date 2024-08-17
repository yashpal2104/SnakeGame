from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", 'r') as data:
            self.highscore = int(data.read())
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 230)
        self.updateScoreboard()

    def updateScoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score:{self.highscore}", move=False, align="center",
                   font=("Arial", 24, "normal"))

    def increaseScore(self):
        self.score += 1
        self.updateScoreboard()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode='w') as data:
                data.write(f"{self.highscore}")

        self.score = 0
        self.updateScoreboard()

    def increase_score(self):
        self.score += 1
        self.updateScoreboard()

    # def endgame(self):
    #     self.goto(0,0)
    #     self.write(f"Game Over.", move=False, align="center", font=("Arial", 18, "normal"))
