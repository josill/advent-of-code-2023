file = open("./inputs/day2.txt", "r")
lines = file.readlines()

sum = 0

for line in lines:
    id = line.split(":")[0].split(" ")[1]
    sets = line.split(":")[1].split(";")
    
    max_red = 0
    max_green = 0
    max_blue = 0

    for set in sets:
        for cube in set.split(","):
            cube_amount = cube.split(" ")[1]
            cube_color = cube.split(" ")[2]

            if cube_color.strip() == "blue" and int(cube_amount) > max_blue:
                max_blue = int(cube_amount)
            elif cube_color.strip() == "green" and int(cube_amount) > max_green:
                max_green = int(cube_amount)
            elif cube_color.strip() == "red" and int(cube_amount) > max_red:
                max_red = int(cube_amount)
    
    sum += max_red * max_green * max_blue

print(sum)