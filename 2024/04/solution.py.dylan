import helper as helper


def is_valid_position(grid: list[str], r: int, c: int) -> bool:
    rows, cols = len(grid), len(grid[0])
    return 0 <= r < rows and 0 <= c < cols


def search_word(grid: list[str], word: str, start_r: int, start_c: int, dr: int, dc: int) -> list[tuple[int, int]]:
    positions = []
    for i, char in enumerate(word):
        new_r, new_c = start_r + dr * i, start_c + dc * i
        if not is_valid_position(grid, new_r, new_c) or grid[new_r][new_c] != char:
            return []
        positions.append((new_r, new_c))
    return positions


def find_xmas(grid: list[str], word: str) -> tuple[int, str]:
    directions = [
        (0, 1),  # right
        (1, 0),  # down
        (1, 1),  # diagonal down-right
        (1, -1),  # diagonal down-left
        (0, -1),  # left
        (-1, 0),  # up
        (-1, -1),  # diagonal up-left
        (-1, 1),  # diagonal up-right
    ]
    word_positions = set()
    count = 0
    rows, cols = len(grid), len(grid[0])

    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                positions = search_word(grid, word, r, c, dr, dc)
                if positions:
                    count += 1
                    word_positions.update(positions)

    stripped_grid = []
    for r in range(len(grid)):
        stripped_grid.append("".join(grid[r][c] if (r, c) in word_positions else "." for c in range(len(grid[0]))))

    return count, "\n".join(stripped_grid)


def mas_pattern(letters: list[str]) -> bool:
    return letters == ["M", "A", "S"] or letters == ["S", "A", "M"]


def find_xmas_patterns(grid: list[str]) -> tuple[int, str]:
    word_positions = set()
    count = 0
    rows, cols = len(grid), len(grid[0])

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != "A":
                continue

            # up-left -> bottom-right
            diagonal_one = [(r - 1, c - 1), (r, c), (r + 1, c + 1)]
            if all(is_valid_position(grid, pos[0], pos[1]) for pos in diagonal_one):
                diagonal_one_letters = [grid[pos[0]][pos[1]] for pos in diagonal_one]
                valid_diagonal_one = mas_pattern(diagonal_one_letters) or mas_pattern(diagonal_one_letters[::-1])
            else:
                valid_diagonal_one = False

            # up-right -> bottom-left
            diagonal_two = [(r - 1, c + 1), (r, c), (r + 1, c - 1)]
            if all(is_valid_position(grid, pos[0], pos[1]) for pos in diagonal_two):
                diagonal_two_letters = [grid[pos[0]][pos[1]] for pos in diagonal_two]
                valid_diagonal_two = mas_pattern(diagonal_two_letters) or mas_pattern(diagonal_two_letters[::-1])
            else:
                valid_diagonal_two = False

            if valid_diagonal_one and valid_diagonal_two:
                count += 1
                word_positions.update(diagonal_one)
                word_positions.update(diagonal_two)

    stripped_grid = []
    for r in range(rows):
        line = ""
        for c in range(cols):
            if (r, c) in word_positions:
                line += grid[r][c]
            else:
                line += "."
        stripped_grid.append(line)
    return count, "\n".join(stripped_grid)


@helper.performance
@helper.debug
def solution_p1(data):
    grid = [line.strip() for line in data.splitlines()]
    word = "XMAS"
    count, stripped_grid = find_xmas(grid, word)
    print(stripped_grid)
    print("Type" + str(type(count)))
    return count


@helper.performance
@helper.debug
def solution_p2(data):
    # input = input_clean("projects/aoc_2024/2024/day1/day1.1_example")
    input = input_clean(data)
    # print(input)
    group0 = []
    group1 = []
    for group in input:
        group0 += [group[0]]
        group1 += [group[1]]
    # print(group0)
    group0 = sorted(group0)
    group1 = sorted(group1)
    # print(group0)

    i = 0
    score = 0
    while i < len(group0):
        for cord in group0:
            # print(cord)
            count = group1.count(cord)
            score += int(count) * int(cord)
            # print(count)
            i += 1
    return str(score)


if __name__ == "__main__":
    args = helper.parse_arguments()
    if args.example:
        helper.run_example_solutions(solution_p1, solution_p2, args)
    else:
        helper.run_solutions(solution_p1, solution_p2, args)
