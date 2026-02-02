def solve():
    with open("input.txt", "r") as f:
        lines = [line.strip() for line in f if line.strip()]

    pairs = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>'
    }

    part1_scores = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }

    part2_scores = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }

    total_syntax_error_score = 0
    completion_scores = []

    for line in lines:
        stack = []
        is_corrupted = False
        for char in line:
            if char in pairs:
                stack.append(pairs[char]) # Push expected closer
            else:
                if not stack or stack[-1] != char:
                    # Corrupted
                    total_syntax_error_score += part1_scores[char]
                    is_corrupted = True
                    break
                else:
                    stack.pop()

        if not is_corrupted and stack:
            # Incomplete
            line_score = 0
            # Stack contains expected closers in order (last added is next expected)
            # So we just pop them off
            while stack:
                closer = stack.pop()
                line_score = line_score * 5 + part2_scores[closer]
            completion_scores.append(line_score)

    print(f"Part 1: {total_syntax_error_score}")

    completion_scores.sort()
    part2_result = completion_scores[len(completion_scores) // 2]
    print(f"Part 2: {part2_result}")

if __name__ == "__main__":
    solve()
