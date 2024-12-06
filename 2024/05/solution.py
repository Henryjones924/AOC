import helper as helper


def extract_rules_and_updates(data):
    rules = []
    updates = []
    clean_list = [line.strip() for line in data.splitlines()]
    for line in clean_list:
        rule = []
        update = []
        if len(line) == 5:
            rule += line.split("|")
            rules.append(rule)
        else:
            update += line.split(",")
            if len(update) > 1:
                updates.append(update)
            print(update)
    return rules, updates


def rule_checker(update, rules):
    for a, b in rules:
        a_index = False
        b_index = False
        if a in update:
            a_index = update.index(a)
        if b in update:
            b_index = update.index(b)

        # print(a_index)
        if a_index is False or b_index is False:
            pass
        elif a_index < b_index:
            pass
        else:
            return False
    print(update)
    middle_index = (len(update)) // 2
    middle = update[middle_index]
    print(middle)
    return int(middle)


@helper.performance
@helper.debug
def solution_p1(data):
    total = 0
    rules, updates = extract_rules_and_updates(data)

    for update in updates:
        valid = rule_checker(update, rules)

        if valid is False:
            pass
        else:
            total += valid
    return total


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
