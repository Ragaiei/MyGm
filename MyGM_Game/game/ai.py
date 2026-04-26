import random

def ai_pick(pool):
    return max(pool, key=lambda x: x["power"] + x["pop"])

def ai_book_matches(roster):
    matches = []
    r = roster[:]
    random.shuffle(r)

    while len(r) >= 2:
        a = r.pop()
        b = r.pop()
        matches.append({"wrestlers":[a,b], "title": None})

    return matches