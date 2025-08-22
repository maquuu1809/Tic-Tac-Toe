from tkinter import *
from global_variables import *
from centering_window import centering_window

window_width = 232
window_height = 125

def win_window(player, main_window):
    window = Toplevel(main_window)
    window.title("Winner!")

    center_x, center_y = centering_window(window, window_width, window_height)
    window.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

    label = Label(window, text=f"{player} won the game!")
    label.config(font=(font, title_font_size))
    label.grid(column=0, row=0, padx=title_x_padding, pady=title_y_padding)

    back_button = Button(window, text="Back", width=button_width, command=window.destroy)
    back_button.config(font=(font, small_button_font_size))
    back_button.grid(column=0, row=1, padx=title_x_padding, pady=title_y_padding)

    window.grab_set()