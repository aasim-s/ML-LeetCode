def matrix_dot_vector(a: list[list[int | float]], b: list[int | float]) -> list[int | float]:
    vector_len = len(b)
    matrix_rows = len(a)
    c = []

    if len(a[0]) != vector_len:
        return [-1]

    for i in range(matrix_rows):
        total = 0
        for j in range(vector_len):
            total += a[i][j] * b[j]
        c.append(total)

    return c


print(matrix_dot_vector([[1, 2, 3], [2, 4, 5], [6, 8, 9]], [1, 2, 3]))  #[14, 25, 49]

"""
[1,2,3]  [1,2,3]   1+4+9   = 14
[2,4,5]            2+8+15  = 25
[6,8,9]            6+16+27 = 49
"""
