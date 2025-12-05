import pytest


def solve_part_1(puzzle_input: tuple[list[range], list[int]]) -> int:
    [ranges, ingredients] = puzzle_input

    t = 0

    for ingredient in ingredients:
        for r in ranges:
            if ingredient in r:
                t += 1
                break
    return t


def solve_part_2(puzzle_input: tuple[list[range], list[int]]) -> int:
    [ranges, _] = puzzle_input

    combined = []

    for r in sorted(ranges, key=lambda x: x.start):
        if not combined or r.start > combined[-1].stop:
            combined.append(r)
        else:
            combined[-1] = range(combined[-1].start, max(combined[-1].stop, r.stop))

    return sum(map(len, combined))


###
# UNIT TESTS
###


def parse_range(line: str):
    [start, end] = line.split("-")
    return range(int(start), int(end) + 1)


def get_input(file_path):
    with open(file_path, "r") as file:
        [head, tail] = file.read().strip().split("\n\n")
        ranges = [parse_range(x) for x in head.split("\n")]
        ingredients = [int(x) for x in tail.split("\n")]

        return [ranges, ingredients]

input_example = get_input("day5/example.txt")
input_final = get_input("day5/input.txt")

def test_part_1_example_solution():
    assert solve_part_1(input_example) == 3


def test_part_1_final_solution():
    assert solve_part_1(input_final) == 635


def test_part_2_example_solution():
    assert solve_part_2(input_example) == 14


def test_part_2_final_solution():
    assert solve_part_2(input_final) == 369761800782619
