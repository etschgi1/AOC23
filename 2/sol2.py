with open("2/input.txt", "r") as f:
    lines = f.readlines()

LOADED = (12, 13, 14) #RGB

games = {}

def get_rgb_tuple(rounds):
    l = []
    for round in rounds:
        r,g,b = 0,0,0
        round = round.replace(" ", "")
        round = round.split(",")
        for c in round:
            if "red" in c:
                r = int(c.split("r")[0])
            elif "green" in c:
                g = int(c.split("g")[0])
            elif "blue" in c:
                b = int(c.split("b")[0])
        l.append((r,g,b))
    return l

def tuple_all_samller_eq(t1,t2):
    for i,j in zip(t1,t2):
        if i > j:
            return False
    return True

for line in lines: 
    game_id = line.split(":")[0].split(" ")[-1]
    draw_rounds = line.split(":")[1].split(";")
    games[game_id] = get_rgb_tuple(draw_rounds)

# part 1 check games
sum_ = 0
for game_id in games:
    if all(tuple_all_samller_eq(round, LOADED) for round in games[game_id]):
        sum_ += int(game_id)
print(sum_)

# part 2 calc power
game_maxs = {"r":[], "g":[], "b":[]}
for game_id in games:
    game_maxs["r"].append(max([round[0] for round in games[game_id]]))
    game_maxs["g"].append(max([round[1] for round in games[game_id]]))
    game_maxs["b"].append(max([round[2] for round in games[game_id]]))

# multiply
r = game_maxs["r"]
g = game_maxs["g"]
b = game_maxs["b"]
sum_ = 0
for r,g,b in zip(r,g,b):
    sum_ += r*g*b
print(sum_)