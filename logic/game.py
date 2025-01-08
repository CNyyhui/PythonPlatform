import random

class Game:
    def __init__(self):
        self.target_number = None
        self.guesses = []
        self.max_guesses = 10

    def start(self):
        self.target_number = random.randint(0, 100)
        self.guesses = []

    def make_guess(self, guess):
        if not self.target_number:
            return {"message": "Game not started"}

        if len(self.guesses) >= self.max_guesses:
            return {
                "message": f"很遗憾，正确答案是：{self.target_number}",
                "correct_number": self.target_number
            }

        self.guesses.append(guess)

        if guess < self.target_number:
            return {"message": "小了", "attempts": len(self.guesses)}
        elif guess > self.target_number:
            return {"message": "大了", "attempts": len(self.guesses)}
        else:
            return {
                "message": f"正确答案就是：{self.target_number}",
                "attempts": len(self.guesses)
            }