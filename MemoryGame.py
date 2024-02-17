from Colors import *
import Utils

DISPLAY_SECONDS = 0.7


def generate_sequence(difficulty) -> list:
    """
    Generate a list of random numbers between 1 and 101.
    The list length will be based on arg "difficulty".

    Args:
        difficulty: An int number

    Raises:
        ValueError: If the "difficulty" is not a valid integer or is less than 1.

    Returns:
        A list of length "difficulty" with randon numbers between 1 and 101.
    """
    if not isinstance(difficulty, int) or difficulty < 1:
        raise ValueError(Colors.RED + "\"difficulty\" must be a valid integer greater than or equal to 1." + Colors.END)

    list_of_numbers = []

    list_length = 0
    while list_length < difficulty:
        list_of_numbers.append(Utils.get_random_int_between_two_numbers(1, 101))
        list_length += 1

    return list_of_numbers


def get_list_from_user(difficulty) -> list:
    """
    Prompts the user to enter a list of integers based on the specified difficulty level.

    Args:
        difficulty (int): The number of integers to collect from the user. Must be an integer greater than or equal to 1.

    Returns:
        list: A list of integers entered by the user.

    Raises:
        ValueError: If the `difficulty` is not a valid integer or is less than 1.
    """
    if not isinstance(difficulty, int) or difficulty < 1:
        raise ValueError(Colors.RED + "\"difficulty\" must be a valid integer greater than or equal to 1." + Colors.END)

    list_of_numbers = []

    list_length = 0
    while list_length < difficulty:
        while True:
            user_input = input(f"Please type a number of your guess (selection: {list_length+1}): ")
            if Utils.is_valid_integer(user_input):
                user_input_num = int(user_input)
                list_of_numbers.append(user_input_num)
                break
            else:
                print(Colors.RED + "Invalid integer number" + Colors.END)

        list_length += 1

    return list_of_numbers


def is_list_equal(list1, list2) -> bool:
    """
      Compares two lists of integers and returns True if all items in the first list
      are equal to items in the second list, regardless of order.

      Args:
        list1: The first list of integers.
        list2: The second list of integers.

      Returns:
        True if all items in list1 are equal to items in list2, False otherwise.
      """

    # Check if the lists have the same length.
    if len(list1) != len(list2):
        return False

    # Sort both lists
    list1_sorted = sorted(list1)
    list2_sorted = sorted(list2)

    # Compare elements based on indices
    for i, num in enumerate(list1_sorted):
        if i >= len(list2_sorted) or num != list2_sorted[i]:
            return False
    return True


def play(difficulty) -> bool:
    """
    Plays a memory game by presenting a sequence of random numbers and prompting
    the user to recall them in the same order.

    Args:
      difficulty (int): The difficulty level of the game, determining the number
                         of random numbers to be presented. Must be an integer
                         greater than or equal to 1.

    Returns:
      bool: True if the user recalls the sequence correctly, False otherwise.

    Raises:
      ValueError: If the `difficulty` is not a valid integer or is less than 1.
    """
    print(Colors.YELLOW + f"Memory Game (difficulty: {difficulty})\n==============================" + Colors.END)
    list_of_random_numbers = generate_sequence(difficulty)
    Utils.display_info(f"Computer random numbers: {list_of_random_numbers}", DISPLAY_SECONDS)
    user_list_of_numbers = get_list_from_user(difficulty)

    return is_list_equal(list_of_random_numbers, user_list_of_numbers)
