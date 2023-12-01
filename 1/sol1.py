with open("1/input.txt", "r") as f:
    lines = f.readlines()

WTON = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6,
        "seven":7, "eight":8, "nine":9}

def get_sum(lines, replace=False):
    sum_ = 0
    for line in lines:
        if replace:
            for key in WTON.keys():
                line = line.replace(key, str(key + str(WTON[key]) + key))
        temp = []
        for c in line:
            if c.isnumeric():
                temp.append(int(c))
        sum_ += 10*temp[0]+temp[-1]
    return sum_
#task 1
print(get_sum(lines))
#task 2
print(get_sum(lines, replace=True))
