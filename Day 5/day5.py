import numpy as np
import re

# read input file
lines = open("input.txt").readlines()
# Convert the input file into a numpy array of coordinates
coordinates = np.array([re.match('(\d+),(\d+) -> (\d+),(\d+)', line).groups() for line in lines]).astype(int)
size = np.max(coordinates)+1


# init grid of zeros of size by size
grid = np.zeros((size, size))
# Find the coordinates that are horizontal or vertical
hv = coordinates[(coordinates[:, 0] == coordinates[:, 2]) + (coordinates[:, 1] == coordinates[:, 3])]
# For each horizontal or vertical coordinate, find the x and y ranges
# For each x and y range, increment the grid by 1
for x1, y1, x2, y2 in hv:
    grid[rrange(y1, y2), rrange(x1, x2)] += 1
# Sum the grid to find the number of coordinates that overlap
result = (grid >= 2).sum()
print("Part 1 result:", result)

#Part 2 - diagonal hack
def rrange(start, stop):
    return range(start, stop+1) if stop >= start else range(start, stop-1, -1)

grid = np.zeros((size, size))
for x1, y1, x2, y2 in coords:
    grid[rrange(y1, y2), rrange(x1, x2)] += 1
result = (grid >= 2).sum()
print("Part 2 result:", result)
