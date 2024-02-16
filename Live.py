from GlobalConstants import *
from Utils import *


def welcome(name) -> str:
    return ("Hello {} and welcome to the World of Games (WoG).\n"
            "Here you can find many cool games to play.").format(name)


def load_game():
    choose_game_msg = ("1. Memory Game - a sequence of numbers will appear for 1 second  and you have to guess it "
                       "back\n"
                       "2. Guess Game - guess a number and see if you can choose like the computer\n"
                       "3. Currency Roulette - try and guess the value of a random amount of USD in ILS")
    print(choose_game_msg)

    while True:
        user_game_choose = input("Please choose a game to play (1-3): ")
        if is_valid_integer(user_game_choose):
            user_game_choose_number = int(user_game_choose)
            if user_game_choose_number not in range(1, 4):
                print(COLOR_RED + "Invalid option chosen, you should choose 1 to 3" + COLOR_END)
                continue
            else:
                break
        else:
            print(COLOR_RED + "Invalid option chosen, you should choose 1 to 3" + COLOR_END)
            continue

    while True:
        user_level_choose = input("Please choose game difficulty from 1 to 5: ")
        if is_valid_integer(user_level_choose):
            user_level_choose_number = int(user_level_choose)
            if user_level_choose_number not in range(1, 6):
                print(COLOR_RED + "Invalid option chosen, you should choose 1 to 5" + COLOR_END)
            else:
                break
        else:
            print(COLOR_RED + "Invalid option chosen, you should choose 1 to 5" + COLOR_END)






