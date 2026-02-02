def solve():
    with open("input.txt", "r") as f:
        data = list(map(int, f.read().strip().split(",")))

    # Initial state
    fish_counts = [0] * 9
    for timer in data:
        fish_counts[timer] += 1

    def simulate(counts, days):
        current_counts = list(counts)
        for _ in range(days):
            new_counts = [0] * 9
            # Shift counts down
            for i in range(1, 9):
                new_counts[i-1] = current_counts[i]

            # Spawn new fish
            spawning_fish = current_counts[0]
            new_counts[6] += spawning_fish # Reset parents
            new_counts[8] = spawning_fish  # New offspring

            current_counts = new_counts
        return sum(current_counts)

    # Part 1: 80 days
    part1_result = simulate(fish_counts, 80)
    print(f"Part 1: {part1_result}")

    # Part 2: 256 days
    part2_result = simulate(fish_counts, 256)
    print(f"Part 2: {part2_result}")

if __name__ == "__main__":
    solve()
