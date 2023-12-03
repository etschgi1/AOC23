with open("3/input.txt", "r") as f:
    lines = f.readlines()

# indices = [] # lineindex, startindex, endindex

def parselines(lines, only_star=False, index_dict = False):
    indices = []
    indices_dict = {str(x): [] for x in range(len(lines))}
    symbols = {str(x): [] for x in range(len(lines))}
    for lnr, line in enumerate(lines): 
        line = line.strip()
        c = 0
        while c < len(line):
            cur = line[c]
            if cur.isnumeric():
                s = c
                c+=1
                while c < len(line) and line[c].isnumeric():
                    c+=1
                e = c
                num = int(line[s:e])
                if index_dict:
                    indices_dict[str(lnr)] += [(s,e,num)]
                indices.append((lnr ,s ,e, num))
                c -= 1
            elif cur != ".":
                if only_star == False or cur == "*":
                    symbols[str(lnr)] += [c]
            c += 1
    if index_dict:
        return indices_dict, symbols
    return indices, symbols 


def checkforsymbol(symbols, row, s,e):
    l, r = s-1, e+1
    #check left + right
    if any(x in symbols[str(row)] for x in list(range(max(0,l),r))):
        return True
    # check top
    if row > 0 and any(x in symbols[str(row-1)] for x in list(range(l,r))):
        return True
    try:
        if any(x in symbols[str(row+1)] for x in list(range(l, r))):
            return True
    except Exception:
        pass
    return False 


def reduce_nums(num_indices, symbols):
    sum_ = 0
    for num_ in num_indices:
        row_ , s, e, num = num_
        if checkforsymbol(symbols, row_, s,e):
            sum_ += num
    return sum_

def getgearratio(num_indices, star_row, star_index):
    gears = []
    #top
    if star_row > 0:
        for s,e, num in num_indices[str(star_row-1)]:
            if star_index in list(range(max(0,s-1),e+1)):
                gears.append(num)
    # left right
    for s,e,num in num_indices[str(star_row)]:
        if star_index in list(range(max(0,s-1),e+1)):
                gears.append(num)
    # bottom
    try: 
        for s,e,num in num_indices[str(star_row+1)]:
            if star_index in list(range(max(0,s-1),e+1)):
                    gears.append(num)
    except Exception:
        pass
    if len(gears) == 2: 
        return gears[0]*gears[1]
    elif len(gears) > 2: 
        raise Exception("Seems off!")
    return 0


def getratiosum(num_indices, stars):
    sum_ = 0
    for row in stars.keys():
        stars_in_row = stars[row]
        for star in stars_in_row:
            sum_ += getgearratio(num_indices, int(row), star)
    return sum_


num_indices, symbols = parselines(lines)
#Part 1
print(reduce_nums(num_indices, symbols))

#Part 2 
indices, stars = parselines(lines, only_star=True, index_dict=True)
print(getratiosum(indices, stars))
