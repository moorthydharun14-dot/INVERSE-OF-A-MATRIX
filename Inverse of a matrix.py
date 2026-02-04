#Program to find the inverse of a matrix.
#RegisterNumber: DHARUN M 25018453
#RegisterNumber:212225230057
import numpy as np
matrix = np.array([[6, 2, 3], [3, 1, 1],[10, 3, 4]])
rank = np.linalg.inv(matrix)
print(rank)
