import pytest


def solve_battery_array(arr: list[int]) -> int:
    p1 = 0

    while p1 < len(arr) - 2:
        print(f"p1: {p1}, value: {arr[p1]}")

        if arr[p1] == 9:
            break

        found = False
        for i in range(p1 + 1, len(arr) - 1):
            print(f"i: {i}, value: {arr[i]}")

            if arr[p1] < arr[i]:
                print(f"Found {arr[i]} is larger than {arr[p1]}")
                p1 = i
                found = True
                break

        if not found:
            print("No larger value found for p1, breaking")
            break

    p2 = p1 + 1

    while p2 < len(arr):
        print(f"p2: {p2}, value: {arr[p2]}")

        if arr[p2] == 9:
            break

        found = False
        for i in range(p2 + 1, len(arr)):
            print(f"i: {i}, value: {arr[i]}")

            if arr[p2] < arr[i]:
                print(f"Found {arr[i]} is larger than {arr[p2]}")
                p2 = i
                found = True
                break

        if not found:
            print("No larger value found for p2, breaking")
            break

    return arr[p1] * 10 + arr[p2]


def solve_part_1(input: list[list[int]]) -> int:
    return sum([solve_battery_array(line) for line in input])


def solve_part_2(input: list[list[int]]) -> int:
    pass


###
# UNIT TESTS
###


def parse_line(line):
    return [int(n) for n in list(line)]


def get_input(file_path):
    with open(file_path, "r") as file:
        return [parse_line(line) for line in file.read().split("\n")]


input_example = get_input("day3/example.txt")
input_final = get_input("day3/input.txt")


def test_solve_battery_array():
    assert solve_battery_array([0, 2, 1, 3, 2, 1]) == 32
    assert solve_battery_array([1, 1, 1, 3, 5, 1, 4, 1, 1]) == 54

def test_solve_example():
    assert solve_part_1(input_example) == 357


def test_solve_final():
    assert solve_part_1(input_final) == 17403


@pytest.mark.skip(reason="not implemented")
def test_solve2_example():
    assert solve_part_2(input_example) == False


@pytest.mark.skip(reason="not implemented")
def test_solve2_final():
    assert solve_part_2(input_final) == False
