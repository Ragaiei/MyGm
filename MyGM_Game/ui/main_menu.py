import tkinter as tk
import json, os

def main_menu(root, start_game, load_game):
    for w in root.winfo_children():
        w.destroy()

    tk.Label(root, text="🔥 MyGM PRO 🔥", font=("Arial",24)).pack(pady=20)

    tk.Button(root, text="New Game", width=20, command=start_game).pack(pady=10)

    if os.path.exists("save.json"):
        tk.Button(root, text="Load Game", width=20, command=load_game).pack(pady=10)