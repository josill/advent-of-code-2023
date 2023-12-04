file = open("./inputs/day1.txt", "r")
lines = file.readlines()

sum = 0

for line in lines:
    first_char = ""
    last_char = ""

    for char in line:
        if char.isdigit():
            if first_char == "": first_char = char
            else: last_char = char

    sum += int(first_char + first_char) if last_char == "" else int(first_char + last_char)

print(sum)
    