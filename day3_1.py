file = open("./inputs/day3.txt", "r")
lines = file.readlines()

symbols = ["*", "#", "+", "$"]

sum = 0

for i, line in enumerate(lines):
    cl = ""
    
    for j, c in enumerate(line):
        if c.isdigit():
            cl += c
        elif cl != "":
            si = j - len(cl)
            ei = j

            if i != 0:
                for j1 in range(len(cl) + 2):
                    s = lines[i-1][si+j1-1]
                    
                    if s in symbols:
                        sum += int(cl)

            for j2 in range(2):
                if j2 == 0:
                    if line[si-1] in symbols:
                        sum += int(cl)
                else:
                    if line[ei] in symbols:
                        sum += int(cl)

            if i != len(lines) - 1:
                for j3 in range(len(cl) + 2):
                    s = lines[i+1][si+j3-1]

                    if s in symbols:
                        sum += int(cl)


            cl = ""

print(sum)