# game_logic.py

from config import board_size, win_length, playerX, playerO, color_yellow, color_light_gray

# Herní proměnné
turns = 0
game_over = False
curr_player = playerX

def set_tile(row, column, board, label):
    """ Nastaví políčko na hrací ploše při kliknutí a změní hráče. """
    global curr_player, game_over, turns

    if game_over or board[row][column]["text"] != "":
        return  # Nedovolí tah, pokud je pole obsazené nebo hra skončila

    board[row][column]["text"] = curr_player  # Nastaví symbol hráče

    # Přepnutí hráče
    curr_player = playerO if curr_player == playerX else playerX
    label["text"] = f"{curr_player} je na tahu"

    turns += 1
    check_winner(board, label)

def check_winner(board, label):
    """ Kontroluje, zda někdo vyhrál hru. """
    global game_over

    for row in range(board_size):
        for column in range(board_size):
            if check_line(board, row, column, 1, 0) or \
               check_line(board, row, column, 0, 1) or \
               check_line(board, row, column, 1, 1) or \
               check_line(board, row, column, 1, -1):
                game_over = True
                label.config(text=f"{board[row][column]['text']} je výherce!", foreground=color_yellow)
                return

    # Kontrola remízy
    if turns == board_size * board_size:
        game_over = True
        label.config(text="Remíza!", foreground=color_yellow)

def check_line(board, start_row, start_col, step_row, step_col):
    """ Kontroluje řadu políček daným směrem. """
    initial = board[start_row][start_col]["text"]
    if initial == "":
        return False

    winning_positions = []
    for i in range(win_length):
        r, c = start_row + i * step_row, start_col + i * step_col
        if 0 <= r < board_size and 0 <= c < board_size and board[r][c]["text"] == initial:
            winning_positions.append((r, c))
        else:
            break

    if len(winning_positions) == win_length:
        highlight_winner(board, winning_positions)
        return True
    return False

def highlight_winner(board, positions):
    """ Zvýrazní vítězná políčka. """
    for r, c in positions:
        board[r][c].config(background=color_yellow, foreground=color_light_gray)

def new_game(board, label):
    """ Restartuje hru. """
    global turns, game_over, curr_player
    turns = 0
    game_over = False
    curr_player = playerX  # Začíná hráč X

    label.config(text=f"{curr_player} je na tahu", foreground="white")

    for row in range(board_size):
        for column in range(board_size):
            board[row][column].config(text="", foreground=color_blue, background=color_gray)
