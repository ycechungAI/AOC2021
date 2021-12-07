x = 0;
d = 0;
aim = 0;
prod = 0;
with open('input.txt') as f:
	for line in f:
		direction, value = [item.strip() for item in line.split(' ')]   
		if direction == "forward":
			x += int(value);
			d += aim*int(value);
		elif direction == "down":
			aim += int(value);
		elif direction == "up":
			aim -= int(value);
prod = d * x;
print(prod)
