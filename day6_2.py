file = open("./inputs/day6.txt", "r")
lines = file.readlines()

file = open("./inputs/day6.txt", "r")
lines = file.readlines()

time = int("".join([c for c in lines[0].strip().split(":")[1].strip().split(" ") if c != ""]))
dist = int("".join([c for c in lines[1].strip().split(":")[1].strip().split(" ") if c != ""]))

wins_total = 0

for speed in range(time):
    if speed != 0:
        dist_remaining = time - speed
        dist_race = speed * dist_remaining

        if dist_race > dist:
            wins_total += 1
        
print("---")
print(wins_total)
