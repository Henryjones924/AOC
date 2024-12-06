import helper as helper
import numpy as np


def input_clean(data):
    clean_list = [line.strip() for line in data.splitlines()]
    return clean_list


def create_wordsearch_array(puzzle_input):
    x = 0
    y = 0
    wordsearch = []
    x1 = len(puzzle_input)
    y1 = len(puzzle_input[0])

    wordsearch = np.empty((x1, y1), dtype=str)
    for line in puzzle_input:
        for letter in line:
            wordsearch[y, x] = letter
            x += 1
        x = 0
        y += 1
    return wordsearch


def word_finder(y, x, wordsearch):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    len_x = len(wordsearch)
    len_y = len(wordsearch[0])
    count = 0
    for x1, y1 in directions:
        row = 0
        col = 0
        row = x1 + x
        col = y1 + y
        if (row >= 0 and col >= 0 and row <= len_x - 1 and col <= len_y - 1) and ("M" == wordsearch[col][row]):
            row = row + x1
            col = col + y1
            if (row >= 0 and col >= 0 and row <= len_x - 1 and col <= len_y - 1) and ("A" == wordsearch[col][row]):
                row = row + x1
                col = col + y1
                if (row >= 0 and col >= 0 and row <= len_x - 1 and col <= len_y - 1) and ("S" == wordsearch[col][row]):
                    row = row + x1
                    col = col + y1
                    count += 1
        else:
            pass

        row = 0
        col = 0
    return count


@helper.performance
#@helper.debug
def solution_p1(data):
    # find_word = "XMAS"
    raw_puzzle = input_clean(data)
    wordsearch = create_wordsearch_array(raw_puzzle)
    x = 0
    y = 0
    result_list = 0
    for row in wordsearch:
        x = 0
        for letter in row:
            if "X" == letter:
                result_list = word_finder(y, x, wordsearch) + result_list
            x += 1
        y += 1
    return result_list


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
