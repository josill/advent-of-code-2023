file = open("./inputs/day4.txt", "r")
lines = file.readlines()

pts = 0

for line in lines:
    data = line.split(":")[1]

    win_nrs = data.split("|")[0].strip().split(" ")
    scratch_nrs = data.split("|")[1].strip().split(" ")

    l_pts = 0

    print(win_nrs)
    print(scratch_nrs)

    for nr in scratch_nrs:
        if nr.strip() in win_nrs and nr != "":
            print(nr.strip())
            if l_pts == 0: l_pts = 1
            else: l_pts *= 2

    pts += l_pts 
    
print(f"Total pts: {pts}")