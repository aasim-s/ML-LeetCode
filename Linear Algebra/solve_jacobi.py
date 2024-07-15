"""
Write a Python function that uses the Jacobi method to solve a system of linear equations given by Ax = b.
The function should iterate 10 times, rounding each intermediate solution to four decimal places, and return
the approximate solution x.
"""

import numpy as np


def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
    x = np.zeros(len(b))
    d_a = np.diag(A)
    nda = A - np.diag(d_a)
    x_hold = np.zeros(len(b))
    for _ in range(n):
        for i in range(len(A)):
            x_hold[i] = (1 / d_a[i]) * (b[i] - sum(nda[i] * x))
        x = x_hold.copy()
    return np.round(x, 4).tolist()


print(solve_jacobi(np.array([[5, -2, 3], [-3, 9, 1], [2, -1, -7]]), np.array([-1, 2, 3]), 2))
# [0.146, 0.2032, -0.5175]
