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


def area_is_contained(
    a: tuple[int, int],
    b: tuple[int, int],
    vertical_lines: list[tuple[int, int, int]],
    horizontal_lines: list[tuple[int, int, int]],
):
    min_x = min(a[0], b[0])
    max_x = max(a[0], b[0])
    min_y = min(a[1], b[1])
    max_y = max(a[1], b[1])

    for x, y1, y2 in vertical_lines:
        if min_x < x < max_x:
            if y2 <= min_y or y1 >= max_y:
                continue
            return False

    for y, x1, x2 in horizontal_lines:
        if min_y < y < max_y:
            if x2 <= min_x or x1 >= max_x:
                continue
            return False

    return True


def build_polygon_lines(corners: list[tuple[int, int]]):
    if len(corners) < 2:
        return []

    lines = []
    for i, a in enumerate(corners):
        b = corners[(i + 1) % len(corners)]
        if a[0] != b[0] and a[1] != b[1]:
            raise ValueError("Non axis-aligned corner pair detected")
        lines.append((a, b))

    return lines


def split_segments(lines: list[tuple[int, int]]):
    vertical_segments = []
    horizontal_segments = []

    for a, b in lines:
        if a[0] == b[0]:
            y1, y2 = sorted((a[1], b[1]))
            vertical_segments.append((a[0], y1, y2))
        else:
            x1, x2 = sorted((a[0], b[0]))
            horizontal_segments.append((a[1], x1, x2))

    return vertical_segments, horizontal_segments


def solve_part_2(corners: list[tuple[int, int]]):
    lines = build_polygon_lines(corners)
    vertical_segments, horizontal_segments = split_segments(lines)
    best_area = 0

    for i, a in enumerate(corners):
        for j in range(i + 1, len(corners)):
            b = corners[j]
            candidate_area = (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)
            if candidate_area <= best_area:
                continue
            if not area_is_contained(a, b, vertical_segments, horizontal_segments):
                continue
            best_area = candidate_area

    return best_area


###
# UNIT TESTS
###


def parse_input(line: str) -> tuple[int, int]:
    return tuple(int(i) for i in line.split(","))


def get_input(file_path):
    with open(file_path, "r") as file:
        return [parse_input(line) for line in file.read().splitlines()]


def test_part_1_example_solution():
    input_example = get_input("day9/example.txt")
    assert solve_part_1(input_example) == 50


def test_part_1_final_solution():
    input_final = get_input("day9/input.txt")
    assert solve_part_1(input_final) == 4725826296


def test_part_2_example_solution():
    input_example = get_input("day9/example.txt")
    assert solve_part_2(input_example) == 24


def test_part_2_final_solution():
    input_final = get_input("day9/input.txt")
    assert solve_part_2(input_final) == 1637556834
