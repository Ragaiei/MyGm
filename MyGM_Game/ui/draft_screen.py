import tkinter as tk
from game.draft import draft_pick, current_turn

def draft_screen(root, game, go_match):
    for w in root.winfo_children():
        w.destroy()

    tk.Label(root, text="Draft Phase", font=("Arial",18)).pack()

    turn = tk.Label(root)
    turn.pack()

    frame = tk.Frame(root)
    frame.pack()

    pool = tk.Listbox(frame, width=30)
    pool.grid(row=0,column=0)

    boxes={}
    col=1
    for b,c in [("RAW","red"),("SmackDown","blue"),("ECW","black")]:
        f=tk.Frame(frame)
        f.grid(row=0,column=col)
        tk.Label(f,text=b,fg=c).pack()
        lb=tk.Listbox(f,width=25)
        lb.pack()
        boxes[b]=lb
        col+=1

    def update():
        pool.delete(0,tk.END)
        for w in game["pool"]:
            pool.insert(tk.END,w["name"])

        for b in boxes:
            boxes[b].delete(0,tk.END)
            for w in game["brands"][b]:
                boxes[b].insert(tk.END,w["name"])

        turn.config(text=f"Turn: {current_turn(game)}")

    def pick():
        sel=pool.curselection()
        if not sel: return
        draft_pick(game, sel[0])
        update()

    tk.Button(root,text="Draft",command=pick).pack(pady=5)
    tk.Button(root,text="Next",command=go_match).pack()

    update()