file = open("./inputs/day6.txt", "r")
lines = file.readlines()

time = [int(c) for c in lines[0].strip().split(":")[1].strip().split(" ") if c != ""]
dist = [int(c) for c in lines[1].strip().split(":")[1].strip().split(" ") if c != ""]

wins_total = 1

for i in range(len(time)):
    nr_of_wins = 0

    for speed in range(time[i]):
        if speed != 0:
            dist_remaining = time[i] - speed
            dist_race = speed * dist_remaining

            if dist_race > dist[i]:
                nr_of_wins += 1

            print(time[i])
            print(f"time {speed}")
            print(f"distance: {dist_race}")

    print(f"nr of wins is: {nr_of_wins}")
    wins_total *= nr_of_wins


print("---")
print(wins_total)
