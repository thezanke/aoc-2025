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

    cache: dict[tuple[int, int], int] = {}

        
    def solve_recursively(lines: list[list[str]], x, y=0):
        if (x, y) in cache:
            return cache[(x, y)]

        v: int = 0
        if y >= len(lines):
            v += 1
        elif lines[y][x] == "|" or lines[y][x] == "S":
            v += solve_recursively(lines, x, y + 1)
        elif lines[y][x] == "^":
            v += solve_recursively(lines, x - 1, y + 1) + solve_recursively(
                lines, x + 1, y + 1
            )

        cache[(x, y)] = v

        return v

        

    t = solve_recursively(lines, lines[0].index("S"))

    return t


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
    assert solve_part_2(input_final) == 10733529153890
