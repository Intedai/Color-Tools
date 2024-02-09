import os
from typing import NoReturn


class Colors():
    """
    GUI Colors (Nord theme)
    """

    PRIMARY_COLOR = "#2e3440"  # Darkest color and used for the GUI's bg
    MEDIUM_COLOR = "#3b4252"
    LIGHT_COLOR = "#434C5E"

    ACTIVE = "#88c0d0"  # When a button is clicked
    TEXT_COLOR = "#d8dee9"

    # Colors for the RGB sliders
    RED = "#bf616a"
    GREEN = "#a3be8c"
    BLUE = "#5e81ac"

    # Color for the HSV sliders
    HSV_SLIDE = "#81a1c1"


class OptionKeys():
    """
    Option keys settings.json object
    """

    HEX_COPY_KEY = "COPY_HEX"
    RGB_COPY_KEY = "COPY_RGB"
    HSV_COPY_KEY = "COPY_HSV"
    COLOR_PICKER_KEY = "COLOR_PICKER_KEY"
    HEX_UPPER = "HEX_UPPER"


class GuiFonts():
    """
    Fonts for tkinter GUI
    """

    font = ("Calibri", 15, "bold")


class ProjectPaths():
    """
    Paths of folders and files used in the project
    """

    ASSETS_FOLDER = "assets"
    SETTINGS_FOLDER = "settings"

    SETTINGS_PATH = os.path.join(SETTINGS_FOLDER, "settings.json")
    DEFAULT_SETTINGS_PATH = os.path.join(
        SETTINGS_FOLDER, "default_settings.json")


def rgb_to_hex(R: int, G: int, B: int) -> str:
    """
    Returns the HEX color representation of an RGB Color

    :param R: red
    :param G: green
    :param B: blue
    :returns: HEX color representation of RGB
    """

    return "#{0:02x}{1:02x}{2:02x}".format(R, G, B)


def validate_copy_format(fmt: str) -> bool:
    """
    Validates if a copy format (of HEX,RGB or HSV) is valid,
    the format is like a python str.format format
    VALID: must contain maximum 3 {} in format
    INVALID: more than 3 {} in format

    :param fmt: copy format
    :returns: True if the format is valid, False if it's invalid
    """

    # Let python validate by checking if it returns an error
    try:
        fmt.format(1, 1, 1)
        return True
    except:
        return False


def validate_key(P: str) -> bool:
    """
    Validates if a string is an alphanumerical with maximum one character.
    used by tkinter for entry validation

    :param P: Text to be validated in tkinter entry
    :returns: True if the format is valid, False if it's invalid
    """
    if len(P) == 0:
        # empty Entry is ok
        return True
    elif len(P) == 1 and P.isalnum():
        # Entry with 1 digit is ok
        return True
    else:
        # Anything else, reject it
        return False


def copy_file(source_file: str, destination_file: str) -> NoReturn:
    """
    Copies text from a file into another file with error checking

    :param source_file: path of the source file
    :param destination_file: path of the destination file
    """
    try:
        with open(source_file, 'r') as source:
            content = source.read()

        with open(destination_file, 'w') as destination:
            destination.write(content)
    except FileNotFoundError as e:
        print(f"File not found: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
