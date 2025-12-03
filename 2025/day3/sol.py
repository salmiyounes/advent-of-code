from typing import List, Tuple

#Part 01
def generate_evry_possible_joltage(bank: str):
    l = len(bank)
    for i in range(l):
        for j in range(i + 1, l):
            yield i, j

def largest_joltage_possible(bank: str) -> Tuple[int, int]:
    return max(
        ((i, j) for i, j in generate_evry_possible_joltage(bank)),
        key=lambda pair: int(bank[pair[0]] + bank[pair[1]])
    )

def total_joltage(banks: List[str], size: int = 2) -> int:
    if (size == 2):
        return sum(
            int(b[i] + b[j]) 
            for b in banks 
            for i, j in [largest_joltage_possible(b)]
        )
    else :
        return sum(int(largest_joltage_twelve_size(b)) for b in banks)

#Part 02
def largest_joltage_twelve_size(bank: str, index: int = 0, joltage: str = "") -> str:
    if len(joltage) == 12:
        return joltage
    substr = bank[index:len(bank) - (12 - len(joltage)) + 1]
    if not substr:
        return joltage
    m = max(substr)
    next_index = index + substr.index(m) + 1
    return largest_joltage_twelve_size(bank, next_index, joltage + m)

if __name__ == "__main__":
    banks: List[str] = [b.strip() for b in open("input.txt", "r").readlines()]

    part01 = total_joltage(banks)
    part02 = total_joltage(banks, 12)
    print (f"Part 01: {part01}")
    print (f"Part 02: {part02}")

