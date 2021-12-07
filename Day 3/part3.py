#Using data science library numpy
import numpy as np

import numpy as np
# loads the input file into a numpy array.
lines = np.loadtxt("input.txt", "U")
# bits is each character is a single element of the array.
bits = int(len(lines[0]))
# The data reshaped into a 2D array, where each row is a single row of 
# the input file, and each column is a single bit.
data = lines.view('U1').astype(int).reshape(lines.shape[0], bits)
# creates a list of all possible bitmasks of size bits
pow2 = 1 << np.arange(bits)[::-1]

# counts the number of 1s and 0s in each row of the data.
ones = (data == 1).sum(axis=0)
zeros = (data == 0).sum(axis=0)

result = pow2.dot(ones > zeros) * pow2.dot(ones < zeros)
print("Part 1 result:", result)

a = b = data
# The for loop iterates over the columns of a and b.
for idx in range(bits):
    acol = a[:, idx]
    bcol = b[:, idx]
# Create a list of booleans called "b", such that b[i] is true if and only if
#  acol[i] is greater than the sum of all other elements in acol.
# Use b to index into a, and return the first element.
    a = a[acol == (acol.sum()*2 >= acol.size)] if len(a) > 1 else a
# Create a list of booleans called "a", such that a[i] is True if and only if 
# acol[i] is greater than or equal to the sum of all the elements of acol
# Use the built-in function len() to find the number of elements in a2.
# If the number of elements in a2 is greater than 1, then select all 
# the columns of a corresponding to the elements of a2;
# otherwise, select all the columns of a.
    b = b[bcol == (bcol.sum()*2 < bcol.size)] if len(b) > 1 else b
result = 0
result = pow2.dot(a[0]) * pow2.dot(b[0])
print("Part 2 result:", result)
