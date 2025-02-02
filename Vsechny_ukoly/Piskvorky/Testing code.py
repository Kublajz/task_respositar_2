""" CONFIG """
playerX = "X"  # Symbol pro hráče X
playerO = "O"  # Symbol pro hráče O
board_size = 6  # Velikost hracího pole (6x6)
win_length = 5  # Počet políček v řadě pro výhru

# Barvy
color_blue = "#4584b6"  # Barva pro písmo na políčkách
color_yellow = "#ffde57"  # Barva pro zvýraznění vítězných polí
color_gray = "#343434"  # Barva pozadí herního pole
color_light_gray = "#646464"  # Světlejší barva pro vítězná pole

# Stavové proměnné
next_player = playerX  # Nastaví, že první hráč je X
curr_player = playerX  # Nastaví, že první hráč je X
turns = 0  # Počáteční počet tahů je 0
game_over = False  # Hra ještě neskončila

""" LOGIKA """
def set_tile(row, column):  # Funkce pro nastavení políčka po kliknutí
    global curr_player

    if game_over:  # Pokud je hra skončená, nedělej nic
        return

    if board[row][column]["text"] != "":  # Pokud je pole již obsazené
        return

    board[row][column]["text"] = curr_player  # Označení políčka aktuálním hráčem

    if curr_player == playerO:  # Pokud je aktuální hráč O, přepni na X
        curr_player = playerX
    else:  # Pokud je aktuální hráč X, přepni na O
        curr_player = playerO

    label["text"] = curr_player + " je na tahu"  # Změní text na panelu, kdo je na tahu

    check_winner()  # Zavolání funkce pro kontrolu, jestli někdo vyhrál


def check_winner():  # Funkce pro kontrolu vítěze
    global turns, game_over
    turns += 1  # Zvyšuje počet tahů

    # Kontrola horizontální, vertikální a diagonální výhry
    for row in range(board_size):
        for column in range(board_size):
            if check_line(row, column, 1, 0) or check_line(row, column, 0, 1) or \
               check_line(row, column, 1, 1) or check_line(row, column, 1, -1):
                game_over = True  # Hra končí, protože někdo vyhrál
                label.config(text=f"{board[row][column]['text']} je výherce!", foreground=color_yellow)
                return

    # Kontrola remízy
    if turns == board_size * board_size:  # Pokud jsou všechna políčka obsazena
        game_over = True
        label.config(text="Remíza!", foreground=color_yellow)


def check_line(start_row, start_col, step_row, step_col):  # Funkce pro kontrolu řady políček
    """Zkontroluje řadu políček ve směru (step_row, step_col)"""
    initial = board[start_row][start_col]["text"]
    if initial == "":
        return False

    winning_positions = []
    for i in range(win_length):  # Prochází všechny pozice v řadě
        r = start_row + i * step_row
        c = start_col + i * step_col
        if 0 <= r < board_size and 0 <= c < board_size and board[r][c]["text"] == initial:
            winning_positions.append((r, c))
        else:
            break

    if len(winning_positions) == win_length:  # Pokud délka vítězné sekvence odpovídá požadované délce
        highlight_winner(winning_positions)
        return True
    return False


def highlight_winner(positions):  # Funkce pro barevné zvýraznění vítězných polí
    """Barevně zvýrazní vítězná pole"""
    for r, c in positions:
        board[r][c].config(background=color_yellow, foreground=color_light_gray)


def new_game():  # Funkce pro spuštění nové hry
    global turns, game_over, curr_player, next_player
    turns = 0
    game_over = False
    curr_player = next_player  # Nastavíme aktuálního hráče podle hodnoty next_player
    next_player = playerX if curr_player == playerO else playerO  # Přepneme na druhého hráče

    label.config(text=curr_player + " je na tahu", foreground="white")

    for row in range(board_size):
        for column in range(board_size):
            board[row][column].config(text="", foreground=color_blue, background=color_gray)

""" UI """
import tkinter  # Importuje knihovnu tkinter pro tvorbu grafického uživatelského rozhraní

# Inicializace hracího pole
board = [[0 for _ in range(board_size)] for _ in range(board_size)]  # Vytvoření prázdného hracího pole o velikosti 6x6

# Window setup
window = tkinter.Tk()
window.title("Piškvorky")
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text=curr_player + " je na tahu", font=("Consolas", 20), background=color_gray, foreground="white")
label.grid(row=0, column=0, columnspan=board_size, sticky="we")

for row in range(board_size):
    for column in range(board_size):
        board[row][column] = tkinter.Button(frame, text="", font=("Consolas", 30, "bold"), background=color_gray, foreground=color_blue, width=3, height=1, command=lambda row=row, column=column: set_tile(row, column))
        board[row][column].grid(row=row + 1, column=column)

button = tkinter.Button(frame, text="Restart", font=("Consolas", 20), background=color_gray, foreground="white", command=new_game)
button.grid(row=board_size + 1, column=0, columnspan=board_size, sticky="we")

frame.pack()

# Vycentrování okna
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width / 2) - (window_width / 2))
window_y = int((screen_height / 2) - (window_height / 2))

window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.mainloop()
