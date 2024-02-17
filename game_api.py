from flask import Flask, jsonify

import Live
import Utils

app = Flask(__name__)


@app.route('/welcome', methods=['GET'])
def welcome():
    """
    Returns a welcome message for the user.
    """
    return Live.welcome("Maxim")


@app.route('/games', methods=['GET'])
def get_games():
    """
    Returns a list of available games with their descriptions.
    """
    game_descriptions = {
        1: {"name": "Memory Game", "description": "a sequence of numbers will appear for 1 second and you have to guess it back"},
        2: {"name": "Guess Game", "description": "guess a number and see if you can choose like the computer"},
        3: {"name": "Currency Roulette", "description": "try and guess the value of a random amount of USD in ILS"},
    }

    games = [{
        "id": game_id,
        "name": game_data["name"],  # Access nested values
        "description": game_data["description"]
    } for game_id, game_data in game_descriptions.items()]  # Iterate over nested data

    return jsonify(games)


@app.route('/play_game/<int:game_id>/<int:difficulty>', methods=['GET'])
def play_game(game_id, difficulty):
    """
    Executes a chosen game based on user selection and difficulty level.
    Returns the game result in JSON format.
    """
    # Placeholder for actual game logic
    game_result = {"win": Live.play_game_based_on_user_choice(game_id, difficulty),
                   "message": "Game Not Implemented Yet"}

    # Simulate different results based on game ID
    if game_id == 1:
        game_result["message"] = "Playing Memory Game with difficulty {}".format(difficulty)
    elif game_id == 2:
        game_result["message"] = "Playing Guess Game with difficulty {}".format(difficulty)
    elif game_id == 3:
        game_result["message"] = "Playing Currency Roulette with difficulty {}".format(difficulty)

    return jsonify(game_result)


if __name__ == '__main__':
    app.run(host=Utils.HOST, debug=False, threaded=True, port=Utils.PORT)
