import random  # 导入随机模块用于生成随机数

class ShooterGame:
    def __init__(self):
        # 初始化游戏状态
        self.player_pos = [400, 550]  # 玩家初始位置
        self.player_size = 50  # 玩家大小
        self.enemy_speed = 5  # 敌人下落速度
        self.bullet_speed = 20  # 子弹上升速度
        self.score = 0  # 初始化分数
        self.enemies = []  # 敌人列表
        self.bullets = []  # 子弹列表

    def move_player(self, direction):
        # 根据方向移动玩家
        if direction == 'left' and self.player_pos[0] > 0:  # 向左移动
            self.player_pos[0] -= 10
        elif direction == 'right' and self.player_pos[0] < 800 - self.player_size:  # 向右移动
            self.player_pos[0] += 10

    def shoot(self):
        # 玩家射击时创建子弹
        bullet_pos = [self.player_pos[0] + self.player_size // 2, self.player_pos[1]]  # 子弹初始位置
        self.bullets.append(bullet_pos)  # 将子弹添加到子弹列表

    def drop_enemies(self):
        # 随机生成敌人
        if len(self.enemies) < 10 and random.random() < 0.1:  # 限制最多10个敌人
            x_pos = random.randint(0, 800 - self.player_size)  # 随机生成敌人横坐标
            self.enemies.append([x_pos, 0])  # 将敌人添加到敌人列表

    def update_enemy_positions(self):
        # 更新敌人的位置
        for enemy in self.enemies[:]:  # 遍历敌人列表的副本
            enemy[1] += self.enemy_speed  # 敌人向下移动
            if enemy[1] > 600:  # 如果敌人超出屏幕底部
                self.enemies.remove(enemy)  # 从列表中移除敌人
                self.score += 1  # 增加分数

    def update_bullet_positions(self):
        # 更新子弹的位置
        for bullet in self.bullets[:]:  # 遍历子弹列表的副本
            bullet[1] -= self.bullet_speed  # 子弹向上移动
            if bullet[1] < 0:  # 如果子弹超出屏幕顶部
                self.bullets.remove(bullet)  # 从列表中移除子弹

    def check_collisions(self):
        # 检查碰撞
        for enemy in self.enemies:
            if self.detect_collision(enemy, self.player_pos):  # 检查敌人与玩家的碰撞
                return True  # 如果碰撞，返回 True
            for bullet in self.bullets:
                if self.detect_collision(bullet, enemy):  # 检查子弹与敌人的碰撞
                    self.bullets.remove(bullet)  # 移除子弹
                    self.enemies.remove(enemy)  # 移除敌人
                    self.score += 5  # 增加分数
                    break  # 退出子弹循环
        return False  # 如果没有碰撞，返回 False

    def detect_collision(self, obj1, obj2):
        # 检测两个对象之间的碰撞
        return (obj1[0] < obj2[0] + self.player_size and
                obj1[0] + self.player_size > obj2[0] and
                obj1[1] < obj2[1] + self.player_size and
                obj1[1] + self.player_size > obj2[1])