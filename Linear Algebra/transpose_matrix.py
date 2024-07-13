def transpose_matrix(a: list[list[int | float]]) -> list[list[int | float]]:
    column_len = len(a)
    row_len = len(a[0])
    b = []
    for i in range(row_len):
        new_row = []
        for j in range(column_len):
            new_row.append(a[j][i])
        b.append(new_row)
    return b


# using inbuilt methods
# def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
#     return [list(i) for i in zip(*a)]

print(transpose_matrix([[1, 2, 3], [4, 5, 6]]))  # [[1,4],[2,5],[3,6]]
