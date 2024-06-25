from tkinter import *
from functools import partial # To prevent unwanted windows

import random


class Converter:
    def __init__(self):

        # Formatting variables...
        background_color = "gold"

        # In actual program this is blank and is populated with user calculations
        self.all_calc_list = ['0 degrees C is -17.8 degrees F',
                              '40 degrees C is 32 degrees F',
                              '40 degrees C is 33 degrees F',
                              '12 degrees C is -45 degrees F',
                              '24 degrees C is -87 degrees F',
                              '100 degrees C is -79 degrees F']
        
        # Converter Main Screen GUI...
        self.converter_frame = Frame(width=300, height=300, bg=background_color,
                                     pady=10)
        self.converter_frame.grid()
        
        # Temerature Conversion Heading (row 0)
        self.temp_converter_label = Label(self.converter_frame,
                                          text="Temperature Converter",
                                          font=("Arial", "16", "bold"),
                                          bg=background_color,
                                          padx=10, pady=10)
        self.temp_converter_label.grid(row=0)
        
#main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter()
    root.mainloop()
