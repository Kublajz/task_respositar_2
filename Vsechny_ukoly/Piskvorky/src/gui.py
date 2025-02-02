# gui.py

import tkinter as tk
from config import board_size, color_blue, color_gray, playerX
from game_logic import set_tile, new_game

# Vytvoření hlavního okna
window = tk.Tk()
window.title("Piškvorky")
window.resizable(False, False)

# Rámeček pro prvky GUI
frame = tk.Frame(window)

# Štítek s informací o tahu hráče
label = tk.Label(frame, text=f"{playerX} je na tahu", font=("Consolas", 20), background=color_gray, foreground="white")
label.grid(row=0, column=0, columnspan=board_size, sticky="we")

# Hrací pole
board = [[None for _ in range(board_size)] for _ in range(board_size)]
for row in range(board_size):
    for column in range(board_size):
        board[row][column] = tk.Button(
            frame, text="", font=("Consolas", 30, "bold"), background=color_gray,
            foreground=color_blue, width=3, height=1,
            command=lambda r=row, c=column: set_tile(r, c, board, label)
        )
        board[row][column].grid(row=row + 1, column=column)

# Tlačítko pro restart hry
restart_button = tk.Button(frame, text="Restart", font=("Consolas", 20), background=color_gray, foreground="white",
                           command=lambda: new_game(board, label))
restart_button.grid(row=board_size + 1, column=0, columnspan=board_size, sticky="we")

# Zobrazení prvků GUI
frame.pack()

# Spuštění hlavní smyčky
window.mainloop()
