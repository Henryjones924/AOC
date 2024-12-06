with open("input.txt") as file:
    data = file.readlines()

line_list = []
max_blue = 14
max_red = 12
max_green = 13
total = 0
# Line Clean Up
for line in data:
    fix_line = line.strip("\n")
    line_list += [fix_line]
# print (line_list)

# Game Logic
for match in line_list:
    match = str(match).split(":")
    game_id_list = match[0]
    game_id_list = game_id_list.split()
    match = match[-1]
    match = str(match).split(";")

    red = False
    blue = False
    green = False
    for rounds in match:
        rounds = str(rounds).split(",")
        # print (rounds)
        for balls in rounds:
            if "green" in str(balls):
                green_balls = balls.split()

                if int(green_balls[0]) > max_green:
                    green = True
                    # print("Green Failed")
                else:
                    pass
            elif "blue" in str(balls):
                blue_balls = balls.split()
                if int(blue_balls[0]) > max_blue:
                    blue = True
                    # print("Blue Failed")
                else:
                    pass
            elif "red" in str(balls):
                red_balls = balls.split()
                if int(red_balls[0]) > max_red:
                    red = True
                    # print("Red Failed")
                else:
                    pass
            else:
                print("Invalid Ball Color")

    if red == True or green == True or blue == True:
        print("failed " + game_id_list[1])
    else:
        print("Sucess " + game_id_list[1])
        total += int(game_id_list[1])
print(total)
