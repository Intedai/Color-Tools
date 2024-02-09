import tkinter as tk
from colorsys import rgb_to_hsv, hsv_to_rgb
import random
import os
from typing import NoReturn

from colorpicker import start_capture
from settings import *
from utils import *


SOFTWARE_WIDTH = 500
SOFTWARE_HEIGHT = 845
SOFTWARE_TITLE = "Color Tools"

LAUNCH_ERROR_MSG = "\n\nPress <ENTER> to quit ..."


class Software():

    def __init__(self) -> None:

        self.root = tk.Tk()
        self.root.title(SOFTWARE_TITLE)
        self.root.geometry(f"{SOFTWARE_WIDTH}x{SOFTWARE_HEIGHT}")
        self.root.minsize(SOFTWARE_WIDTH, SOFTWARE_HEIGHT)
        self.root.config(bg=Colors.PRIMARY_COLOR)

        # If icon.ico exists set it as the gui's icon
        try:
            self.root.iconbitmap(os.path.join(
                ProjectPaths.ASSETS_FOLDER, "icon.ico"))
        except Exception as e:
            print(e)

        # Load logo and all function icon images
        self.logo_img = tk.PhotoImage(file=os.path.join(
            ProjectPaths.ASSETS_FOLDER, "LOGO.png"))
        self.settings_img = tk.PhotoImage(file=os.path.join(
            ProjectPaths.ASSETS_FOLDER, "SETTINGS.png"))
        self.copy_hex_img = tk.PhotoImage(file=os.path.join(
            ProjectPaths.ASSETS_FOLDER, "COPY_HEX.png"))
        self.copy_rgb_img = tk.PhotoImage(file=os.path.join(
            ProjectPaths.ASSETS_FOLDER, "COPY_RGB.png"))
        self.copy_hsv_img = tk.PhotoImage(file=os.path.join(
            ProjectPaths.ASSETS_FOLDER, "COPY_HSV.png"))
        self.color_picker_img = tk.PhotoImage(file=os.path.join(
            ProjectPaths.ASSETS_FOLDER, "COLOR_PICKER.png"))
        self.random_img = tk.PhotoImage(file=os.path.join(
            ProjectPaths.ASSETS_FOLDER, "RANDOM.png"))

        # Color Tools logo in label
        self.user_label = tk.Label(
            self.root, image=self.logo_img, fg=Colors.TEXT_COLOR, bg=Colors.LIGHT_COLOR, width=1000)
        self.user_label.pack(pady=0, fill=tk.X)

        # Frame that will contain all function buttons
        self.button_frame = tk.Frame(self.root, bg=Colors.MEDIUM_COLOR)
        self.button_frame.pack(pady=0, fill=tk.X)

        # Create function buttons and put them in the button frame
        self.settings_button = tk.Button(self.button_frame, image=self.settings_img, command=self.open_settings,
                                         bg=Colors.MEDIUM_COLOR, activebackground=Colors.ACTIVE, bd=0, padx=10, pady=0)
        self.settings_button.grid(row=0, column=0, padx=0)

        self.hex_button = tk.Button(self.button_frame, image=self.copy_hex_img, command=self.copy_hex_to_clipboard,
                                    bg=Colors.MEDIUM_COLOR, activebackground=Colors.ACTIVE, bd=0, padx=10, pady=0)
        self.hex_button.grid(row=0, column=1, padx=0)

        self.rgb_button = tk.Button(self.button_frame, image=self.copy_rgb_img, command=self.copy_rgb_to_clipboard,
                                    bg=Colors.MEDIUM_COLOR, activebackground=Colors.ACTIVE, bd=0, padx=10, pady=0)
        self.rgb_button.grid(row=0, column=2, padx=0)

        self.hsv_button = tk.Button(self.button_frame, image=self.copy_hsv_img, command=self.copy_hsv_to_clipboard,
                                    bg=Colors.MEDIUM_COLOR, activebackground=Colors.ACTIVE, bd=0, padx=10, pady=0)
        self.hsv_button.grid(row=0, column=3, padx=0)

        self.colorpicker_button = tk.Button(self.button_frame, image=self.color_picker_img, command=self.capture_picked_color,
                                            bg=Colors.MEDIUM_COLOR, activebackground=Colors.ACTIVE, bd=0, padx=10, pady=0)
        self.colorpicker_button.grid(row=0, column=4, padx=0)

        self.random_button = tk.Button(self.button_frame, image=self.random_img, command=self.random_color,
                                       bg=Colors.MEDIUM_COLOR, activebackground=Colors.ACTIVE, bd=0, padx=10, pady=0)
        self.random_button.grid(row=0, column=5, padx=0)

        # Hex value displayed at the top
        self.hex_input = tk.Entry(self.root, font=GuiFonts.font, fg=Colors.TEXT_COLOR,
                                  bg=Colors.LIGHT_COLOR, bd=0, insertbackground=Colors.TEXT_COLOR, justify='center')
        self.hex_input.pack(fill=tk.X, pady=(20, 0))
        self.hex_input.insert(0, "#000000")  # Default value

        # When ENTER is pressed update color
        # Bind the Enter key
        self.hex_input.bind("<Return>", self.update_from_hex_input)

        self.color_preview = tk.Frame(
            self.root, width=300, height=100, bg=rgb_to_hex(0, 0, 0))
        self.color_preview.pack(pady=(20, 0))

        # RGB title
        self.rgb_label = tk.Label(
            self.root, text="RGB:", font=GuiFonts.font, fg=Colors.TEXT_COLOR, bg=Colors.LIGHT_COLOR)
        self.rgb_label.pack(fill=tk.X, pady=(20, 0))

        # Variables that hold RGB values from sliders
        self.red_var, self.green_var, self.blue_var = tk.IntVar(), tk.IntVar(), tk.IntVar()

        # RGB Sliders
        self.red = tk.Scale(self.root, command=self.RGB_color_change, variable=self.red_var, font=GuiFonts.font, from_=0, to=255, background=Colors.RED, foreground=Colors.TEXT_COLOR,
                            sliderrelief='flat', troughcolor=Colors.MEDIUM_COLOR, highlightthickness=0, activebackground=Colors.ACTIVE, orient="horizontal", length=300, bd=5)
        self.red.set(0)
        self.red.pack(pady=(20, 10))

        self.green = tk.Scale(self.root, command=self.RGB_color_change, variable=self.green_var, font=GuiFonts.font, from_=0, to=255, background=Colors.GREEN, foreground=Colors.TEXT_COLOR,
                              sliderrelief='flat', troughcolor=Colors.MEDIUM_COLOR, highlightthickness=0, activebackground=Colors.ACTIVE, orient="horizontal", length=300, bd=5)
        self.green.set(0)
        self.green.pack(pady=(0, 10))

        self.blue = tk.Scale(self.root, command=self.RGB_color_change, variable=self.blue_var, font=GuiFonts.font, from_=0, to=255, background=Colors.BLUE, foreground=Colors.TEXT_COLOR,
                             sliderrelief='flat', troughcolor=Colors.MEDIUM_COLOR, highlightthickness=0, activebackground=Colors.ACTIVE, orient="horizontal", length=300, bd=5)
        self.blue.set(0)
        self.blue.pack(pady=(0, 8))

        # HSV title with light background
        self.hsv_label = tk.Label(self.root, text="HSV:", font=GuiFonts.font,
                                  fg=Colors.TEXT_COLOR, bg=Colors.LIGHT_COLOR, width=1000)
        self.hsv_label.pack(pady=(20, 0))

        # Variables that hold HSV values from sliders
        self.hsv0_var, self.hsv1_var, self.hsv2_var = tk.IntVar(), tk.IntVar(), tk.IntVar()

        # HSV Sliders
        self.hsv0 = tk.Scale(self.root, command=self.HSV_color_change, variable=self.hsv0_var, font=GuiFonts.font, from_=0, to=360, background=Colors.HSV_SLIDE, foreground=Colors.TEXT_COLOR,
                             sliderrelief='flat', troughcolor=Colors.MEDIUM_COLOR, highlightthickness=0, activebackground=Colors.ACTIVE, orient="horizontal", length=300, bd=5)
        self.hsv0.set(0)
        self.hsv0.pack(pady=(20, 10))

        self.hsv1 = tk.Scale(self.root, command=self.HSV_color_change, variable=self.hsv1_var, font=GuiFonts.font, from_=0, to=100, background=Colors.HSV_SLIDE, foreground=Colors.TEXT_COLOR,
                             sliderrelief='flat', troughcolor=Colors.MEDIUM_COLOR, highlightthickness=0, activebackground=Colors.ACTIVE, orient="horizontal", length=300, bd=5)
        self.hsv1.set(0)
        self.hsv1.pack(pady=(0, 10))

        self.hsv2 = tk.Scale(self.root, command=self.HSV_color_change, variable=self.hsv2_var, font=GuiFonts.font, from_=0, to=100, background=Colors.HSV_SLIDE, foreground=Colors.TEXT_COLOR,
                             sliderrelief='flat', troughcolor=Colors.MEDIUM_COLOR, highlightthickness=0, activebackground=Colors.ACTIVE, orient="horizontal", length=300, bd=5)
        self.hsv2.set(0)
        self.hsv2.pack(pady=(0, 8))

        tk.mainloop()

    def RGB_color_change(self, value: any = None) -> NoReturn:
        """
        changes the preview to the current color and moves the HSV sliders and the HEX value
        according to the RGB sliders
        gets executed when one of the RGB sliders move.

        :param value: required by tkinter, is not used in the code    
        """

        rgb = (self.red_var.get(), self.green_var.get(), self.blue_var.get())

        # Converts RGB to the accurate messurements for the rgb_to_hsv func
        hsv = rgb_to_hsv(*tuple(map(lambda x: x/255, rgb)))
        hsv = (hsv[0]*3.6, hsv[1], hsv[2])

        # Converts the hsv to int and multiplies by hundred which is how HSV is usually viewed
        hsv = tuple(map(lambda x: int(x*100), hsv))

        # moves the hsv sliders
        self.hsv0_var.set(hsv[0])
        self.hsv1_var.set(hsv[1])
        self.hsv2_var.set(hsv[2])

        # changes the preview and the hex value
        current_color = rgb_to_hex(*rgb)

        self.color_preview.configure(bg=current_color)

        self.hex_input.delete(0, tk.END)  # Remove the current text
        self.hex_input.insert(0, current_color)  # Insert the new hex color

    def HSV_color_change(self, value: any = None) -> NoReturn:
        """
        changes the preview to the current color and moves the RGB sliders and the HEX value
        according to the HSV sliders
        gets executed when one of the HSV sliders move.

        :param value: required by tkinter, is not used in the code    
        """

        hsv = (self.hsv0_var.get(), self.hsv1_var.get(), self.hsv2_var.get())

        # converts it to the accurate messurements for the hsv_to_rgb func
        hsv = (hsv[0]/360, hsv[1]/100, hsv[2]/100)

        # converts the hsv to int and multiplies by 255 because the values are from 0.0 to 1.0
        rgb = tuple(map(lambda x: int(x*255), hsv_to_rgb(*hsv)))

        # moves the sliders
        self.red_var.set(rgb[0])
        self.green_var.set(rgb[1])
        self.blue_var.set(rgb[2])

        # changes the preview and the hex value
        hex = rgb_to_hex(*rgb)

        self.color_preview.configure(bg=hex)

        self.hex_input.delete(0, tk.END)  # Remove the current text
        self.hex_input.insert(0, hex)  # Insert the new hex color

    def update_from_hex_input(self, value: any = None) -> NoReturn:
        """
        Update color preview and sliders based on the HEX value entered in the HEX entry.

        :param value: required by tkinter, is not used in the code
        """
        hex_color = self.hex_input.get()
        try:
            # Validate and convert hex to RGB
            r, g, b = [int(hex_color[i:i+2], 16) for i in (1, 3, 5)]
            self.red_var.set(r)
            self.green_var.set(g)
            self.blue_var.set(b)
            self.RGB_color_change(None)  # Update color preview and HSV sliders
        finally:
            # Unfocus the Entry widget by setting focus back to the root window
            self.root.focus_set()

    def copy_hex_to_clipboard(self):
        """
        Copy current HEX using the copy format
        """

        self.update_copy_formats()
        rgb = (self.red_var.get(), self.green_var.get(), self.blue_var.get())

        # Doesn't use rgb to hex function because of format
        HEX_R = "{0:02x}".format(rgb[0])
        HEX_G = "{0:02x}".format(rgb[1])
        HEX_B = "{0:02x}".format(rgb[1])

        # If upper option is on in settings upper all variables
        if self.hex_upper:
            HEX_R = HEX_R.upper()
            HEX_G = HEX_G.upper()
            HEX_B = HEX_B.upper()

        hex_text = self.hex_copy_format.format(HEX_R, HEX_G, HEX_B)
        self.root.clipboard_clear()
        self.root.clipboard_append(hex_text)
        self.root.update()

    def copy_rgb_to_clipboard(self):
        """
        Copy current RGB using the copy format
        """

        self.update_copy_formats()
        rgb = (self.red_var.get(), self.green_var.get(), self.blue_var.get())
        rgb_text = self.rgb_copy_format.format(rgb[0], rgb[1], rgb[2])
        self.root.clipboard_clear()
        self.root.clipboard_append(rgb_text)
        self.root.update()

    def copy_hsv_to_clipboard(self):
        """
        Copy current HSV using the copy format
        """

        self.update_copy_formats()
        hsv = (self.hsv0_var.get(), self.hsv1_var.get(), self.hsv2_var.get())
        hsv_text = self.hsv_copy_format.format(hsv[0], hsv[1], hsv[2])
        self.root.clipboard_clear()
        self.root.clipboard_append(hsv_text)
        self.root.update()

    def set_color(self, hex):
        """
        Set current color

        :param hex: HEX color representation
        """

        # Manipulate update_from_hex_input function to set color
        self.hex_input.delete(0, tk.END)
        self.hex_input.insert(0, hex)
        self.update_from_hex_input()

    def random_color(self):
        """
        Set random color as current color
        """

        R = random.randint(0, 255)
        G = random.randint(0, 255)
        B = random.randint(0, 255)
        random_hex = rgb_to_hex(R, G, B)

        self.set_color(random_hex)

    def capture_picked_color(self):
        """
        Use color picker and set current color to the color at the mouse position
        when the color picker key is pressed
        """

        start_capture(self.set_color)

    def open_settings(self):
        """
        Launch settings window
        """

        # Launch Settings class with root as parent
        Settings(self.root)

    def update_copy_formats(self):
        """
        Update copy formats by setting the variables to the current values
        in the settings json file
        """

        with open(ProjectPaths.SETTINGS_PATH, 'r') as file:
            data = json.load(file)
            self.hex_copy_format = data[OptionKeys.HEX_COPY_KEY]
            self.rgb_copy_format = data[OptionKeys.RGB_COPY_KEY]
            self.hsv_copy_format = data[OptionKeys.HSV_COPY_KEY]
            self.hex_upper = data[OptionKeys.HEX_UPPER]


if __name__ == '__main__':
    try:
        Software()
    except Exception as e:
        print(e)
        input(LAUNCH_ERROR_MSG)
