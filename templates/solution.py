import helper as helper


@helper.performance
@helper.debug
def solution_p1(data):
    return "null"


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

