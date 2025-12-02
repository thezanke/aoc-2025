def solve(input_lines, start=50, length=100):
    curr = start
    z = 0

    for line in input_lines:
        direction, chng = line[0], int(line[1:])

        if direction == "L":
            chng = -chng

        curr = ((curr + chng) % length + length) % length
        if curr == 0:
            z += 1

    return z


def solve2(input_lines, start=50, length=100):
    curr = start
    z = 0

    for line in input_lines:
        direction, chng = line[0], int(line[1:])
        dist = (curr if direction == "L" else length - curr) or length

        if chng >= dist:
            z += 1 + ((chng - dist) // length)

        if direction == "L":
            chng = -chng

        curr = ((curr + chng) % length + length) % length

    return z


def get_input(file_path):
    with open(file_path, "r") as file:
        return file.readlines()


input_example = get_input("day1/example.txt")
input_final = get_input("day1/input.txt")


def test_solve_example():
    assert solve(input_example) == 3


def test_solve_final():
    assert solve(input_final) == 984


def test_solve2_example():
    assert solve2(input_example) == 6


def test_solve2_final():
    assert solve2(input_final) == 5657
