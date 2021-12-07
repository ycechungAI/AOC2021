x = 0;
d = 0;
prod = 0;
with open('input.txt') as f:
	for line in f:
		direction, value = [item.strip() for item in line.split(' ')]   
		if direction == "forward":
			x += int(value)
		elif direction == "down":
			d += int(value)
		elif direction == "up":
			d -= int(value)
prod = d * x
print(prod)
