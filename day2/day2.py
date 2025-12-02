import re
from typing import List
import pytest


def solve(input: List[str]):
    t = 0
    for entry in input:
        [n, max_n] = map(int, entry.split("-"))
        while n <= max_n:
            match = re.match(r"^(\d+)\1$", str(n))
            if match is not None:
                t += n
            n += 1

    return t


def solve2(input: List[str]):
    t = 0
    for entry in input:
        [n, max_n] = map(int, entry.split("-"))
        while n <= max_n:
            match = re.match(r"^(\d+)\1+$", str(n))
            if match is not None:
                t += n
            n += 1

    return t


def get_input(file_path):
    with open(file_path, "r") as file:
        return file.read().strip().split(",")


input_example = get_input("day2/example.txt")
input_final = get_input("day2/input.txt")


def test_solve_example():
    assert solve(input_example) == 1227775554


@pytest.mark.skip(reason="takes too long")
def test_solve_final():
    assert solve(input_final) == 28844599675


def test_solve2_example():
    assert solve2(input_example) == 4174379265


@pytest.mark.skip(reason="takes too long")
def test_solve2_final():
    assert solve2(input_final) == 48778605167
