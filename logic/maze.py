import random  # 导入随机模块以生成随机数

def generate_maze(width, height):
    # 创建一个初始迷宫，所有位置用 '#' 表示（墙）
    maze = [['#'] * width for _ in range(height)]
    # 定义四个可能的方向（上、下、左、右）
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def carve_passage(x, y):
        # 将当前单元格设为空格（通路）
        maze[y][x] = ' '
        random.shuffle(directions)  # 随机打乱方向顺序
        for dx, dy in directions:
            # 计算下一个单元格的位置（跳过一个单元格）
            nx, ny = x + dx * 2, y + dy * 2
            # 检查新位置是否在迷宫范围内且未被访问（仍为墙）
            if 0 <= nx < width and 0 <= ny < height and maze[ny][nx] == '#':
                # 将当前方向的墙打通
                maze[y + dy][x + dx] = ' '
                # 递归地从新位置继续挖掘通路
                carve_passage(nx, ny)

    # 随机选择起始位置，确保是偶数坐标
    start_x, start_y = random.randrange(0, width, 2), random.randrange(0, height, 2)
    carve_passage(start_x, start_y)  # 从起始位置开始挖掘通路

    return maze  # 返回生成的迷宫

def display_maze(maze):
    # 输出迷宫到控制台
    for row in maze:
        print("".join(row))  # 将每行的字符连接并打印