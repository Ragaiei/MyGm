from game.ai import ai_pick

def current_turn(game):
    return game["turn_order"][game["turn_index"]]

def next_turn(game):
    game["turn_index"] = (game["turn_index"] + 1) % 3

def draft_pick(game, index):
    w = game["pool"][index]
    brand = current_turn(game)

    game["brands"][brand].append(w)
    game["pool"].remove(w)

    next_turn(game)

    if current_turn(game) != "ECW" and game["pool"]:
        ai = ai_pick(game["pool"])
        game["brands"][current_turn(game)].append(ai)
        game["pool"].remove(ai)

    next_turn(game)