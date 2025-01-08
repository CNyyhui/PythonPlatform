from flask import Blueprint, render_template, request, jsonify
from logic.minesweeper import Minesweeper

# 创建一个蓝图用于扫雷游戏
minesweeper_blueprint = Blueprint('minesweeper', __name__)

# 初始化游戏实例的全局变量
minesweeper_game = None

# 定义根路由，渲染扫雷游戏的主页面
@minesweeper_blueprint.route('/')
def minesweeper_index():
    return render_template('minesweeper.html')

# 定义启动游戏的路由
@minesweeper_blueprint.route('/start_game', methods=['POST'])
def start_game():
    # 使用全局变量建立一个实例
    global minesweeper_game
    # 获取请求中的 JSON 数据
    data = request.json
    # 获取行数，默认为 5
    rows = data.get('rows', 5)
    # 获取列数，默认为 5
    cols = data.get('cols', 5)
    # 获取地雷数量，默认为 5
    mines = data.get('mines', 5)
    # 初始化 Minesweeper 实例
    minesweeper_game = Minesweeper(rows, cols, mines)
    # 返回游戏启动的状态
    return jsonify({"status": "Game started"})

# 定义揭示格子的路由
@minesweeper_blueprint.route('/reveal_cell', methods=['POST'])
def reveal_cell():
    # 使用全局变量
    global minesweeper_game
    # 获取要揭示的格子的坐标
    x, y = request.json.get('x'), request.json.get('y')
    # 尝试揭示格子
    if minesweeper_game.reveal_cell(x, y):
        # 检查游戏是否胜利
        game_won = minesweeper_game.is_game_won()
        return jsonify({"status": "Cell revealed", "minefield": minesweeper_game.get_display(), "game_won": game_won})
    else:
        # 返回踩雷的信息
        return jsonify({"status": "Hit a mine", "minefield": minesweeper_game.get_display()})

# 定义重置游戏的路由
@minesweeper_blueprint.route('/reset_game', methods=['POST'])
def reset_game():
    # 使用全局变量
    global minesweeper_game
    # 重置游戏实例
    minesweeper_game = None
    # 返回重置状态
    return jsonify({"status": "Game reset"})