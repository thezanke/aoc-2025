import pytest


def solve_part_1(coord_list: list[tuple[int, int]]):
    neighbor_distances = {}
    for i, a in enumerate(coord_list):
        for j, b in enumerate(coord_list):
            if i == j:
                continue

            if (b, a) in neighbor_distances:
                continue

            dist = abs(a[0] - b[0]) + abs(a[1] - b[1])
            neighbor_distances[(a, b)] = dist

    sorted_distances = sorted(neighbor_distances.items(), key=lambda item: item[1])
    (p1, p2), _ = sorted_distances[-1]
    return (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)


def solve_part_2(coord_list: list[tuple[int, int]]):
    pass


###
# UNIT TESTS
###


def parse_input(line: str) -> tuple[int, int]:
    return tuple(int(i) for i in line.split(","))


def get_input(file_path):
    with open(file_path, "r") as file:
        coord_list = [parse_input(line) for line in file.read().splitlines()]
        return coord_list


def test_part_1_example_solution():
    input_example = get_input("day9/example.txt")
    assert solve_part_1(input_example) == 50


def test_part_1_final_solution():
    input_final = get_input("day9/input.txt")
    assert solve_part_1(input_final) == 4725826296


def test_part_2_example_solution():
    input_example = get_input("day9/example.txt")
    assert solve_part_2(input_example) == 24


@pytest.mark.skip(reason="Not implemented yet")
def test_part_2_final_solution():
    input_final = get_input("day9/input.txt")
    assert solve_part_2(input_final) == 1
