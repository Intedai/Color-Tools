import tkinter as tk #tkinter
from colorsys import rgb_to_hsv, hsv_to_rgb #converting rgb to hsv and vice versa

#THE COLORS ARE FROM THE NORD THEME:
#colors for the gui
PRIMARY_COLOR = "#2e3440"
LIGHT_COLOR = "#3b4252"
DARK_COLOR = "#434C5E"
ACTIVE = "#88c0d0" #When a button is clicked (active)
TEXT_COLOR = "#d8dee9"

#colors for the RGB sliders
RED = "#bf616a"
GREEN = "#a3be8c"
BLUE = "#5e81ac"

#color for the HSV sliders
HSV_SLIDE = "#81a1c1"


#function to convert rgb values to hex
rgb_to_hex = lambda r, g, b: "#{0:02x}{1:02x}{2:02x}".format(r, g, b)

#The entire software: the GUI
class Software():

    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.geometry("400x860")
        self.root.config(bg = PRIMARY_COLOR)
        self.root.title("Color Sliders")

        #if icon.ico exists it will set it as the gui's icon
        try:
            self.root.iconbitmap("icon.ico")
        except Exception as e:
            print(e) #prints to the console

        #sets minimum size to 400x860
        self.root.minsize(400, 860)

        self.user_label = tk.Label(self.root,text="Color Sliders", font=("Calibri",30,"bold"), fg=TEXT_COLOR ,bg=DARK_COLOR, width=1000)
        self.user_label.pack(pady=0)

        #hex value displayed at the top
        self.hex = tk.Label(self.root,text=rgb_to_hex(0,0,0), font=("Calibri",25,"bold"), fg=TEXT_COLOR ,bg=DARK_COLOR, width=1000)
        self.hex.pack(pady=(20,0))

        self.color_preview = tk.Frame(self.root, width=300, height=100, bg=rgb_to_hex(0,0,0))
        self.color_preview.pack(pady=(20,0))

        #RGB title with light background
        self.rgb_label = tk.Label(self.root,text="RGB:", font=("Calibri",15,"bold"), fg=TEXT_COLOR ,bg=DARK_COLOR, width=1000)
        self.rgb_label.pack(pady=(20,0))

        #variables to hold the RGB values
        self.red_var, self.green_var, self.blue_var = tk.IntVar(),tk.IntVar(),tk.IntVar()

        #red slider
        self.red = tk.Scale(self.root, command=self.RGB_color_change,variable=self.red_var ,font='Helvetica 18 bold', from_=0, to=255,background=RED,foreground=TEXT_COLOR, sliderrelief='flat', troughcolor=LIGHT_COLOR,highlightthickness=0, activebackground=ACTIVE,orient="horizontal", length=300,bd=5)
        self.red.set(0)
        self.red.pack(pady=(20,10))

        #green slider
        self.green = tk.Scale(self.root, command=self.RGB_color_change,variable=self.green_var ,font='Helvetica 18 bold', from_=0, to=255,background=GREEN,foreground=TEXT_COLOR, sliderrelief='flat', troughcolor=LIGHT_COLOR,highlightthickness=0, activebackground=ACTIVE,orient="horizontal", length=300,bd=5)
        self.green.set(0)
        self.green.pack(pady=(0,10))

        #blue slider
        self.blue = tk.Scale(self.root, command=self.RGB_color_change,variable=self.blue_var ,font='Helvetica 18 bold', from_=0, to=255,background=BLUE,foreground=TEXT_COLOR, sliderrelief='flat', troughcolor=LIGHT_COLOR,highlightthickness=0, activebackground=ACTIVE,orient="horizontal", length=300,bd=5)
        self.blue.set(0)
        self.blue.pack(pady=(0,8))


        #HSV title with light background
        self.hsv_label = tk.Label(self.root,text="HSV:", font=("Calibri",15,"bold"), fg=TEXT_COLOR ,bg=DARK_COLOR, width=1000)
        self.hsv_label.pack(pady=(20,0))


        #variables to hold the HSV values
        self.hsv0_var, self.hsv1_var, self.hsv2_var = tk.IntVar(),tk.IntVar(),tk.IntVar()

        #red slider
        self.hsv0 = tk.Scale(self.root, command=self.HSV_color_change,variable=self.hsv0_var ,font='Helvetica 18 bold', from_=0, to=360,background=HSV_SLIDE,foreground=TEXT_COLOR, sliderrelief='flat', troughcolor=LIGHT_COLOR,highlightthickness=0, activebackground=ACTIVE,orient="horizontal", length=300,bd=5)
        self.hsv0.set(0)
        self.hsv0.pack(pady=(20,10))

        #green slider
        self.hsv1 = tk.Scale(self.root, command=self.HSV_color_change,variable=self.hsv1_var ,font='Helvetica 18 bold', from_=0, to=100,background=HSV_SLIDE,foreground=TEXT_COLOR, sliderrelief='flat', troughcolor=LIGHT_COLOR,highlightthickness=0, activebackground=ACTIVE,orient="horizontal", length=300,bd=5)
        self.hsv1.set(0)
        self.hsv1.pack(pady=(0,10))

        #blue slider
        self.hsv2 = tk.Scale(self.root, command=self.HSV_color_change,variable=self.hsv2_var ,font='Helvetica 18 bold', from_=0, to=100,background=HSV_SLIDE,foreground=TEXT_COLOR, sliderrelief='flat', troughcolor=LIGHT_COLOR,highlightthickness=0, activebackground=ACTIVE,orient="horizontal", length=300,bd=5)
        self.hsv2.set(0)
        self.hsv2.pack(pady=(0,8))

        tk.mainloop()


    def RGB_color_change(self,value) -> None:
        """
        function that gets executed when one of the RGB sliders move
        changes the preview to the current color and moves the HSV sliders
        changes the hex value at the top
        """

        #gets the current RGB value
        rgb = (self.red_var.get(),self.green_var.get(),self.blue_var.get())

        #converts it to the accurate messurements for the rgb_to_hsv func
        hsv = rgb_to_hsv(*tuple(map(lambda x: x/255,rgb)))
        hsv = (hsv[0]*3.6,hsv[1],hsv[2])

        #converts the hsv to int and multiplies by hundred which is how HSV is usually viewed
        hsv = tuple(map(lambda x: int(x*100),hsv))

        #moves the hsv sliders
        self.hsv0_var.set(hsv[0])
        self.hsv1_var.set(hsv[1])
        self.hsv2_var.set(hsv[2])

        #changes the preview and the hex value
        current_color = rgb_to_hex(*rgb)
        
        self.color_preview.configure(bg = current_color)

        self.hex.configure(text=current_color)
        self.hex.pack()


    def HSV_color_change(self,value) -> None:
        """
        function that gets executed when one of the HSV sliders move
        changes the preview to the current color and moves the RGB sliders
        changes the hex value at the top
        """

        #gets the current HSV value
        hsv = (self.hsv0_var.get(),self.hsv1_var.get(),self.hsv2_var.get())

        #converts it to the accurate messurements for the hsv_to_rgb func
        hsv = (hsv[0]/360,hsv[1]/100,hsv[2]/100)
        
        #converts the hsv to int and multiplies by 255 because the values are from 0.0 to 1.0
        rgb = tuple(map(lambda x: int(x*255),hsv_to_rgb(*hsv)))

        #moves the sliders
        self.red_var.set(rgb[0])
        self.green_var.set(rgb[1])
        self.blue_var.set(rgb[2])

        #changes the preview and the hex value
        hex = rgb_to_hex(*rgb)

        self.color_preview.configure(bg = hex)

        self.hex.configure(text= hex)
        self.hex.pack()

if __name__ == '__main__':
    try:
        Software()
    except Exception as e:
        print(e) #prints to the console
        input("\n\nPress enter to quit ...")