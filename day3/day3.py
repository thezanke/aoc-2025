import pytest


def solve_battery_array(arr: list[int], d=2) -> int:
    t = 0

    print(f"Solving for array: {arr}")

    x = 0

    while d > 0:
        while x < len(arr) - d:
            print(f"x[{d}]: {x}, value: {arr[x]}")

            if arr[x] == 9:
                break

            found = False
            for i in range(x + 1, len(arr) - d + 1):
                print(f"i: {i}, value: {arr[i]}")

                if arr[x] < arr[i]:
                    print(f"Found {arr[i]} is larger than {arr[x]}")
                    x = i
                    found = True
                    break

            if not found:
                print("No larger value found for x, breaking")
                break

        t += arr[x] * 10 ** (d - 1)
        d -= 1
        x += 1

        print(f"total: {t}, remaining digits: {d}")

    return t


def solve_part_1(arr_list: list[list[int]]) -> int:
    return sum([solve_battery_array(line) for line in arr_list])


def solve_part_2(arr_list: list[list[int]]) -> int:
    return sum([solve_battery_array(line, 12) for line in arr_list])


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


def test_example_arr_1():
    assert solve_battery_array(input_example[0]) == 98


def test_example_arr_2():
    assert solve_battery_array(input_example[1]) == 89


def test_example_arr_3():
    assert solve_battery_array(input_example[2]) == 78


def test_example_arr_4():
    assert solve_battery_array(input_example[3]) == 92

def test_solve_example():
    assert solve_part_1(input_example) == 357


def test_solve_final():
    assert solve_part_1(input_final) == 17403

def test_example_arr_1_part2():
    assert solve_battery_array(input_example[0], 12) == 987654321111


def test_solve2_example():
    assert solve_part_2(input_example) == 3121910778619


def test_solve2_final():
    assert solve_part_2(input_final) == 173416889848394
