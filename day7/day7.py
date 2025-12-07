import itertools
import pytest


def solve_part_1(lines: list[list[str]]) -> int:
    t = 0

    for a, b in itertools.pairwise(lines):
        for ii in range(len(a)):
            if a[ii] == "S" or a[ii] == "|":
                if b[ii] == "^":
                    if b[ii - 1] == ".":
                        b[ii - 1] = "|"
                    if b[ii + 1] == ".":
                        b[ii + 1] = "|"
                    t += 1
                else:
                    b[ii] = "|"
    return t


def print_lines(lines: list[list[str]]):
    for line in lines:
        print("".join(line))
    print()


def solve_part_2(lines: list[list[str]]) -> int:
    for a, b in itertools.pairwise(lines):
        for ii in range(len(a)):
            if a[ii] == "S" or a[ii] == "|":
                if b[ii] == "^":
                    if b[ii - 1] == ".":
                        b[ii - 1] = "|"
                    if b[ii + 1] == ".":
                        b[ii + 1] = "|"
                else:
                    b[ii] = "|"

    def solve_recursively(lines: list[list[str]], ret, li, pos):
        if pos == -1 or pos == len(lines[li]) or lines[li][pos] != "|":
            return 0

        if li + 2 == len(lines):
            return 1


        return solve_recursively(lines, ret, li + 1, pos - 1) + solve_recursively(
            lines, ret, li + 1, pos + 1
        )

    filtered = [line for line in lines if not any(c == "^" for c in line)]
    header = filtered.pop(0)

    return solve_recursively(filtered, {"total": 0}, 0, header.index("S"))


###
# UNIT TESTS
###


def get_input(file_path):
    with open(file_path, "r") as file:
        return [list(line) for line in file.read().splitlines()]


def test_part_1_example_solution():
    input_example = get_input("day7/example.txt")
    assert solve_part_1(input_example) == 21


def test_part_1_final_solution():
    input_final = get_input("day7/input.txt")
    assert solve_part_1(input_final) == 1533


def test_part_2_example_solution():
    input_example = get_input("day7/example.txt")
    assert solve_part_2(input_example) == 40


def test_part_2_final_solution():
    input_final = get_input("day7/input.txt")
    assert solve_part_2(input_final) == 40
