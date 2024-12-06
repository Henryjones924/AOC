import argparse
import sys
import time
from functools import wraps
from typing import Any, Callable, Dict, List, Tuple

import pysnooper
from colorama import Fore, Style, init

init(autoreset=True)

SolutionFunction = Callable[[List[str]], Tuple[str, float]]

DEBUG_MODE = any(arg in sys.argv for arg in ["--debug", "-d", "--example", "-e"])


def performance(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Tuple[Any, float]:
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        return result, end_time - start_time

    return wrapper


def debug(*args: Any, **kwargs: Any) -> Callable:
    if DEBUG_MODE:
        if len(args) == 1 and callable(args[0]):
            return pysnooper.snoop()(args[0])
        else:
            return lambda func: pysnooper.snoop(*args, **kwargs)(func)
    else:
        if len(args) == 1 and callable(args[0]):
            return args[0]
        else:
            return lambda func: func


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="dev_aoc_helper")
    parser.add_argument(
        "-e",
        "--example",
        action="store_true",
        help="run solutions against example data",
    )
    parser.add_argument("-1", "--p1", action="store_true", help="run only Part 1")
    parser.add_argument("-2", "--p2", action="store_true", help="run only Part 2")
    parser.add_argument("-d", "--debug", action="store_true", help="enable debug mode")
    args = parser.parse_args()

    if args.p1 and args.p2:
        print("Error: can only use --p1 or --p2 but not both")
        sys.exit(1)

    return args


def read_input_file(filename: str = "input") -> str:
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Input file '{filename}' not found.")
        sys.exit(1)


def read_example_file(filename: str = "example") -> str:
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Example input file '{filename}' not found.")
        sys.exit(1)


def parse_example_data(example_data: str) -> List[Dict[str, Any]]:
    examples = []
    current_example = {"data": [], "answer_a": None, "answer_b": None}

    for line in example_data.splitlines():
        line = line.strip()
        if line.startswith("https://") or not line or line.startswith("---"):
            continue
        if line.startswith("answer_a:"):
            current_example["answer_a"] = line.split("answer_a:")[1].strip()
        elif line.startswith("answer_b:"):
            current_example["answer_b"] = line.split("answer_b:")[1].strip()
            current_example["data"] = "\n".join(current_example["data"])
            examples.append(current_example)
            current_example = {"data": [], "answer_a": None, "answer_b": None}
        else:
            current_example["data"].append(line)

    return examples


def print_example_input_and_answer(
    input_data: List[str], expected_answer: str, part_label: str
) -> None:
    print(f"\nExample input:\n{Fore.YELLOW}{input_data}{Style.RESET_ALL}")
    if expected_answer != "-":
        print(
            f"Expected answer for {part_label}: {Fore.YELLOW}{expected_answer}{Style.RESET_ALL}"
        )


def print_example(
    solution_func: SolutionFunction,
    input_data: List[str],
    expected_answer: str,
    part_label: str,
) -> None:
    result, time_taken = solution_func(input_data)
    if result != "null":
        print_example_input_and_answer(input_data, expected_answer, part_label)
        print("--------------------------------")
        print_solution_result(result, expected_answer, time_taken, part_label)


def run_example_solutions(
    solution_p1: SolutionFunction,
    solution_p2: SolutionFunction,
    args: argparse.Namespace,
) -> None:
    example_lines = read_example_file()
    examples = parse_example_data(example_lines)

    for example in examples:
        input_data = example["data"]

        if example["answer_a"] != "-" and (args.p1 or not args.p2):
            print_example(solution_p1, input_data, example["answer_a"], "Part 1")

        if example["answer_b"] != "-" and (args.p2 or not args.p1):
            print_example(solution_p2, input_data, example["answer_b"], "Part 2")


def run_solutions(
    solution_p1: SolutionFunction,
    solution_p2: SolutionFunction,
    args: argparse.Namespace,
) -> None:
    data = read_input_file()

    if args.p1 or not args.p2:
        result_p1, time_p1 = solution_p1(data)
        if result_p1 != "null":
            print_solution_result(result_p1, "-", time_p1, "Part 1")

    if args.p2 or not args.p1:
        result_p2, time_p2 = solution_p2(data)
        if result_p2 != "null":
            print_solution_result(result_p2, "-", time_p2, "Part 2")


def print_example_result(result: str, expected_result: str) -> None:
    if str(result) == expected_result:
        print(Fore.GREEN + f"Result: {result} (matches expected result)")
    else:
        print(
            Fore.RED
            + f"Result: {result} (does not match expected result: {expected_result})"
        )


def print_solution_result(
    result: str, expected_result: str, time_taken: float, part_label: str
) -> None:
    print(f"Running {part_label} Solution:")
    if result != "null":
        print(f"{part_label} Result: {Fore.GREEN}{result}{Style.RESET_ALL}")
        print(
            f"Execution time for {part_label}: {Fore.GREEN}{time_taken:.6f}{Style.RESET_ALL} seconds"
        )
        if expected_result != "-":
            print_example_result(result, expected_result)
    print("\n")

