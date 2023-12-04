file = open("./inputs/day2.txt", "r")
lines = file.readlines()

max_blue = 14
max_green = 13
max_red = 12

possible_games = 0

for line in lines:
    id = line.strip().split(":")[0].split(" ")[1]
    sets = line.strip().split(":")[1].split(";")
    possible_flag = True

    for set in sets:
        for cube in set.split(","):
            cube_amount = cube.split(" ")[1]
            cube_color = cube.split(" ")[2]

            if cube_color == "blue" and int(cube_amount) > max_blue:
                possible_flag = False
            elif cube_color == "green" and int(cube_amount) > max_green:
                possible_flag = False
            elif cube_color == "red" and int(cube_amount) > max_red:
                possible_flag = False

    if possible_flag:
        possible_games += int(id)

print(possible_games)