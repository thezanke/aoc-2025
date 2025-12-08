import itertools

import pytest


def solve_part_1(lines: list[list[str]]) -> int:
    t = 0
    return t


def solve_part_2(lines: list[list[str]]) -> int:
    t = 0
    return t


###
# UNIT TESTS
###


def parse_input(lines: list[list[str]]) -> list[list[str]]:
    return lines


def get_input(file_path):
    with open(file_path, "r") as file:
        lines = [[int(i) for i in line.split(",")] for line in file.read().splitlines()]
        return parse_input(lines)


def test_part_1_example_solution():
    input_example = get_input("day8/example.txt")
    assert solve_part_1(input_example) == 40


@pytest.mark.skip(reason="Not implemented")
def test_part_1_final_solution():
    input_final = get_input("day8/input.txt")
    assert solve_part_1(input_final) == 1


@pytest.mark.skip(reason="Not implemented")
def test_part_2_example_solution():
    input_example = get_input("day8/example.txt")
    assert solve_part_2(input_example) == 1


@pytest.mark.skip(reason="Not implemented")
def test_part_2_final_solution():
    input_final = get_input("day8/input.txt")
    assert solve_part_2(input_final) == 1
