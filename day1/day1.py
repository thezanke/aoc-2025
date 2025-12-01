def get_input(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

def solve(input_lines, start_location = 50):
    curr = start_location
    z = 0

    print("Starting location:", curr)

    for line in input_lines:
        direction, distance = line[0], int(line[1:])

        if direction == 'L':
            distance = -distance

        curr = ((curr + distance) % 100 + 100) % 100
        if (curr == 0):
            z += 1


        print("Updated location:", curr)

    print("Final location:", curr)

    print("Zeroes:", z)

def solve2(input_lines, start_location = 50):
    curr = start_location
    z = 0

    print("Starting location:", curr)

    for line in input_lines:
        direction, distance = line[0], int(line[1:])

        if direction == 'L':
            if distance >= curr:
                z += (distance - curr) // 100
            distance = -distance

        if direction == 'R':
            remaining = 100 - curr
            if distance >= remaining:
                z += (distance - remaining) // 100

        curr = ((curr + distance) % 100 + 100) % 100

        print("Updated location:", curr)

    print("Final location:", curr)
    print("Zeroes:", z)
        

example = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82""".splitlines()

solve2(example)
# solve2(get_input('day1/input.txt'))