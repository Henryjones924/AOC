import helper as helper
import numpy as np

directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}


def create_grid(data):
    data = [line.strip() for line in data.splitlines()]
    x = 0
    y = 0
    x1 = len(data)
    y1 = len(data[0])

    grid = np.empty((x1, y1), dtype=str)
    for line in data:
        for object in line:
            grid[y, x] = object
            x += 1
        x = 0
        y += 1
    return grid


def turn_right(current_direction):
    # current_direction = directions[current_direction]

    if current_direction == directions["up"]:
        return directions["right"]
    elif current_direction == directions["right"]:
        return directions["down"]
    elif current_direction == directions["down"]:
        return directions["left"]
    elif current_direction == directions["left"]:
        return directions["up"]
    else:
        print("No valid turn")


def locate_start(grid):
    for col_index, col in enumerate(grid):
        for row_index, item in enumerate(col):
            if item == "^":
                start_cord = (col_index, row_index)
                return start_cord
            else:
                pass


def check_for_obstructions(current_cords, current_direction, grid):
    result = tuple(a + b for a, b in zip(current_cords, current_direction))
    if check_boundary(result, grid):
        col = result[0]
        row = result[1]
        if grid[col][row] == "." or grid[col][row] == "^":
            return True
        elif grid[col][row] == "#":
            return False
        else:
            print("Not valid in Check for Obstructions")
    # print(result)


def check_boundary(position, grid):
    check_col = position[0]
    check_row = position[1]
    if 0 <= check_col < len(grid) and 0 <= check_row < len(grid[check_col]):
        return True
    else:
        return False


def mark_x(past_cords, grid):
    for cords in past_cords:
        col = cords[0]
        row = cords[1]
        grid[col][row] = "X"
    return grid


@helper.performance
# @helper.debug
def solution_p1(data):
    grid = create_grid(data)
    direction = (-1, 0)  # Starting direction up
    current_cords = locate_start(grid)  # Starting cords
    pastcords = set()
    pastcords.add(current_cords)
    while True:
        safe = check_for_obstructions(current_cords, direction, grid)
        if safe is True:
            current_cords = tuple(a + b for a, b in zip(current_cords, direction))
            pastcords.add(current_cords)
        elif safe is False:
            direction = turn_right(direction)
        else:
            x = mark_x(pastcords, grid)
            print(x)
            count = len(pastcords)
            return count


@helper.performance
@helper.debug
def solution_p2(data):
    return "null"


if __name__ == "__main__":
    args = helper.parse_arguments()
    if args.example:
        helper.run_example_solutions(solution_p1, solution_p2, args)
    else:
        helper.run_solutions(solution_p1, solution_p2, args)
