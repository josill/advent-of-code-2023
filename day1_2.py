file = open("./inputs/day1.txt", "r")
lines = file.readlines()

sum = 0

digits = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

for line in lines:
    chars = ""
    chars_reverse = ""

    first_num_flag = False
    last_num_flag = False

    line_num = ""

    for char in line:
        chars += char
        
        if char.isdigit() and not first_num_flag:
            line_num += str(char)
            first_num_flag = True

        for digit in digits:
            if digit in chars and not first_num_flag:
                line_num += str(digits[digit])
                first_num_flag = True

    for char in reversed(line):
        chars_reverse = char + chars_reverse
        
        if char.isdigit() and not last_num_flag:
            line_num += str(char)
            last_num_flag = True

        for digit in digits:
            if digit in chars_reverse and not last_num_flag:
                line_num += str(digits[digit])
                last_num_flag = True

    sum += int(line_num)

print(sum)
    