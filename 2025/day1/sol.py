import re
from typing import List

number_pattern: str = r"\d+"

def parse_rotation(rotation: str) -> int:
    match = int(re.search(number_pattern, rotation).group(0))
    return -match if rotation[0] == 'L' else match

def move(start: int, rotation: int, sign: int = 1) -> int:
    return (start + sign * rotation) % 100

#Part 01
def rotation_generator(rotations: List[int], start: int = 50):
    for rotation in rotations:
        yield (start := move(start, rotation)) == 0

def count_zero_positions(rotations: List[int]) -> int:
    return sum(rotation_generator(rotations))

#Part 02
def rotation_clicks(rotations: List[int], start: int = 50):
    for rotation in rotations:
        sign = -1 if rotation < 0 else 1 
        yield from (move(start, step, sign) == 0 for step in range(1, abs(rotation)))
        start = move(start, rotation)

def count_zero_clicks(rotations: List[int]) -> int:
    return sum(rotation_clicks(rotations))

if __name__ == "__main__":
    rotations: List[int] = [parse_rotation(line.strip()) for line in open("input.txt", "r").readlines()]

    part1 = count_zero_positions(rotations)
    part2 = part1 + count_zero_clicks(rotations)

    print(f"Part 01: {part1}")
    print(f"Part 02: {part2}")
