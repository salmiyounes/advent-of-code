from typing import List, Tuple, Iterable

def get_neighbors(grid: List[List[bool]], x: int, y: int) -> Iterable[bool]:
    rows, cols = len(grid), len(grid[0])

    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if dx == 0 and dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                yield grid[nx][ny]

def can_be_accessed(grid: List[List[bool]], x: int, y: int) -> bool:
    return grid[x][y] and sum(get_neighbors(grid, x, y)) < 4

def all_cells(grid: List[List[bool]]) -> Iterable[Tuple[int, int]]:
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            yield i, j

#Part 01
def total_rolls_of_paper(grid: List[List[bool]]) -> int:
    return sum(
        1
        for (i, j) in all_cells(grid)
        if can_be_accessed(grid, i, j)
    )

#Part 02
def access_then_remove(grid: List[List[bool]]) -> int:
    # Find accessible cells
    accessible = [
        (i, j)
        for (i, j) in all_cells(grid)
        if can_be_accessed(grid, i, j)
    ]

    # Remove them
    for i, j in accessible:
        grid[i][j] = False

    return len(accessible)

def total_removed_papers(grid: List[List[bool]]) -> int:
    total = 0
    while (removed := access_then_remove(grid)) > 0:
        total += removed
    return total

if __name__ == "__main__":
    grid = [[c == '@' for c in line.strip()] for line in open("input.txt", "r").readlines()]

    part01 = total_rolls_of_paper(grid)
    part02 = total_removed_papers(grid)
    print(f"Part 01: {part01}")
    print(f"Part 02: {part02}")
    
