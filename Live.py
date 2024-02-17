from Colors import *
from MemoryGame import play as memoryGame_play
from GuessGame import play as GuessGame_play
from CurrencyRouletteGame import play as CurrencyRouletteGame_play
import Utils
from flask import Flask, request, jsonify

app = Flask(__name__)

GAME_NAME = {
    1: "Memory Game",
    2: "Guess Game",
    3: "Currency Roulette Game"
}


def play_game_based_on_user_choice(game_value, difficulty_value) -> bool:
    """
    Executes a chosen game based on user selection and difficulty level.

    Args:
      game_value (int): The chosen game ID (1, 2, or 3).
      difficulty_value (int): The chosen difficulty level (1 to 5).

    Raises:
      ValueError: If the game ID is invalid (not between 1 and 3).
    """

    game_result = False
    if game_value == 1:
        game_result = memoryGame_play(difficulty_value)
    elif game_value == 2:
        game_result = GuessGame_play(difficulty_value)
    elif game_value == 3:
        game_result = CurrencyRouletteGame_play(difficulty_value)
    else:
        raise ValueError("Incorrect game value (should be a value between 1 and 3)")

    if game_result:
        print(Colors.PURPLE + f"You won the `{GAME_NAME.get(game_value)}`" + Colors.END)
    else:
        print(Colors.PURPLE + f"You lost the `{GAME_NAME.get(game_value)}`!!! :(" + Colors.END)

    return game_result


def welcome(name) -> str:
    return ("Hello {} and welcome to the World of Games (WoG).\n"
            "Here you can find many cool games to play.").format(name)


def present_games() -> None:
    # Game descriptions and available options
    game_descriptions = {
        1: "Memory Game - a sequence of numbers will appear for 1 second  and you have to guess it back",
        2: "Guess Game - guess a number and see if you can choose like the computer",
        3: "Currency Roulette - try and guess the value of a random amount of USD in ILS",
    }

    # Present game options and choices
    print("Choose a game:")
    for game_id, description in game_descriptions.items():
        print(f"{game_id}: {description}")


def load_game() -> None:
    """
    Prompts the user to choose a game and difficulty level, and starts the selected game.

    Returns:
      None
    """
    present_games()

    user_game_choose_number = None  # Set default value

    # Validate and get user's game choice
    while True:
        user_game_choose = input(Colors.GREEN + "Please choose a game to play (1-3): " + Colors.END)
        if Utils.is_valid_integer(user_game_choose):
            user_game_choose_number = int(user_game_choose)
            if user_game_choose_number not in range(1, 4):
                print(Colors.RED + "Invalid option chosen, you should choose 1 to 3" + Colors.END)
                continue
            else:
                break
        else:
            print(Colors.RED + "Invalid option chosen, you should choose 1 to 3" + Colors.END)
            continue

    print(f"You chose to play `{GAME_NAME.get(user_game_choose_number)}`")
    # Validate and get difficulty level
    while True:
        user_level_choose = input(Colors.GREEN + "Please choose game difficulty from 1 to 5: " + Colors.END)
        if Utils.is_valid_integer(user_level_choose):
            user_level_choose_number = int(user_level_choose)
            if user_level_choose_number not in range(1, 6):
                print(Colors.RED + "Invalid option chosen, you should choose 1 to 5" + Colors.END)
            else:
                break
        else:
            print(Colors.RED + "Invalid option chosen, you should choose 1 to 5" + Colors.END)

    # Start the chosen game with selected difficulty
    play_game_based_on_user_choice(user_game_choose_number, user_level_choose_number)


if __name__ == '__main__':
    print(welcome("Maxim"))
    load_game()
