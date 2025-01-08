import random

class Minesweeper:
    def __init__(self, rows, cols, mines):
        # 定义行数
        self.rows = rows
        # 定义列数
        self.cols = cols
        # 定义地雷数量
        self.mines = mines
        # 创建雷区
        self.minefield = self.create_minefield()
        # 创建一个布尔矩阵，用于跟踪已揭示的格子
        self.revealed = [[False] * cols for _ in range(rows)]

    # 创建挖矿区域
    def create_minefield(self):
        # 初始化雷区，所有格子初始为 '0'
        minefield = [['0'] * self.cols for _ in range(self.rows)]
        # 用于存储地雷的位置
        mine_positions = set()

        # 随机放置地雷
        while len(mine_positions) < self.mines:
            # 随机选择行
            x = random.randint(0, self.rows - 1)
            # 随机选择列
            y = random.randint(0, self.cols - 1)
            # 确保不重复放置地雷
            if (x, y) not in mine_positions:
                mine_positions.add((x, y))
                # 将地雷标记为 'M'
                minefield[x][y] = 'M'

                # 更新周围格子的数字
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if 0 <= x + dx < self.rows and 0 <= y + dy < self.cols and minefield[x + dx][y + dy] != 'M':
                            # 将周围格子的数字加 1
                            minefield[x + dx][y + dy] = str(int(minefield[x + dx][y + dy]) + 1)
        # 返回生成的雷区
        return minefield

    # 揭示指定位置的格子
    def reveal_cell(self, x, y):
        # 如果是地雷，返回 False
        if self.minefield[x][y] == 'M':
            return False
        # 否则将格子标记为已揭示
        self.revealed[x][y] = True
        return True

    # 检查游戏是否胜利
    def is_game_won(self):
        # 如果所有非地雷的格子都被揭示，返回 True
        return all(all(self.revealed[i][j] or self.minefield[i][j] == 'M' for j in range(self.cols)) for i in range(self.rows))

    # 获取当前雷区的显示状态
    def get_display(self):
        # 返回一个显示矩阵，揭示的格子显示其内容，未揭示的格子显示 '-'
        return [[str(self.minefield[i][j]) if self.revealed[i][j] else '-' for j in range(self.cols)] for i in range(self.rows)]