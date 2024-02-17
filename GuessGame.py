from Colors import *
import Utils


def generate_number(difficulty) -> int:
    """
      Generates a random integer between 1 and the specified "difficulty" (inclusive).

      Args:
        difficulty: The upper bound for the random number (inclusive).

      Returns:
        A random integer between 1 and the "difficulty".

      Raises:
        ValueError: If the "difficulty" is not a valid integer or is less than 1.
      """
    if not isinstance(difficulty, int) or difficulty < 1:
        raise ValueError(Colors.RED + "\"difficulty\" must be a valid integer greater than or equal to 1." + Colors.END)

    return Utils.get_random_int_between_two_numbers(1, difficulty)


def get_guess_from_user(difficulty) -> int:
    """
    Prompt user for a number between 1 to "difficulty" and return the number

    Args:
        difficulty: The upper bound number for user prompt (inclusive).

    Raises:
        ValueError: If the "difficulty" is not a valid integer or is less than 1.

    Returns:
        Valid integer number between 1 and "difficulty"
    """
    if not isinstance(difficulty, int) or difficulty < 1:
        raise ValueError(Colors.RED + "\"difficulty\" must be a valid integer greater than or equal to 1." + Colors.END)

    while True:
        user_input = input(f"Please type a valid number of your guess, between 1 and {difficulty}: ")
        if Utils.is_valid_integer(user_input):
            user_input_num = int(user_input)
            if user_input_num not in range(1, difficulty + 1):
                print(
                    Colors.RED + f"Invalid number chosen, you should chose a valid number between 1 and {difficulty}" + Colors.END)
            else:
                break

    return user_input_num


def compare_results(user_selected_number, secret_number) -> bool:
    """
    Compares two integer numbers and returns True if they are equal, False otherwise.

    Args:
    user_selected_number: integer number selected by the user.
    secret_number: random integer number.

    Returns:
    True if "user_selected_number" and "secret_number" are equal, False otherwise.
    """
    if user_selected_number == secret_number:
        print(Colors.GREEN + "Correct guess!" + Colors.END)
    else:
        print(Colors.LIGHT_RED + "Incorrect guess!" + Colors.END)

    return user_selected_number == secret_number


def play(difficulty) -> bool:
    print(Colors.YELLOW + f"Guess Game (difficulty: {difficulty})\n==============================" + Colors.END)

    user_selected_num = get_guess_from_user(difficulty)
    secret_num = generate_number(difficulty)
    return compare_results(user_selected_num, secret_num)
