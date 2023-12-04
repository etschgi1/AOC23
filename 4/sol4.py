with open('4/input.txt') as f:
    data = f.readlines()

def parseinput(lines, cardid = False):
    cards = []
    for line_ in lines:
        line = line_.split(":")[-1]
        line = (line.replace("  ", " ")).strip()
        win, my = line.split(" | ")
        win = [int(x) for x in win.split(" ") if x.isnumeric()]
        my = [int(x) for x in my.split(" ") if x.isnumeric()]
        if cardid: 
            id_ = int(line_.split(":")[0][4:])-1
            cards.append([win,my, id_])
        else:
            cards.append([win,my])
    return cards

# part 1
def getwinningtotal(data):
    sum_ = 0
    for line in data: 
        c = 0
        for n in line[0]:
            if n in line[1]:
                c +=1
        if c > 0:
            sum_ += 2**(c-1)
    return sum_

#part 2 rec winning
def getnrwins(card):
    c = 0
    for n in card[0]:
        if n in card[1]:
            c +=1
    return c

def count_cards(original_, data):
    sum_ = 0
    for card in data: 
        wins = getnrwins(card)
        start_ = (card[2]+1)
        sum_ += count_cards(original_, original_[start_:(start_+wins)])
    return sum_
#part1
print(getwinningtotal(parseinput(data)))
#part 2
original_ = parseinput(data, cardid=True)
total_cards = len(original_) + count_cards(original_, original_)
print(total_cards)