import random  # 导入随机模块用于生成随机数

class Guess:
    def __init__(self):
        # 初始化游戏状态
        self.target_number = None  # 目标数字
        self.guesses = []  # 存储用户的猜测
        self.max_guesses = 10  # 最大猜测次数
        self.attempts_left = self.max_guesses  # 剩余猜测次数

    def start(self):
        # 启动游戏
        self.target_number = random.randint(0, 100)  # 随机生成一个 0 到 100 之间的目标数字
        self.guesses = []  # 清空之前的猜测
        self.attempts_left = self.max_guesses  # 重置剩余猜测次数
        return {"message": "游戏已开始，请猜一个数字。", "max_guesses": self.max_guesses}  # 返回游戏启动信息

    def make_guess(self, guess):
        # 处理用户的猜测
        if self.target_number is None:
            return {"status": "error", "message": "游戏未开始，请先启动游戏。"}  # 检查游戏是否已启动

        if self.attempts_left <= 0:
            return {
                "status": "game_over",  # 发送游戏结束状态
                "message": f"很遗憾，正确答案是：{self.target_number}",  # 游戏结束时返回正确答案
                "correct_number": self.target_number
            }

        self.guesses.append(guess)  # 记录用户的猜测
        self.attempts_left -= 1  # 每次猜测后减少剩余尝试次数

        # 判断猜测结果
        if guess < self.target_number:
            return {"status": "too_low", "message": "太小了", "attempts": len(self.guesses), "remaining": self.attempts_left}  # 猜的数字太小
        elif guess > self.target_number:
            return {"status": "too_high", "message": "太大了", "attempts": len(self.guesses), "remaining": self.attempts_left}  # 猜的数字太大
        else:
            return {
                "status": "correct",
                "message": f"正确答案就是：{self.target_number}",  # 猜对了
                "attempts": len(self.guesses),
                "correct": True
            }