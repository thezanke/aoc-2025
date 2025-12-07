import re


def parse_input(lines: list[str]):
    header = lines.pop(-1)

    problems = [
        (match.group().strip(), match.span(), [])
        for match in re.finditer(r"(\S\s+)[\s$]", header)
    ]

    for line in lines:
        for prob in problems:
            [_, (start, end), num_list] = prob
            value = line[start:end]
            if value:
                num_list.append(value)

    return problems


def solve_part_1(
    problems: tuple[list[tuple[str, tuple[int, int], list[list[str]]]]],
) -> int:
    t = 0
    for op, _, num_list in problems:
        t += eval(op.join(num_list))

    return t


def solve_part_2(
    problems: tuple[list[tuple[str, tuple[int, int], list[list[str]]]]],
) -> int:
    t = 0
    for op, _, num_list in problems:
        t += eval(op.join(filter(None, ["".join(r).strip() for r in zip(*num_list)])))

    return t


###
# UNIT TESTS
###


def get_input(file_path):
    with open(file_path, "r") as file:
        return parse_input(file.read().splitlines())


def test_part_1_example_solution():
    input_example = get_input("day6/example.txt")
    assert solve_part_1(input_example) == 4277556


def test_part_1_final_solution():
    input_final = get_input("day6/input.txt")
    assert solve_part_1(input_final) == 6757749566978


def test_part_2_example_solution():
    input_example = get_input("day6/example.txt")
    assert solve_part_2(input_example) == 3263827


def test_part_2_final_solution():
    input_final = get_input("day6/input.txt")
    assert solve_part_2(input_final) == 10603075273949
