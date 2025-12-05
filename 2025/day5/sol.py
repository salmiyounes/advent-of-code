from typing import List, Generator, Tuple
import re

RANGE_PATTERN = r"(\d+)-(\d+)"
NUMBER_PATTERN = r"\d+"

def parse_ranges(data: str) -> Generator[Tuple[int, int], None, None]:
    for start, end in re.findall(RANGE_PATTERN, data):
        yield int(start), int(end)

def parse_ingredients(data: str) -> Generator[int, None, None]:
    last_section = data.split("\n\n")[-1]
    for num in re.findall(NUMBER_PATTERN, last_section):
        yield int(num)

#Part 01
def is_fresh(start: int, end: int, ingredient: int) -> bool:
    return start <= ingredient <= end

def count_fresh_ingredients(data: str) -> int:
    ranges = list(parse_ranges(data))
    total = 0
    for ingredient in parse_ingredients(data):
        if any(is_fresh(start, end, ingredient) for start, end in ranges):
            total += 1
    return total

#Part 02
def merge_intervals(intervals: Generator[Tuple[int, int], None, None]) -> Generator[Tuple[int, int], None, None]:
    intervals: List[Tuple[int, int]] = sorted(intervals, key=lambda x: x[0])
    if not intervals:
        return
    prev_start, prev_end = intervals[0]
    for start, end in intervals[1:]:
        if start <= prev_end:
            prev_end = max(prev_end, end)
        else:
            yield prev_start, prev_end
            prev_start, prev_end = start, end
    yield prev_start, prev_end

def count_fresh_ingredient_ranges(data: str) -> int:
    return sum(end - start + 1 for start, end in merge_intervals(parse_ranges(data)))

if __name__ == "__main__":
    data = open("input.txt").read()

    part01 = count_fresh_ingredients(data)
    part02 = count_fresh_ingredient_ranges(data)

    print(f"Part 01: {part01}")
    print(f"Part 02: {part02}")

