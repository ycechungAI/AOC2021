def solve():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    part1_count = 0
    total_output_sum = 0

    for line in lines:
        if "|" not in line:
            continue
        patterns_str, output_str = line.strip().split(" | ")
        patterns = patterns_str.split()
        outputs = output_str.split()

        # Part 1 counting
        for o in outputs:
            if len(o) in [2, 4, 3, 7]:
                part1_count += 1

        # Part 2 Decoding
        # Map sorted string -> digit
        # 1: len 2
        # 4: len 4
        # 7: len 3
        # 8: len 7

        digits = {} # int -> set of chars
        by_len = {l: [] for l in range(2, 8)}

        for p in patterns:
            by_len[len(p)].append(set(p))

        if not by_len[2]:
            print(f"Error parsing line: {line.strip()}")
            continue

        digits[1] = by_len[2][0]
        digits[4] = by_len[4][0]
        digits[7] = by_len[3][0]
        digits[8] = by_len[7][0]

        # Length 6: 0, 6, 9
        # 9 contains 4
        # 0 contains 1, not 4
        # 6 contains neither (doesn't contain 1)
        for p_set in by_len[6]:
            if digits[4].issubset(p_set):
                digits[9] = p_set
            elif digits[1].issubset(p_set):
                digits[0] = p_set
            else:
                digits[6] = p_set

        # Length 5: 2, 3, 5
        # 3 contains 1
        # 5 is subset of 6 (or 9) -> 6 contains 5
        # 2 remaining
        for p_set in by_len[5]:
            if digits[1].issubset(p_set):
                digits[3] = p_set
            elif p_set.issubset(digits[6]):
                digits[5] = p_set
            else:
                digits[2] = p_set

        # Create reverse map: sorted string -> value
        s_map = {}
        for val, char_set in digits.items():
            key = "".join(sorted(list(char_set)))
            s_map[key] = val

        # Decode output
        current_val = 0
        for o in outputs:
            key = "".join(sorted(list(o)))
            current_val = current_val * 10 + s_map[key]

        total_output_sum += current_val

    print(f"Part 1: {part1_count}")
    print(f"Part 2: {total_output_sum}")

if __name__ == "__main__":
    solve()
