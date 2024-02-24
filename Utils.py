import random
import time
import platform

from Colors import *
from typing import Union


HOST = '0.0.0.0'
PORT = 8777
SCORE_FILE_NAME = 'Scores.txt'
BAD_RETURN_CODE = "ERROR"


def is_valid_integer(s):
    if s.isdigit():
        return True
    elif s[0] == '-' and s[1:].isdigit():
        return True
    return False


def print_colored_message(message: str, color: str) -> None:
    """Prints a message in a specified color, handling invalid color input."""

    # Validate the color input
    if hasattr(Colors, color):
        color_code = getattr(Colors, color)  # Get the color code from the Colors class
        print(color_code + message + Colors.END)  # Print the colored message
    else:
        raise ValueError(f"Invalid color: '{color}'. Please choose from valid colors: {', '.join(Colors.__dict__.keys())}")


def screen_cleaner() -> None:
    """Clears the screen depending on the operating system.

    This function uses platform-independent methods to clear the screen.

    Args:
        None

    Returns:
        None
    """

    if platform.system() == "Windows":
        print("\033c", end="")  # ANSI escape code for clear screen on Windows
    else:
        print("\x1b[2J\x1b[H", end="")  # ANSI escape code for clear screen on Unix-like systems


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


if __name__ == '__main__':
    # Example usage
    print_colored_message("This is a red message", "RED")  # Prints in red
    print_colored_message("This is a blue message", "BLUE")  # Prints in blue
    print_colored_message("This is an invalid color", "INVALID_COLOR")  # Raises ValueError