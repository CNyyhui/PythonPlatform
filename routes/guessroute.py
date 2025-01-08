from flask import Blueprint, jsonify, request, render_template
from logic.guess import Guess  # 导入游戏逻辑

# 创建 Blueprint
guess_blueprint = Blueprint('guess', __name__)

# 初始化游戏实例
guess_instance = Guess()

@guess_blueprint.route('/')
def guess_index():
    return render_template('guess.html')

@guess_blueprint.route('/start_guess', methods=['POST'])
def start_game():
    guess_instance.start()  # 初始化游戏
    return jsonify({"status": "Game started", "max_guesses": guess_instance.max_guesses})

@guess_blueprint.route('/guess', methods=['POST'])
def make_guess():
    data = request.json
    number = data.get('number')

    # 检查输入是否有效
    if number is None or not isinstance(number, int):
        return jsonify({"error": "Invalid input, please provide a valid number."}), 400

    result = guess_instance.make_guess(number)

    # 返回错误消息
    if result.get("status") == "error":
        return jsonify(result), 400  # 返回错误状态码

    return jsonify({
        "status": result["status"],
        "attempts_left": guess_instance.attempts_left,
        "target": guess_instance.target_number if result["status"] == "correct" else None,
        "message": result.get("message")
    })