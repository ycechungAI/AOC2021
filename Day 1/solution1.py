with open("input.txt") as f:
    l = [int(x.strip()) for x in f]

part1 = 0
for i, n1 in enumerate(l[:-1]):
    n2 = l[i+1]
    if n2 - n1 > 0:
		part1 = part1 + 1
		
part2 = 0
for j, m1 in enumerate(l[:-3]):
	m2 = l[j+1]
	m3 = l[j+2]
	m4 = l[j+3]
	sum3 = m1 + m2 + m3
	sumnext = m2 + m3 + m4
	if sumnext - sum3 > 0:
		part2 = part2 + 1
		
print(part1)
print(part2)
