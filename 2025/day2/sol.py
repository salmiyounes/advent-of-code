import re
import math
from typing import List

RANGE_PATTERN: str = r"(\d+)-(\d+)"

def parse_ranges(ranges: List[str]):
    for line in ranges:
        for start_id, end_id in re.findall(RANGE_PATTERN, line):
            yield int(start_id), int(end_id)

def generate_divisors(num: int):
    limit = math.isqrt(num) 
    
    for i in range(1, limit + 1):  
        if num % i == 0:
            yield i
            quotient = num // i
            if i != quotient:
                yield quotient

def is_repeating_substring_number(num: int) -> bool:
    s = str(num)
    l = len(s)
    
    for d in generate_divisors(l):
        if d < l:
            if s[:d] * (l // d) == s:
                return True
    return False

def sum_repeating_substring_numbers(start_id: int, end_id: int) -> int:
    return sum(filter(is_repeating_substring_number, range(start_id, end_id + 1)))

def count_invalid_ids(ranges: List[str]) -> int:
    return sum(sum_repeating_substring_numbers(*r) for r in parse_ranges(ranges))

if __name__ == "__main__":
    patterns = [l.strip() for l in open("input.txt", "r").readlines()]
    part2 = count_invalid_ids(patterns)

    print(f"Part 02: {part2}")