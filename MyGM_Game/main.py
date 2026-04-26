import tkinter as tk

from game.state import new_game
from ui.main_menu import main_menu
from ui.draft_screen import draft_screen
from ui.match_screen import match_screen


# =========================
# WINDOW SETUP
# =========================
root = tk.Tk()
root.geometry("1000x650")
root.title("🔥 MyGM PRO - Full Game 🔥")

# =========================
# GAME STATE
# =========================
game = {}

# =========================
# NAVIGATION FUNCTIONS
# =========================
def start_new_game():
    global game
    game = new_game()
    go_draft()

def go_draft():
    draft_screen(root, game, go_match)

def go_match():
    match_screen(root, game)

def load_saved_game(saved_game):
    global game
    game = saved_game
    go_draft()

# =========================
# START APP
# =========================
main_menu(
    root=root,
    start_game=start_new_game,
    load_game=load_saved_game
)

root.mainloop()