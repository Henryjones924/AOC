import re

import helper as helper


@helper.performance
# @helper.debug
def solution_p1(data):
    input = str(data)
    mul_found = re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)", input)
    mul_total = 0
    for mul in mul_found:
        mul_sets = re.findall(r"[0-9]{1,3},[0-9]{1,3}", mul)
        mul_values = re.split(r",", mul_sets[0])
        mul_total += int(mul_values[0]) * int(mul_values[1])
    return mul_total


@helper.performance
# @helper.debug
def solution_p2(data):
    input = str(data)
    mul_found = re.findall(r"(mul\([0-9]{1,3},[0-9]{1,3}\))|(don't\(\))|(do\(\))", input)
    dont = True
    mul_total = 0
    for item in mul_found:
        if item[1]:
            dont = False
        elif item[2]:
            dont = True
        elif item[0] and dont:
            mul_sets = re.findall(r"[0-9]{1,3},[0-9]{1,3}", item[0])
            mul_values = re.split(r",", mul_sets[0])
            mul_total += int(mul_values[0]) * int(mul_values[1])
            dont = True

    return str(mul_total)


if __name__ == "__main__":
    args = helper.parse_arguments()
    if args.example:
        helper.run_example_solutions(solution_p1, solution_p2, args)
    else:
        helper.run_solutions(solution_p1, solution_p2, args)
