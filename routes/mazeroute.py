from flask import Blueprint, jsonify, render_template
from logic.maze import generate_maze

maze_blueprint = Blueprint('maze', __name__)

@maze_blueprint.route('/')
def index():
    return render_template('maze.html')

@maze_blueprint.route('/generate', methods=['GET'])
def generate():
    maze = generate_maze(21, 21)  # 生成 21x21 的迷宫
    return jsonify({"maze": maze})