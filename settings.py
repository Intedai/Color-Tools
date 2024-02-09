import tkinter as tk
import json
from tkinter import messagebox
import os

from utils import *

SETTINGS_WIDTH = 500
SETTINGS_HEIGHT = 420
SETTINGS_TITLE = "Color Tools"


class Settings():
    def __init__(self, parent) -> None:

        self.root = tk.Toplevel(parent)
        self.root.title(SETTINGS_TITLE)
        self.root.geometry(f"{SETTINGS_WIDTH}x{SETTINGS_HEIGHT}")
        self.root.minsize(SETTINGS_WIDTH, SETTINGS_HEIGHT)
        self.root.config(bg=Colors.PRIMARY_COLOR)

        # If icon.ico exists set it as the gui's icon
        try:
            self.root.iconbitmap(os.path.join(
                ProjectPaths.ASSETS_FOLDER, "icon.ico"))
        except Exception as e:
            print(e)

        # Load settings logo, apply and default icon images
        self.settings_logo_img = tk.PhotoImage(file=os.path.join(
            ProjectPaths.ASSETS_FOLDER, "SETTINGS_LOGO.png"))
        self.apply_img = tk.PhotoImage(file=os.path.join(
            ProjectPaths.ASSETS_FOLDER, "APPLY.png"))
        self.reset_img = tk.PhotoImage(file=os.path.join(
            ProjectPaths.ASSETS_FOLDER, "RESET.png"))

        # Settings logo in label
        self.user_label = tk.Label(self.root, image=self.settings_logo_img,
                                   fg=Colors.TEXT_COLOR, bg=Colors.LIGHT_COLOR, width=1000)
        self.user_label.pack(pady=0, fill=tk.X)

        # Frame for each option
        self.hex_copy_frame = tk.Frame(self.root, bg=Colors.LIGHT_COLOR)
        self.hex_copy_frame.pack(pady=(30, 10))

        self.rgb_copy_frame = tk.Frame(self.root, bg=Colors.LIGHT_COLOR)
        self.rgb_copy_frame.pack(pady=10)

        self.hsv_copy_frame = tk.Frame(self.root, bg=Colors.LIGHT_COLOR)
        self.hsv_copy_frame.pack(pady=10)

        self.color_picker_frame = tk.Frame(self.root, bg=Colors.LIGHT_COLOR)
        self.color_picker_frame.pack(pady=(10, 30))

        # Option text and input in each frame, using an helper function
        self.hex_copy_entry = self.create_text_input(
            self.hex_copy_frame, "Copy HEX Format: ")
        self.upper = tk.IntVar()
        self.hex_upper = tk.Checkbutton(self.hex_copy_frame, variable=self.upper, text='Uppercase for HEX characters', onvalue=1, offvalue=0, background=Colors.LIGHT_COLOR,
                                        foreground=Colors.TEXT_COLOR, selectcolor=Colors.MEDIUM_COLOR, activebackground=Colors.ACTIVE, activeforeground=Colors.PRIMARY_COLOR, font=GuiFonts.font, relief="flat", bd=0)
        self.hex_upper.pack()

        self.rgb_copy_entry = self.create_text_input(
            self.rgb_copy_frame, "Copy RGB Format: ")
        self.hsv_copy_entry = self.create_text_input(
            self.hsv_copy_frame, "Copy HSV Format: ")
        self.copy_key_entry = self.create_text_input(
            self.color_picker_frame, "Color Picker Key: ")
        # Add validation to color picker key so it will be 1 character which is alphanumerical
        self.copy_key_entry.config(validate="key", validatecommand=(
            self.root.register(validate_key), '%P'))

        # Load current values to option entries
        self.put_json_in_entry()

        # Button frames where apply and default will be in
        self.buttons_frame = tk.Frame(self.root, bg=Colors.LIGHT_COLOR)
        self.buttons_frame.pack(pady=(0, 10))

        # Apply and default buttons
        self.apply_button = tk.Button(self.buttons_frame, image=self.apply_img, relief="flat",
                                      bd=0, background=Colors.LIGHT_COLOR, activebackground=Colors.ACTIVE, command=self.save)
        self.apply_button.pack(pady=0, side="left")

        self.reset_button = tk.Button(self.buttons_frame, image=self.reset_img, relief="flat",
                                      bd=0, background=Colors.LIGHT_COLOR, activebackground=Colors.ACTIVE, command=self.reset)
        self.reset_button.pack(pady=0, side="left")

        self.root.mainloop()

    def create_text_input(self, parent_frame, label_text):
        """
        Helper function to create a text and input in the same frame

        :param parent_frame: frame to put the text and input in
        :param label_text: text near input
        """

        input_frame = tk.Frame(parent_frame, bg=Colors.LIGHT_COLOR)
        input_frame.pack(pady=5, padx=10, fill=tk.X)

        instruction_label = tk.Label(
            input_frame, text=label_text, font=GuiFonts.font, fg=Colors.TEXT_COLOR, bg=Colors.LIGHT_COLOR)
        instruction_label.pack(side="left")

        text_entry = tk.Entry(input_frame, font=GuiFonts.font, fg=Colors.ACTIVE,
                              bg=Colors.MEDIUM_COLOR, bd=0, justify='center')
        text_entry.pack(side="left")
        return text_entry

    def save(self):
        """
        Save options after pressing apply
        """

        # Make sure user wants to apply the settings
        result = messagebox.askyesno(
            "APPLY SETTINGS", "Are you sure you want to apply the current settings?", parent=self.root)
        # Focus window after question
        self.root.focus_force()

        # If user said NO quit function
        if not result:
            return

        # Craft new json for settings
        formats = {
            OptionKeys.HEX_COPY_KEY: self.hex_copy_entry.get(),
            OptionKeys.RGB_COPY_KEY: self.rgb_copy_entry.get(),
            OptionKeys.HSV_COPY_KEY: self.hsv_copy_entry.get(),
            OptionKeys.COLOR_PICKER_KEY: self.copy_key_entry.get(),
            OptionKeys.HEX_UPPER: bool(self.upper.get())
        }

        # Flag to see if the format is valid
        fmt_is_valid = True

        keys = list(formats.keys())
        i = 0
        for format in list(formats.values())[:3]:
            if not validate_copy_format(format):
                messagebox.showerror("ERROR", f"Format {keys[i]}: \"{
                                     format}\" is not valid", parent=self.root)
                # If format is bad set flag to false
                fmt_is_valid = False
            i += 1

        # If one of the formats is not valid quit function
        if not fmt_is_valid:
            return

        # Dump dict to the the settings json
        with open(ProjectPaths.SETTINGS_PATH, "w") as json_file:
            json.dump(formats, json_file)

    def reset(self):
        """
        reset the settings, settings will be restored to default
        """

        # Make sure user wants to reset the settings
        if messagebox.askyesno("DEFAULT SETTINGS", "Are you sure you want to apply the default settings?", parent=self.root):
            copy_file(ProjectPaths.DEFAULT_SETTINGS_PATH,
                      ProjectPaths.SETTINGS_PATH)

            # Put default values inside entries
            self.put_json_in_entry()  # False VSCODE flag, code is infact reachable

    def put_json_in_entry(self):
        """
        Take text from settings and put them in the entries
        """

        with open(ProjectPaths.SETTINGS_PATH, 'r') as file:
            data = json.load(file)
            self.hex_copy_entry.delete(0, tk.END)
            self.hex_copy_entry.insert(0, data[OptionKeys.HEX_COPY_KEY])
            self.rgb_copy_entry.delete(0, tk.END)
            self.rgb_copy_entry.insert(0, data[OptionKeys.RGB_COPY_KEY])
            self.hsv_copy_entry.delete(0, tk.END)
            self.hsv_copy_entry.insert(0, data[OptionKeys.HSV_COPY_KEY])
            self.copy_key_entry.delete(0, tk.END)
            self.copy_key_entry.insert(0, data[OptionKeys.COLOR_PICKER_KEY])
            self.upper.set(int(data[OptionKeys.HEX_UPPER]))
