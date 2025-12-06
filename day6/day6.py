import re
import pytest


def solve_part_1(
    input: tuple[tuple[str, tuple[int, int], list[int]], list[str]],
) -> int:
    cols, lines = input

    for line in lines:
        for col in cols:
            span = col[1]
            value = line[span[0] : span[1]]
            if value:
                col[2].append(value)

    t = 0
    for col in cols:
        t += eval(col[0].join(col[2]))

    return t


def solve_part_2(
    input: tuple[tuple[str, tuple[int, int], list[str]], list[str]],
) -> int:
    problems, lines = input

    for line in lines:
        for i, p in enumerate(problems):
            [start, end] = p[1]

            value = line[start:end].strip()
            if value:
                p[2].append(value)

    t = 0
    for p in problems:
        t += eval(p[0].join(p[2]))

    return t


###
# UNIT TESTS
###


def get_input(file_path):
    with open(file_path, "r") as file:
        lines = file.read().splitlines()
        header = lines.pop(-1)
        problems = []
        iter = re.finditer(r"(\S\s+)[\s$]", header)
        for match in iter:
            problems.append((match.group().strip(), match.span(), []))
        return (problems, lines)


input_example = get_input("day6/example.txt")
input_final = get_input("day6/input.txt")


def test_part_1_example_solution():
    assert solve_part_1(input_example) == 4277556


def test_part_1_final_solution():
    assert solve_part_1(input_final) == 6757749566978


def test_part_2_example_solution():
    assert solve_part_2(input_example) == 3263827


@pytest.mark.skip(reason="n/i")
def test_part_2_final_solution():
    assert solve_part_2(input_final) == None
