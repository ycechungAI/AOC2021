def solve():
    with open("input.txt", "r") as f:
        # The input is comma-separated integers
        positions = list(map(int, f.read().strip().split(",")))

    # Part 1: Constant fuel cost -> Median minimizes L1 norm
    positions.sort()
    n = len(positions)
    median = positions[n // 2]
    fuel_part1 = sum(abs(x - median) for x in positions)
    print(f"Part 1: {fuel_part1}")

    # Part 2: Increasing fuel cost -> Mean minimizes L2-like norm
    # The optimal position is within 0.5 of the mean.
    mean_val = sum(positions) / n
    import math
    targets = [math.floor(mean_val), math.ceil(mean_val)]

    min_fuel_part2 = float('inf')
    for target in targets:
        current_fuel = 0
        for x in positions:
            dist = abs(x - target)
            current_fuel += dist * (dist + 1) // 2
        if current_fuel < min_fuel_part2:
            min_fuel_part2 = current_fuel

    print(f"Part 2: {min_fuel_part2}")

if __name__ == "__main__":
    solve()
