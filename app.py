from flask import Flask, render_template
from routes.rsproute import rsp_blueprint
from routes.guessroute import guess_blueprint
from routes.minesweeperroute import minesweeper_blueprint
from routes.mazeroute import maze_blueprint
from routes.shooterroute import shooter_blueprint

app = Flask(__name__)

# 注册 ！蓝      图！
# 注册 猜数字的蓝图
app.register_blueprint(guess_blueprint, url_prefix='/guess')
# 注册 猜拳的蓝图
app.register_blueprint(rsp_blueprint, url_prefix='/rsp')
# 注册 扫雷的蓝图
app.register_blueprint(minesweeper_blueprint, url_prefix='/minesweeper')
# 注册 迷宫的蓝图
app.register_blueprint(maze_blueprint, url_prefix='/maze')
# 注册 射击游戏蓝图
app.register_blueprint(shooter_blueprint, url_prefix='/shooter')

@app.route('/')
def home():
    # 初始确定为主页面
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
