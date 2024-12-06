import helper as helper


def input_clean(data):
    clean_data = [line.strip() for line in data.splitlines()]
    clean_data = [line.split() for line in clean_data]
    return clean_data


@helper.performance
# @helper.debug
def solution_p1(data):
    safe_reports = 0
    report_list = input_clean(data)
    for report in report_list:
        if (
            all(int(a) > int(b) for a, b in zip(report, report[1:]))
            or all(int(a) < int(b) for a, b in zip(report, report[1:]))
        ) and all(abs(int(a) - int(b)) <= 3 for a, b in zip(report, report[1:])):
            safe_reports += 1
        else:
            # print(report)
            pass
    return safe_reports


@helper.performance
# @helper.debug
def solution_p2(data):
    safe_reports = 0
    report_list = input_clean(data)
    for report in report_list:
        index = 0
        if (
            all(int(a) > int(b) for a, b in zip(report, report[1:]))
            or all(int(a) < int(b) for a, b in zip(report, report[1:]))
        ) and all(abs(int(a) - int(b)) <= 3 for a, b in zip(report, report[1:])):
            safe_reports += 1
        else:
            while index < len(report):
                copy_report = report.copy()
                copy_report.pop(index)
                if (
                    all(int(a) > int(b) for a, b in zip(copy_report, copy_report[1:]))
                    or all(int(a) < int(b) for a, b in zip(copy_report, copy_report[1:]))
                ) and all(abs(int(a) - int(b)) <= 3 for a, b in zip(copy_report, copy_report[1:])):
                    safe_reports += 1
                    break
                else:
                    index += 1
                    pass
    return safe_reports


if __name__ == "__main__":
    args = helper.parse_arguments()
    if args.example:
        helper.run_example_solutions(solution_p1, solution_p2, args)
    else:
        helper.run_solutions(solution_p1, solution_p2, args)
