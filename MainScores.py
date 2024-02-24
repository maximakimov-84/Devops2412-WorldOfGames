from flask import Flask
from Colors import *

import Utils

app = Flask(__name__)


@app.route('/')
def score_server() -> str:
    """
    Reads the current score from a file and returns the HTML code to display it.

    This function opens the score file specified by `Utils.SCORE_FILE_NAME`,
    reads the first line (assuming the score is stored on the first line),
    and returns the HTML code to display the score within a webpage.
    In case of errors, it returns an HTML page with an error message.

    Returns:
        str: The HTML code to display the score or an error message.
    """
    try:
        # Use "with" for automatic file closing and resource management
        with open(Utils.SCORE_FILE_NAME, "r") as score_file:
            # Read only the first line (assuming single-line score storage)
            score = score_file.readline().strip()  # Remove trailing newline character
        # Construct HTML with f-strings for better readability
        return f"""
            <html>
                <head>
                    <title>Scores Game</title>
                </head>
                <body>
                    <h1>The score is <div id="score">{score}</div></h1>
                </body>
            </html>
            """
    except FileNotFoundError:
        # Handle specific error for missing file and provide a clearer message
        return f"""
                <html>
                    <head>
                        <title>Scores Game</title>
                    </head>
                    <body>
                        <h1><div id="score" style="color:red">Error: Score file not found.</div></h1>
                    </body>
                </html>
                """
    except BaseException as e:  # Catch other potential exceptions
        # Log the error for better troubleshooting and provide a generic message
        Utils.print_colored_message(f"Error reading score file: {e}", "RED")
        return f"""
            <html>
                <head>
                    <title>Scores Game</title>
                </head>
                <body>
                    <h1><div id="score" style="color:red">An error occurred.</br>""" + Utils.BAD_RETURN_CODE + str(e) + """</div></h1>
                </body>
            </html>
            """


if __name__ == '__main__':
    app.run(host=Utils.HOST, debug=False, threaded=True, port=Utils.PORT)
