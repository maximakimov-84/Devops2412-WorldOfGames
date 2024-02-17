from Colors import *
import requests
import Utils

CURRENCY_SOURCE = "usd"
CURRENCY_TARGET = "ils"


def get_random_num() -> int:
    """
      Generates a random integer between 1 and 100 (inclusive).

      Returns:
        int: A random integer between 1 and 100.

      Raises:
        ImportError: If the `Utils` module is not imported or not found.
        AttributeError: If the `get_random_int_between_two_numbers` function is not defined in the `Utils` module.
      """
    return Utils.get_random_int_between_two_numbers(1, 100)


def get_money_interval(difficulty, total_value_of_money) -> tuple[int, int]:
    """
      Calculates a money interval based on difficulty and total value, considering an external currency conversion.

      Args:
          difficulty (int): The difficulty level, determining the range around the total value. Must be an integer greater than or equal to 1.
          total_value_of_money (int): The total value of money used as the base for the interval. Must be a positive integer.

      Returns:
          tuple[int, int]: A tuple representing the lower and upper bounds of the money interval.

      Raises:
          ValueError:
              - If `difficulty` is not a valid integer greater than or equal to 1.
              - If `total_value_of_money` is not a positive integer.
              - If a valid currency rate isn't retrieved from the API.
    """

    # Validate input types and values
    if not isinstance(difficulty, int) or difficulty < 1:
        raise ValueError(Colors.RED + "\"difficulty\" must be a valid integer greater than or equal to 1." + Colors.END)

    if not isinstance(total_value_of_money, int):
        raise ValueError(Colors.RED + "\"total_value_of_money\" must be a valid integer greater than 0" + Colors.END)

    currency_rate = None

    # Fetch currency conversion rate
    try:
        response = requests.get(
            f"https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/{CURRENCY_SOURCE}/{CURRENCY_TARGET}.json")
        if response.status_code == 200:
            result_dic = response.json()
            currency_rate = round(result_dic.get(CURRENCY_TARGET), 0)
    except (requests.exceptions.RequestException, KeyError) as e:
        raise ValueError(f"Couldn't retrieve currency rate: {e}") from e

    if currency_rate is None:
        raise ValueError(Colors.RED + "didn't received a valid currency rate from the API" + Colors.END)

    # Calculate and return the money interval
    return total_value_of_money - (currency_rate - difficulty), total_value_of_money + (currency_rate - difficulty)


def get_guess_from_user():
    """
      Repeatedly prompts the user for a valid integer guess until a valid input is received.

      Returns:
          int: The user's valid integer guess.
    """
    while True:
        user_input = input("Please type your guess for a value to a given amount of USD (must be integer number): ")
        if Utils.is_valid_integer(user_input):
            try:
                user_input_num = int(user_input)
                return user_input_num  # Return immediately upon valid input
            except ValueError:
                print(Colors.RED + "Invalid integer number" + Colors.END)  # Handle potential conversion errors
        else:
            print(Colors.RED + "Invalid integer number" + Colors.END)


def play(difficulty) -> bool:
    """
      Runs a single round of a guessing game, determining user success based on the chosen difficulty.

      Args:
          difficulty (int): The difficulty level of the game, determining the range of the target value. Must be an integer greater than or equal to 1.

      Returns:
          bool: True if the user's guess falls within the target interval, False otherwise.

      Raises:
          ValueError: If `difficulty` is not a valid integer greater than or equal to 1.
    """
    print(Colors.YELLOW + f"Currency Roulette Game (difficulty: {difficulty})\n==============================" + Colors.END)

    # Generate random total value and calculate money interval
    random_total_value_of_money = get_random_num()
    interval = get_money_interval(difficulty, random_total_value_of_money)
    # print(f"interval: {interval}")
    # Prompt user for a guess and validate input
    user_guess = get_guess_from_user()

    # Check if the guess falls within the interval
    lower_bound_interval, upper_bound_interval = interval
    if lower_bound_interval <= user_guess <= upper_bound_interval:
        return True
    else:
        return False


if __name__ == '__main__':
    play_result = play(1)
    if play_result:
        print("Correct answer")
    else:
        print("Not a correct answer")