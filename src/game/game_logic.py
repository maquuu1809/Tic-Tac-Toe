import tkinter
from random import choice
from win_window import win_window
from draw_window import draw_window

game = ["", "", "",
        "", "", "",
        "", "", ""]

occupied = []

def restart(canvas, first_x_line, first_y_line, second_x_line, second_y_line, canvas_width, canvas_height):
    occupied.clear()
    game.clear()
    for i in range(0,9):
        game.append("")
    canvas.delete("all")
    canvas.create_line(first_y_line, 0, first_y_line, canvas_height)
    canvas.create_line(second_y_line, 0, second_y_line, canvas_height)
    canvas.create_line(0, first_x_line, canvas_width, first_x_line)
    canvas.create_line(0, second_x_line, canvas_width, second_x_line)

def reset_game():
    global game, occupied
    occupied.clear()
    game = [""] * 9

def change_team(window, main_window):
    window.destroy()
    reset_game()
    main_window()

def won_check(main_window, canvas, blocks, player):
    if game[0] == game[1] == game[2] != "":
        canvas.create_line(blocks["1"]["middle_point"]["x"] - 25, blocks["1"]["middle_point"]["y"],
                           blocks["3"]["middle_point"]["x"] + 25, blocks["3"]["middle_point"]["y"], fill="#FF0000", width=30, capstyle=tkinter.ROUND)
    if game[3] == game[4] == game[5] != "":
        canvas.create_line(blocks["4"]["middle_point"]["x"] - 25, blocks["4"]["middle_point"]["y"],
                           blocks["6"]["middle_point"]["x"] + 25, blocks["6"]["middle_point"]["y"], fill="#FF0000", width=30, capstyle=tkinter.ROUND)
    if game[6] == game[7] == game[8] != "":
        canvas.create_line(blocks["7"]["middle_point"]["x"] - 25, blocks["7"]["middle_point"]["y"],
                           blocks["9"]["middle_point"]["x"] + 25, blocks["9"]["middle_point"]["y"], fill="#FF0000", width=30, capstyle=tkinter.ROUND)

    if game[0] == game[3] == game[6] != "":
        canvas.create_line(blocks["1"]["middle_point"]["x"], blocks["1"]["middle_point"]["y"] - 25,
                           blocks["7"]["middle_point"]["x"], blocks["7"]["middle_point"]["y"] + 25, fill="#FF0000", width=30, capstyle=tkinter.ROUND)
    if game[1] == game[4] == game[7] != "":
        canvas.create_line(blocks["2"]["middle_point"]["x"], blocks["2"]["middle_point"]["y"] - 25,
                           blocks["8"]["middle_point"]["x"], blocks["8"]["middle_point"]["y"] + 25, fill="#FF0000", width=30, capstyle=tkinter.ROUND)
    if game[2] == game[5] == game[8] != "":
        canvas.create_line(blocks["3"]["middle_point"]["x"], blocks["3"]["middle_point"]["y"] - 25,
                           blocks["9"]["middle_point"]["x"], blocks["9"]["middle_point"]["y"] + 25, fill="#FF0000", width=30, capstyle=tkinter.ROUND)

    if game[0] == game[4] == game[8] != "":
        canvas.create_line(blocks["1"]["middle_point"]["x"] - 25, blocks["1"]["middle_point"]["y"] - 25,
                           blocks["9"]["middle_point"]["x"] + 25, blocks["9"]["middle_point"]["y"] + 25, fill="#FF0000", width=30, capstyle=tkinter.ROUND)
    if game[2] == game[4] == game[6] != "":
        canvas.create_line(blocks["3"]["middle_point"]["x"] + 25, blocks["3"]["middle_point"]["y"] - 25,
                           blocks["7"]["middle_point"]["x"] - 25, blocks["7"]["middle_point"]["y"] + 25, fill="#FF0000", width=30, capstyle=tkinter.ROUND)



    if (game[0] == game[1] == game[2] != ""
            or game[3] == game[4] == game[5] != ""
            or game[6] == game[7] == game[8] != ""
            or game[0] == game[3] == game[6] != ""
            or game[1] == game[4] == game[7] != ""
            or game[2] == game[5] == game[8] != ""
            or game[0] == game[4] == game[8] != ""
            or game[2] == game[4] == game[6] != ""):
        win_window(player, main_window)
        return True
    return False

def bot_move(window, canvas, team, blocks, margin):
    random_move = choice([i for i in range(0, 8) if i not in occupied])
    if team == "O":
        canvas.create_line(blocks[str(random_move + 1)]["top_left"]["x"] + margin, blocks[str(random_move + 1)]["top_left"]["y"] + margin,
                           blocks[str(random_move + 1)]["bottom_right"]["x"] - margin,
                           blocks[str(random_move + 1)]["bottom_right"]["y"] - margin)
        canvas.create_line(blocks[str(random_move + 1)]["top_right"]["x"] - margin, blocks[str(random_move + 1)]["top_right"]["y"] + margin,
                           blocks[str(random_move + 1)]["bottom_left"]["x"] + margin,
                           blocks[str(random_move + 1)]["bottom_left"]["y"] - margin)
        game[random_move] = "X"
    elif team == "X":
        canvas.create_oval(blocks[str(random_move + 1)]["top_left"]["x"] + margin, blocks[str(random_move + 1)]["top_left"]["y"] + margin,
                           blocks[str(random_move + 1)]["bottom_right"]["x"] - margin,
                           blocks[str(random_move + 1)]["bottom_right"]["y"] - margin)
        game[random_move] = "O"
    player = "Bot"
    occupied.append(random_move)
    won_check(window, canvas, blocks, player)

def player_move(event, window, canvas, team, blocks, margin):
    for block in blocks:
        if blocks[block]["top_left"]["x"] <= event.x <= blocks[block]["top_right"]["x"] and blocks[block]["top_left"][
            "y"] <= event.y <= blocks[block]["bottom_left"]["y"] and game[int(block) - 1] == "":
            if team == "O":
                canvas.create_oval(blocks[block]["top_left"]["x"] + margin, blocks[block]["top_left"]["y"] + margin,
                                   blocks[block]["bottom_right"]["x"] - margin,
                                   blocks[block]["bottom_right"]["y"] - margin)
                game[int(block) - 1] = "O"
            elif team == "X":
                canvas.create_line(blocks[block]["top_left"]["x"] + margin, blocks[block]["top_left"]["y"] + margin,
                                   blocks[block]["bottom_right"]["x"] - margin,
                                   blocks[block]["bottom_right"]["y"] - margin)
                canvas.create_line(blocks[block]["top_right"]["x"] - margin, blocks[block]["top_right"]["y"] + margin,
                                   blocks[block]["bottom_left"]["x"] + margin,
                                   blocks[block]["bottom_left"]["y"] - margin)
                game[int(block) - 1] = "X"
            player = "You"
            occupied.append(int(block) - 1)
            if won_check(window, canvas, blocks, player):
                return

            if len(occupied) == 9:
                draw_window(window)
                return

            bot_move(window, canvas, team, blocks, margin)