import helper as helper


def input_clean(data):
    clean_data = [line.strip() for line in data.splitlines()]
    clean_list = []
    for line in clean_data:
        clean_line = line.split("   ")
        clean_list += [clean_line]
    return clean_list


@helper.performance
@helper.debug
def solution_p1(data):
    input = input_clean(data)
    print(input)
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
    distance = 0
    while i < len(group0):
        distance += abs(int(group1[i]) - int(group0[i]))
        # print(distance)
        i += 1

    return str(distance)


@helper.performance
#@helper.debug
def solution_p2(data):
    input = input_clean(data)

    group0 = []
    group1 = []
    for group in input:
        group0 += [group[0]]
        group1 += [group[1]]
    group0 = sorted(group0)
    group1 = sorted(group1)

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
