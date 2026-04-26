import tkinter as tk
from tkinter import messagebox
from game.match import simulate_match, update_rivalries, check_injury
from game.ai import ai_book_matches
from game.economy import calc_show

def match_screen(root, game):

    for w in root.winfo_children():
        w.destroy()

    tk.Label(root,text="ECW Show (Your Brand)",font=("Arial",18)).pack()

    roster = tk.Listbox(root,selectmode=tk.MULTIPLE)
    roster.pack()

    for w in game["brands"]["ECW"]:
        roster.insert(tk.END,w["name"])

    matches=[]
    listbox=tk.Listbox(root,width=60)
    listbox.pack()

    def add_match():
        sel=roster.curselection()
        if len(sel)<2: return
        m=[game["brands"]["ECW"][i] for i in sel]
        matches.append({"wrestlers":m,"title":None})
        listbox.insert(tk.END," vs ".join([x["name"] for x in m]))

    def play():
        ai_raw = ai_book_matches(game["brands"]["RAW"])
        ai_sd = ai_book_matches(game["brands"]["SmackDown"])

        pr, pi = calc_show(game,matches)
        ar,_ = calc_show(game,ai_raw)
        sr,_ = calc_show(game,ai_sd)

        winner = max([("ECW",pr),("RAW",ar),("SD",sr)], key=lambda x:x[1])

        for m in matches:
            w=simulate_match(m["wrestlers"])
            update_rivalries(game,m["wrestlers"])
            for x in m["wrestlers"]:
                check_injury(game,x)

        game["money"] += pi

        messagebox.showinfo("Results",
            f"ECW: {pr}\nRAW: {ar}\nSD: {sr}\n\nWinner: {winner[0]}\nMoney: {game['money']}")

    tk.Button(root,text="Add Match",command=add_match).pack()
    tk.Button(root,text="Play Show",command=play).pack()