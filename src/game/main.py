from tkinter import *
from game import game
from global_variables import *
from exit_window import exit_window
from centering_window import centering_window

window_width = 350
window_height = 175

def main_window():
    window = Tk()
    window.title("Select team")

    center_x, center_y = centering_window(window, window_width, window_height)
    window.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

    label = Label(window, text="Select team")
    label.config(font=(font, title_font_size))
    label.grid(column=0, row=0, columnspan=2, padx=title_x_padding, pady=title_y_padding)

    x_button = Button(window, text="X", width=button_width, command=lambda: game("X", window))
    x_button.config(font=(font, button_font_size))
    x_button.grid(column=0, row=1, padx=row_button_x_padding, pady=row_button_y_padding)
    o_button = Button(window, text="O", width=button_width, command=lambda: game("O", window))
    o_button.config(font=(font, button_font_size))
    o_button.grid(column=1, row=1, padx=row_button_x_padding, pady=row_button_y_padding)

    exit_button = Button(window, text="Exit", width=button_width, command=lambda: exit_window(window))
    exit_button.config(font=(font, small_button_font_size))
    exit_button.grid(column=0, row=2, columnspan=2, padx=button_x_padding, pady=button_y_padding)

    window.mainloop()

if __name__ == "__main__":
    main_window()