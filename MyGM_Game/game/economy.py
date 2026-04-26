def calc_show(game, matches):
    total = 0
    income = 0

    for m in matches:
        w = m["wrestlers"]
        base = sum([x["power"]+x["pop"] for x in w]) / len(w)

        for i in range(len(w)):
            for j in range(i+1,len(w)):
                key = tuple(sorted([w[i]["name"], w[j]["name"]]))
                base += game["rivalries"].get(key,0)*5

        if m["title"]:
            base += 20
            income += 50000

        total += base
        income += int(base*100)

    rating = int(total/len(matches)) if matches else 0
    return rating, income