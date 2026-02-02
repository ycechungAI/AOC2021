from collections import defaultdict

def solve():
    adj = defaultdict(list)
    with open("input.txt", "r") as f:
        for line in f:
            if "-" not in line: continue
            u, v = line.strip().split("-")
            adj[u].append(v)
            adj[v].append(u)

    # Part 1
    def count_paths_part1(u, visited):
        if u == "end":
            return 1

        count = 0
        visited.add(u)
        for v in adj[u]:
            if v == "start": continue
            if v.islower() and v in visited:
                continue
            count += count_paths_part1(v, visited.copy()) # Pass copy to branch
            # Actually, using a shared set with backtrack is faster,
            # but copy is easier to reason about for small inputs.
            # Given input size, copy is fine.
        return count

    part1_result = count_paths_part1("start", set())
    print(f"Part 1: {part1_result}")

    # Part 2
    # Optimization: Use DFS with backtracking on the visited set to avoid excessive copying
    def count_paths_part2(u, visited, doubled_small):
        if u == "end":
            return 1

        count = 0

        # Mark visited if small
        if u.islower():
            visited[u] += 1

        for v in adj[u]:
            if v == "start": continue

            if v.islower():
                if visited[v] == 0:
                    count += count_paths_part2(v, visited, doubled_small)
                elif visited[v] == 1 and not doubled_small:
                    count += count_paths_part2(v, visited, True)
            else:
                count += count_paths_part2(v, visited, doubled_small)

        # Backtrack
        if u.islower():
            visited[u] -= 1

        return count

    # Initialize visited counts
    visited_counts = defaultdict(int)
    part2_result = count_paths_part2("start", visited_counts, False)
    print(f"Part 2: {part2_result}")

if __name__ == "__main__":
    solve()
