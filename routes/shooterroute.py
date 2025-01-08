from flask import Blueprint, jsonify, render_template
from logic.shooter import ShooterGame

shooter_blueprint = Blueprint('shooter', __name__)
game_instance = ShooterGame()

@shooter_blueprint.route('/')
def index():
    return render_template('shooter.html')

@shooter_blueprint.route('/move/<direction>', methods=['GET'])
def move(direction):
    game_instance.move_player(direction)
    return jsonify({"player_pos": game_instance.player_pos})

@shooter_blueprint.route('/shoot', methods=['POST'])
def shoot():
    game_instance.shoot()
    return jsonify({"bullets": game_instance.bullets})

@shooter_blueprint.route('/update', methods=['GET'])
def update():
    game_instance.drop_enemies()
    game_instance.update_enemy_positions()
    game_instance.update_bullet_positions()
    game_over = game_instance.check_collisions()
    return jsonify({
        "player_pos": game_instance.player_pos,
        "enemies": game_instance.enemies,
        "bullets": game_instance.bullets,
        "score": game_instance.score,
        "game_over": game_over
    })

@shooter_blueprint.route('/restart', methods=['POST'])
def restart():
    global game_instance
    game_instance = ShooterGame()
    return jsonify({"message": "Game restarted"})