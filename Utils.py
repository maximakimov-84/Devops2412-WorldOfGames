import random
import time

HOST = '0.0.0.0'
PORT = 8777


def is_valid_integer(s):
    if s.isdigit():
        return True
    elif s[0] == '-' and s[1:].isdigit():
        return True
    return False


def get_random_int_between_two_numbers(num1, num2) -> int:
    return random.randint(num1, num2)


def display_info(message, duration) -> None:
    """
    Displays the message, waits, then overwrites it with blank spaces.

    Args:
    message: The message to display.
    duration: The duration to display the message (in seconds).
    """
    print(message)
    time.sleep(duration)
