import pytest


def get_neighbors(grid: list[list[str]], pos: tuple[int, int]):
    neighbors = []
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for dr, dc in directions:
        r, c = pos[0] + dr, pos[1] + dc
        if 0 <= r < rows and 0 <= c < cols:
            if grid[r][c] == "@":
                neighbors.append((r, c))

    return neighbors


def solve_part_1(arr_list: list[list[int]]) -> int:
    t = 0
    for r in range(len(arr_list)):
        for c in range(len(arr_list[0])):
            if arr_list[r][c] != "@":
                continue
            pos = (r, c)
            neighbors = get_neighbors(arr_list, pos)
            if len(neighbors) < 4:
                t += 1
            print("Position:", pos)
            print(neighbors)
    return t


def solve_part_2(arr_list: list[list[int]]) -> int:
    pass


###
# UNIT TESTS
###


def parse_line(line):
    return [c for c in line]


def get_input(file_path):
    with open(file_path, "r") as file:
        return [parse_line(line) for line in file.read().split("\n")]


input_example = get_input("day4/example.txt")
input_final = get_input("day4/input.txt")


def test_part_1_example_solution():
    assert solve_part_1(input_example) == 13


def test_part_1_final_solution():
    assert solve_part_1(input_final) == 1411


@pytest.mark.skip(reason="not implemented")
def test_part_2_example_solution():
    assert solve_part_2(input_example) == False


@pytest.mark.skip(reason="not implemented")
def test_part_2_final_solution():
    assert solve_part_2(input_final) == False
