file = open("./inputs/day3.txt", "r")
lines = file.readlines()

f_part_flag = False
s_part_flag = False
active_flag = False
rows_since_active_flag = 0

part_nums = 0
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
                    
                    if s == "*":
                        if not f_part_flag:
                            print(cl + "-----")
                            part_nums = int(cl)
                            f_part_flag = True
                            rows_since_active_flag = 3
                        elif not s_part_flag:
                            print(cl + "-----")
                            part_nums *= int(cl)
                            s_part_flag = True

            for j2 in range(2):
                if j2 == 0:
                    if line[si-1] == "*":
                        if not f_part_flag:
                            print(cl)
                            part_nums = int(cl)
                            f_part_flag = True
                            rows_since_active_flag = 2
                        elif not s_part_flag:
                            print(cl)
                            part_nums *= int(cl)
                            s_part_flag = True
                else:
                    if line[ei] == "*":
                        if not f_part_flag:
                            print(cl)
                            part_nums = int(cl)
                            f_part_flag = True
                            rows_since_active_flag = 2
                        elif not s_part_flag:
                            print(cl)
                            part_nums *= int(cl)
                            s_part_flag = True

            if i != len(lines) - 1:
                for j3 in range(len(cl) + 2):
                    s = lines[i+1][si+j3-1]

                    if s == "*":
                        if not f_part_flag:
                            print("-----" + cl)
                            part_nums = int(cl)
                            f_part_flag = True
                            rows_since_active_flag = 1
                        elif not s_part_flag:
                            print("-----" + cl)
                            part_nums *= int(cl)
                            s_part_flag = True


            cl = ""
    if rows_since_active_flag > 3:
        part_nums = 0
        f_part_flag = False
    
    rows_since_active_flag += 1

    if f_part_flag and s_part_flag:
        print(f"Part nums: {part_nums}")
        sum += part_nums
        print(f"Sum: {sum}")
        part_nums = 0
        f_part_flag = False
        s_part_flag = False

print(sum)