import random

def simulate_match(wrestlers):
    return max(wrestlers, key=lambda x: x["power"] + x["pop"] + random.randint(0,20))

def update_rivalries(game, wrestlers):
    for i in range(len(wrestlers)):
        for j in range(i+1,len(wrestlers)):
            key = tuple(sorted([wrestlers[i]["name"], wrestlers[j]["name"]]))
            game["rivalries"][key] = game["rivalries"].get(key,0)+1

def check_injury(game, w):
    if random.random() < 0.15:
        game["injuries"][w["name"]] = random.randint(1,3)