import itertools

import pytest


def build_neighbor_distances(
    coord_list: list[tuple[int, int, int]],
):
    neighbor_distances = {}

    for coord in coord_list:
        for other_coord in coord_list:
            if other_coord == coord:
                continue

            if (other_coord, coord) in neighbor_distances:
                continue

            neighbor_distances[(coord, other_coord)] = (
                (coord[0] - other_coord[0]) ** 2
                + (coord[1] - other_coord[1]) ** 2
                + (coord[2] - other_coord[2]) ** 2
            ) ** 0.5

    return dict(
        sorted(neighbor_distances.items(), key=lambda item: item[1], reverse=True)
    )


def build_circuits(coord_list: list[tuple[int, int, int]], limit: int):
    neighbor_distances = build_neighbor_distances(coord_list)
    circuits = [{coord} for coord in coord_list]
    connections = 0
    coord_a = None
    coord_b = None

    while len(neighbor_distances) > 0:
        if limit != 0 and connections == limit:
            break

        if len(circuits) == 1:
            break

        (coord_a, coord_b), _ = neighbor_distances.popitem()
        connections += 1

        found_circuit_a = None
        found_circuit_b = None

        for circuit in circuits:
            if coord_a in circuit:
                found_circuit_a = circuit
            if coord_b in circuit:
                found_circuit_b = circuit

        if found_circuit_a == found_circuit_b:
            continue

        found_circuit_a.update(found_circuit_b)
        circuits.remove(found_circuit_b)

    return circuits, coord_a, coord_b


def solve_part_1(coord_list: list[tuple[int, int, int]], limit=0):
    circuits, _, _ = build_circuits(coord_list, limit=limit)

    for i, circuit in enumerate(circuits):
        print(f"Circuit {i}:")
        for coord in circuit:
            print(f"  {coord}")

    circuits = sorted(circuits, key=lambda c: len(c), reverse=True)
    top3 = circuits[:3]

    return len(top3[0]) * len(top3[1]) * len(top3[2])


def solve_part_2(coord_list: list[tuple[int, int, int]], limit=0):
    _, coord_a, coord_b = build_circuits(coord_list, limit=limit)

    print(f"Last connected coordinates: {coord_a}, {coord_b}")

    return coord_a[0] * coord_b[0]


###
# UNIT TESTS
###


def parse_input(line: str) -> tuple[int, int, int]:
    return tuple([int(i) for i in line.split(",")])


def get_input(file_path):
    with open(file_path, "r") as file:
        coord_list = [parse_input(line) for line in file.read().splitlines()]
        return coord_list


def test_part_1_example_solution():
    input_example = get_input("day8/example.txt")
    assert solve_part_1(input_example, limit=10) == 40


def test_part_1_final_solution():
    input_final = get_input("day8/input.txt")
    assert solve_part_1(input_final, limit=1000) == 42840


def test_part_2_example_solution():
    input_example = get_input("day8/example.txt")
    assert solve_part_2(input_example) == 25272


def test_part_2_final_solution():
    input_final = get_input("day8/input.txt")
    assert solve_part_2(input_final) == 170629052
