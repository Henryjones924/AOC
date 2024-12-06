with open("input.txt") as file:
    data = file.readlines()

line_list = []
total = 0
# Line Clean Up
for line in data:
    fix_line = line.strip("\n")
    line_list += [fix_line]
# print (line_list)
blue = []
red = []
green = []
redmax = []
bluemax = []
greenmax = []
# Game Logic
for match in line_list:
    match = str(match).split(":")
    game_id_list = match[0]
    game_id_list = game_id_list.split()
    match = match[-1]
    match = str(match).split(";")
    red.clear()
    green.clear()
    blue.clear()
    # print (match)
    for rounds in match:
        rounds = str(rounds).split(",")
        for cube in rounds:
            # print (cube)

            if "blue" in cube:
                cube = cube.split()
                cubetotal = cube[0]
                blue.append(int(cubetotal))
                bluemax = max(blue)

            elif "green" in cube:
                cube = cube.split()
                cubetotal = cube[0]
                green.append(int(cubetotal))
                greenmax = max(green)

            elif "red" in cube:
                cube = cube.split()
                cubetotal = cube[0]
                red.append(int(cubetotal))
                redmax = max(red)

    total_cubes = bluemax * redmax * greenmax
    total += total_cubes
print(total)
