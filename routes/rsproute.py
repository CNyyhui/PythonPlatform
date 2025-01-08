from flask import Blueprint, render_template, request, jsonify
from logic.rsp import RSP

# 创建 Blueprint
rsp_blueprint = Blueprint('rsp', __name__)

# 初始化游戏实例
rsp_game = RSP()

@rsp_blueprint.route('/')
def rsp_index():
    return render_template('rsp.html')

@rsp_blueprint.route('/play_rsp', methods=['POST'])
def play_rsp():
    user_choice = request.json.get('choice')
    computer_choice = rsp_game.get_computer_choice()
    result = rsp_game.determine_winner(user_choice, computer_choice)
    overall_winner = rsp_game.check_winner()

    return jsonify({
        "result": result,
        "user_score": rsp_game.user_score,
        "computer_score": rsp_game.computer_score,
        "computer_choice": computer_choice,
        "overall_winner": overall_winner
    })

@rsp_blueprint.route('/reset_rsp', methods=['POST'])
def reset_rsp():
    rsp_game.reset_scores()
    return jsonify({"status": "Scores reset"})