def solve(input_lines, start_location=50):
    curr = start_location
    z = 0

    for line in input_lines:
        direction, chng = line[0], int(line[1:])

        if direction == "L":
            chng = -chng

        curr = ((curr + chng) % 100 + 100) % 100
        if curr == 0:
            z += 1

    return z


def solve2(input_lines, start_location=50):
    curr = start_location
    z = 0

    for line in input_lines:
        direction, chng = line[0], int(line[1:])
        dist = (curr if direction == "L" else 100 - curr) or 100
        rem = 0

        if chng >= dist:
            z += 1
            rem = chng - dist
            if rem > 0:
                z += rem // 100

        if direction == "L":
            chng = -chng

        curr = ((curr + chng) % 100 + 100) % 100

    return z


def get_input(file_path):
    with open(file_path, "r") as file:
        return file.readlines()


def test_solutions():
    input_example = get_input("day1/example.txt")
    input_final = get_input("day1/input.txt")

    assert solve(input_example) == 3
    assert solve(input_final) == 984
    assert solve2(input_example) == 6
    assert solve2(input_final) == 5657
