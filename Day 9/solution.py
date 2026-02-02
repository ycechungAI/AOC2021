def solve():
    with open("input.txt", "r") as f:
        grid = [list(map(int, list(line.strip()))) for line in f if line.strip()]

    rows = len(grid)
    cols = len(grid[0])

    low_points = []
    risk_level_sum = 0

    for r in range(rows):
        for c in range(cols):
            val = grid[r][c]
            is_low = True
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] <= val:
                        is_low = False
                        break
            if is_low:
                low_points.append((r, c))
                risk_level_sum += (val + 1)

    print(f"Part 1: {risk_level_sum}")

    # Part 2: Basins
    # Basin is any connected region of non-9s
    basin_sizes = []
    visited = set()

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != 9 and (r, c) not in visited:
                # Start BFS/DFS
                size = 0
                queue = [(r, c)]
                visited.add((r, c))
                while queue:
                    curr_r, curr_c = queue.pop(0)
                    size += 1

                    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nr, nc = curr_r + dr, curr_c + dc
                        if 0 <= nr < rows and 0 <= nc < cols:
                            if grid[nr][nc] != 9 and (nr, nc) not in visited:
                                visited.add((nr, nc))
                                queue.append((nr, nc))
                basin_sizes.append(size)

    basin_sizes.sort(reverse=True)
    part2_result = 1
    for i in range(min(3, len(basin_sizes))):
        part2_result *= basin_sizes[i]

    print(f"Part 2: {part2_result}")

if __name__ == "__main__":
    solve()
