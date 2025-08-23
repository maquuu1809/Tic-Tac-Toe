from tkinter import *
from global_variables import *
from exit_window import exit_window
from game_logic import player_move, restart, change_team
from centering_window import centering_window

window_width = 700
window_height = 800

canvas_width = 600
canvas_height = 600

first_y_line = canvas_width / 3
second_y_line = first_y_line + canvas_width / 3

first_x_line = canvas_height / 3
second_x_line = first_x_line + canvas_height / 3

margin = 10

blocks = {
    "1": {
        "middle_point": {
            "x": first_y_line / 2,
            "y": first_x_line / 2
        },
        "top_left": {
            "x": 0,
            "y": 0
        },
        "top_right": {
            "x": first_y_line,
            "y": 0
        },
        "bottom_left": {
            "x": 0,
            "y": first_x_line
        },
        "bottom_right": {
            "x": first_y_line,
            "y": first_x_line
        }
    },
    "2": {
        "middle_point": {
            "x": first_y_line * 3 / 2,
            "y": first_x_line / 2
        },
        "top_left": {
            "x": first_y_line,
            "y": 0
        },
        "top_right": {
            "x": second_y_line,
            "y": 0
        },
        "bottom_left": {
            "x": first_y_line,
            "y": first_x_line
        },
        "bottom_right": {
            "x": second_y_line,
            "y": first_x_line
        }
    },
    "3": {
        "middle_point": {
            "x": first_y_line * 5 / 2,
            "y": first_x_line / 2
        },
        "top_left": {
            "x": second_y_line,
            "y": 0
        },
        "top_right": {
            "x": canvas_width,
            "y": 0
        },
        "bottom_left": {
            "x": second_y_line,
            "y": first_x_line
        },
        "bottom_right": {
            "x": canvas_width,
            "y": first_x_line
        }
    },
    "4": {
        "middle_point": {
            "x": first_y_line / 2,
            "y": first_x_line * 3 / 2
        },
        "top_left": {
            "x": 0,
            "y": first_x_line
        },
        "top_right": {
            "x": first_y_line,
            "y": first_x_line
        },
        "bottom_left": {
            "x": 0,
            "y": second_x_line
        },
        "bottom_right": {
            "x": first_y_line,
            "y": second_x_line
        }
    },
    "5": {
        "middle_point": {
            "x": first_y_line * 3 / 2,
            "y": first_x_line * 3 / 2
        },
        "top_left": {
            "x": first_y_line,
            "y": first_x_line
        },
        "top_right": {
            "x": second_y_line,
            "y": first_x_line
        },
        "bottom_left": {
            "x": first_y_line,
            "y": second_x_line
        },
        "bottom_right": {
            "x": second_y_line,
            "y": second_x_line
        }
    },
    "6": {
        "middle_point": {
            "x": first_y_line * 5 / 2,
            "y": first_x_line * 3 / 2
        },
        "top_left": {
            "x": second_y_line,
            "y": first_x_line
        },
        "top_right": {
            "x": canvas_width,
            "y": first_x_line
        },
        "bottom_left": {
            "x": second_y_line,
            "y": second_x_line
        },
        "bottom_right": {
            "x": canvas_width,
            "y": second_x_line
        }
    },
    "7": {
        "middle_point": {
            "x": first_y_line / 2,
            "y": first_x_line * 5 / 2
        },
        "top_left": {
            "x": 0,
            "y": second_x_line
        },
        "top_right": {
            "x": first_y_line,
            "y": second_x_line
        },
        "bottom_left": {
            "x": 0,
            "y": canvas_height
        },
        "bottom_right": {
            "x": first_y_line,
            "y": canvas_height
        }
    },
    "8": {
        "middle_point": {
            "x": first_y_line * 3 / 2,
            "y": first_x_line * 5 / 2
        },
        "top_left": {
            "x": first_y_line,
            "y": second_x_line
        },
        "top_right": {
            "x": second_y_line,
            "y": second_x_line
        },
        "bottom_left": {
            "x": first_y_line,
            "y": canvas_height
        },
        "bottom_right": {
            "x": second_y_line,
            "y": canvas_height
        }
    },
    "9": {
        "middle_point": {
            "x": first_y_line * 5 / 2,
            "y": first_x_line * 5 / 2
        },
        "top_left": {
            "x": second_y_line,
            "y": second_x_line
        },
        "top_right": {
            "x": canvas_width,
            "y": second_x_line
        },
        "bottom_left": {
            "x": second_y_line,
            "y": canvas_height
        },
        "bottom_right": {
            "x": canvas_width,
            "y": canvas_height
        }
    }
}

def game(team, previous_window):
    from main import main_window
    previous_window.destroy()

    window = Tk()
    window.title("Tic-Tac-Toe")

    center_x, center_y = centering_window(window, window_width, window_height)
    window.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

    if team == "O":
        label = Label(window, text="Playing as O")
    else:
        label = Label(window, text="Playing as X")
    label.config(font=(font, title_font_size))
    label.grid(column=0, row=0, columnspan=3, padx=title_x_padding, pady=title_y_padding)

    def canvas_click_event(event):
        player_move(event, window, canvas, team, blocks, margin)

    canvas = Canvas(window, width=canvas_width, height=canvas_height, bd=1, relief='solid')
    canvas.create_line(first_y_line, 0, first_y_line, canvas_height)
    canvas.create_line(second_y_line, 0, second_y_line, canvas_height)
    canvas.create_line(0, first_x_line, canvas_width, first_x_line)
    canvas.create_line(0, second_x_line, canvas_width, second_x_line)
    canvas.bind('<Button-1>', canvas_click_event)
    canvas.grid(column=0, row=1, columnspan=3, padx=40, pady=10)

    restart_button = Button(window, text="Restart", width=button_width, command=lambda: restart(canvas, first_x_line, first_y_line, second_x_line, second_y_line, canvas_width, canvas_height))
    restart_button.config(font=(font, small_button_font_size))
    restart_button.grid(column=0, row=2)

    change_team_button = Button(window, text="Change team", width=button_width, command=lambda: change_team(window, main_window))
    change_team_button.config(font=(font, small_button_font_size))
    change_team_button.grid(column=1, row=2)

    exit_button = Button(window, text="Exit", width=button_width, command=lambda: exit_window(window))
    exit_button.config(font=(font, small_button_font_size))
    exit_button.grid(column=2, row=2)

    window.mainloop()