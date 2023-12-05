import time
with open("5/input.txt") as f:
    data = f.readlines()

seeds = [int(x) for x in data[0].strip().split(" ")[1:]]

def get_maps(data):
    data = data[1:]
    c = 0 
    maps = []
    while c < len(data): 
        new_map = []
        if data[c][0].isalpha(): #new map
            c+=1
            try: 
                while data[c][0].isnumeric():
                    new_map.append([int(x) for x in data[c].split(" ")])
                    c+=1
            except IndexError:
                pass
            maps.append(new_map)
        c+=1
    return maps

def map_seed(nr, map_): #reverse mapping
    for mapping in map_: 
        if nr in range(mapping[0], (mapping[0] + mapping[2])):
            return (mapping[1] + nr - mapping[0])
    return nr

def map_seed_forward(nr, map_): 
    for mapping in map_: 
        if nr in range(mapping[1], (mapping[1] + mapping[2])):
            return (mapping[0] + nr - mapping[1])
    return nr

def get_lowest_loc(seeds, maps, debug=False):
    for map in maps: 
        for c, seed in enumerate(seeds):
            seeds[c] = map_seed_forward(seed, map)
    return min(seeds) 


def get_lowest_loc_ranges(seeds, maps, debug=True):
    loc_orig = 0
    while True: 
        loc = loc_orig
        for mapping in maps: 
            loc = map_seed(loc, mapping)
        if any(loc in x for x in seeds):
            print("DONE")
            return loc_orig
        loc_orig += 1
        if debug and (loc_orig % 100_000) == 0: 
            print(loc_orig)

maps = get_maps(data)
#Part 1
start = time.time()
print(get_lowest_loc(seeds, maps))
print(f"Took: {time.time()-start} s")
#Part 2 soo much seeds
seeds = [int(x) for x in data[0].strip().split(" ")[1:]]
seeds = [range(x,(x+y)) for x,y in zip(seeds[::2], seeds[1::2])]

# Lol brute force but backwards
maps.reverse()
start = time.time()
print(get_lowest_loc_ranges(seeds, maps))
print(f"Took: {time.time()-start} s")