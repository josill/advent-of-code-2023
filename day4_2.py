file = open("./inputs/day4.txt", "r")
lines = file.readlines()

cards_total = 0
cards = {}

for i, line in enumerate(lines):
    data = line.split(":")[1]
    cards_total += 1

    win_nrs = data.split("|")[0].strip().split(" ")
    scratch_nrs = data.split("|")[1].strip().split(" ")

    loops = cards[i+1] if i+1 in cards else 1 
    print(line.split(":")[0])
    #print(i+1)
    #print(loops)
    for j in range(loops):
        a_card_nr = i+2
        for nr in scratch_nrs:
            if nr.strip() in win_nrs and nr != "":
                if a_card_nr in cards: cards[a_card_nr] += 1
                else: cards[a_card_nr] = 2
                
                a_card_nr += 1
                cards_total += 1
    # print(cards)
    print(cards_total)



print(f"Total pts: {cards_total}")