from Utils import SCORE_FILE_NAME, is_valid_integer, print_colored_message
from Colors import *
import os.path


def add_score(difficulty) -> None:
    """
    Reads a score file, if file exists then read a score number from it.
    If file doesn't exist then create a new one and write the score to it.
    Adds a score based on the provided difficulty level:  points_of_winning = (difficulty * 3) + 5

    Args:
       difficulty (int): The difficulty level, must be a positive integer.

    Raises:
       ValueError: If the difficulty level is not a positive integer.
    """
    if not isinstance(difficulty, int) or difficulty < 1:
        raise ValueError(Colors.RED + "\"difficulty\" must be a valid integer greater than or equal to 1." + Colors.END)

    points_of_winning = (difficulty * 3) + 5
    score = 0

    try:
        # if score file exist, open it for read and get the current score from it.
        if os.path.exists(SCORE_FILE_NAME):
            with open(SCORE_FILE_NAME, mode="r+") as scores_file:
                line = scores_file.read()
                if is_valid_integer(line):
                    score = int(line)
                    print_colored_message('your previous score is %s points' % score, "GREEN")
                else:
                    print_colored_message(f"Score value stored in {SCORE_FILE_NAME} file isn't a valid number", "RED")
    except IOError:
        print_colored_message("Error reading score file.", "RED")
        return

    # Calculate the new score
    score += points_of_winning

    # open scores files for updating a new score. create the file if it doesn't exist
    try:
        with open(SCORE_FILE_NAME, mode="w+") as score_file:
            print_colored_message('your new  score is %s points' % score, "GREEN")
            # save the new score to the file
            score_file.write(str(score))
    except IOError:
        print_colored_message("Error writing score file.", "RED")


if __name__ == '__main__':
    add_score(1)
