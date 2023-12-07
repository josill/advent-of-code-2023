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

cards = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']

def get_type(card):
    j_amount = card.count('J')
    char_amounts = {}

    for c in card:
        if c not in char_amounts: char_amounts[c] = 1
        else: char_amounts[c] += 1

    max_char = max(char_amounts, key=char_amounts.get)
    max_char_nr = char_amounts[max_char]
    print(f"card: {card}")
    print(f"j amount: {j_amount}")
    print(f"max char is: {max_char}")

    if max_char_nr + j_amount == 5 and max_char != 'J' or j_amount == 5 or j_amount == 4: return "Five of a kind"
    if max_char_nr + j_amount == 4 and max_char != 'J': return "Four of a kind"
    if (max_char_nr == 2 and j_amount > 0 and len(char_amounts) == 3) or (max_char_nr == 3 and (len(char_amounts) == 2 or j_amount > 0)): return "Full house"
    if max_char_nr + j_amount == 3: return "Three of a kind"
    if max_char_nr == 2 and ((len(char_amounts) == 3) or j_amount > 0) and max_char != "J": return "Two pair"
    if max_char_nr == 2 or max_char_nr + j_amount == 2: return "One pair"
    else: return "High card"

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
    print("=====")
    type = get_type(card)
    print(type)
    print("=====")
    add_to_queue(card, rank.strip(), type)

sum = 0
r = 1

for k, v in reversed(queue.items()):
    for t in reversed(v):
        sum += int(t[1]) * r
        r += 1
        


# sort and get
print(queue)
print(sum)
