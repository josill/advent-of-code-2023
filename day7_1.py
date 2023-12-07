file = open("./inputs/day7.txt", "r")
lines = file.readlines()

queue = {
    "Five of a kind": [],
    "Four of a kind": [],
    "Full house": [],
    "Three of a kind": [],
    "Two pair": [],
    "One pair": [],
    "High card": [],
}

cards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

def get_type(card):
    chars = list(set(card))

    if len(chars) == 1:
        return "Five of a kind"
    elif len(chars) == 2:
        for c in chars:
            if card.count(c) == 4:
                return "Four of a kind"
        return "Full house"
    elif len(chars) == 3:
        for c in chars:
            if card.count(c) == 3:
                return "Three of a kind"
        return "Two pair"
    elif len(chars) == 4:
        return "One pair"
    elif len(chars) == 5:
        return "High card"


def compare_cards(card1, card2):
    for i in range(5):
        if cards.index(card1[i]) < cards.index(card2[i]):
            return card1
        elif cards.index(card1[i]) > cards.index(card2[i]):
            return card2
        
def add_to_queue(card, rank, type):
    type_queue = queue[type]
    pos = len(type_queue)

    if (len(type_queue) == 0): queue[type] = [(card, rank)]
    else:
        for i, card2 in enumerate(type_queue):
            bigger_card = compare_cards(card, card2[0])
            if bigger_card == card:
                pos = i
                break
    
    type_queue.insert(pos, (card, rank))

for line in lines:
    parts = line.split(" ")
    card = parts[0]
    rank = parts[1]

    type = get_type(card)
    add_to_queue(card, rank.strip(), type)

sum = 0
r = 1

for k, v in reversed(queue.items()):
    for t in reversed(v):
        sum += int(t[1]) * r
        r += 1
        
print(queue)
print(sum)
