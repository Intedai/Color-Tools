from PIL import ImageGrab
from pynput.keyboard import Listener as KeyboardListener
from pynput.mouse import Controller as MouseController
from typing import Callable, NoReturn
from pynput.keyboard import Key
import threading
import json
from utils import *

# Mouse controller to retrieve mouse position
mouse = MouseController()


def get_color_picker_key() -> str:
    """
    Get current color picker key from settings json
    :returns: current color picker key
    """

    with open(ProjectPaths.SETTINGS_PATH, 'r') as file:
        data = json.load(file)
        return data[OptionKeys.COLOR_PICKER_KEY]


def get_color(x: int, y: int) -> str:
    """
    Get color of pixel in the current position of the cursor
    :param x: the x-coordinate of the current position
    :param y: the y-coordinate of the current position
    :returns: color of the pixel in current position in the HEX color representation 
    """

    # Bounding box of current pixel
    bbox = (x, y, x+1, y+1)

    # Screenshot single pixel
    pixel_screenshot = ImageGrab.grab(bbox)

    # Convert rgb to hex from pixel and return
    return rgb_to_hex(*(pixel_screenshot.getpixel((0, 0))))


def start_capture(callback: Callable) -> NoReturn:
    """
    Waits until the color picker key is pressed and
    executes a callback with color as an arguement

    :param callback: Callable to execute with color as it's arguement
    """

    # Function that will execute when key is pressed, defined inside so it will recognize the Callable
    def on_press(key: Key) -> bool:
        try:
            # Get key from settings every time so key will always be up to date
            if key.char == get_color_picker_key():

                x, y = mouse.position
                color = get_color(x, y)
                callback(color)

                # Stop the listener
                return False
        except AttributeError:
            pass

    # thread to not interrupt tkinter mainloop
    t = threading.Thread(
        target=lambda: KeyboardListener(on_press=on_press).start())

    # Daemon thread so it exits when software is closed
    t.daemon = True

    t.start()
