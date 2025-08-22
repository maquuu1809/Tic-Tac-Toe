from tkinter import *
from global_variables import *
from centering_window import centering_window

window_width = 360
window_height = 125

def exit_window(main_window):
    window = Toplevel(main_window)
    window.title("Exit")

    center_x, center_y = centering_window(window, window_width, window_height)
    window.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

    label = Label(window, text="Are you sure you want to exit?")
    label.config(font=(font, title_font_size))
    label.grid(column=0, row=0, columnspan=2, padx=button_x_padding, pady=button_y_padding)

    yes_button = Button(window, text="Yes", width=button_width, command=quit)
    yes_button.config(font=(font, small_button_font_size))
    yes_button.grid(column=0, row=1, padx=row_button_x_padding, pady=row_button_y_padding,)
    no_button = Button(window, text="No", width=button_width, command=window.destroy)
    no_button.config(font=(font, small_button_font_size))
    no_button.grid(column=1, row=1, padx=row_button_x_padding, pady=row_button_y_padding,)

    window.grab_set()