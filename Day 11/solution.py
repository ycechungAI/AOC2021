def solve():
    with open("input.txt", "r") as f:
        grid = [list(map(int, list(line.strip()))) for line in f if line.strip()]

    rows = 10
    cols = 10
    total_flashes = 0
    step = 0

    # We need to simulate indefinitely for Part 2
    # So we'll check for Part 1 condition inside the loop

    first_all_flash_step = None

    while True:
        step += 1

        # 1. Increase energy by 1
        for r in range(rows):
            for c in range(cols):
                grid[r][c] += 1

        # 2. Flash
        flashed = set()
        queue = []

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] > 9:
                    flashed.add((r, c))
                    queue.append((r, c))

        while queue:
            curr_r, curr_c = queue.pop(0)

            # Neighbors (8 directions)
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0:
                        continue
                    nr, nc = curr_r + dr, curr_c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        grid[nr][nc] += 1
                        if grid[nr][nc] > 9 and (nr, nc) not in flashed:
                            flashed.add((nr, nc))
                            queue.append((nr, nc))

        # 3. Reset
        for r, c in flashed:
            grid[r][c] = 0

        if step <= 100:
            total_flashes += len(flashed)

        if len(flashed) == rows * cols:
            first_all_flash_step = step
            if step >= 100: # Only break if we passed step 100 or already printed it
                 break

        # Safety break (unlikely to be needed for valid input)
        if step > 1000 and first_all_flash_step:
            break

    print(f"Part 1: {total_flashes}")
    print(f"Part 2: {first_all_flash_step}")

if __name__ == "__main__":
    solve()
