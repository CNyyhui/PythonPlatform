import random  # 导入随机模块以生成随机选择

class RSP:
    def __init__(self):
        # 初始化用户分数和电脑分数
        self.user_score = 0
        self.computer_score = 0

    def get_computer_choice(self):
        # 随机选择电脑的选项（石头、布、剪刀）
        return random.choice(['石头', '布', '剪刀'])

    def determine_winner(self, user_choice, computer_choice):
        # 根据用户和电脑的选择确定胜者
        if user_choice == computer_choice:
            return '平局'  # 如果选择相同，返回平局
        elif (user_choice == '石头' and computer_choice == '剪刀') or \
             (user_choice == '剪刀' and computer_choice == '布') or \
             (user_choice == '布' and computer_choice == '石头'):
            self.user_score += 1  # 用户获胜，增加用户分数
            return '你赢了！'  # 返回用户胜利信息
        else:
            self.computer_score += 1  # 电脑获胜，增加电脑分数
            return '电脑赢了！'  # 返回电脑胜利信息

    def check_winner(self):
        # 检查是否有一方达到胜利条件（分数达到3）
        if self.user_score >= 3:
            winner = '你赢了游戏！'  # 用户胜利信息
            self.reset_scores()  # 重置分数
            return winner  # 返回用户胜利信息
        elif self.computer_score >= 3:
            winner = '电脑赢了游戏！'  # 电脑胜利信息
            self.reset_scores()  # 重置分数
            return winner  # 返回电脑胜利信息
        return None  # 如果没有胜利者，返回 None

    def reset_scores(self):
        # 重置用户和电脑的分数
        self.user_score = 0
        self.computer_score = 0