def scalar_multiply(matrix: list[list[int | float]], scalar: int | float) -> list[list[int | float]]:
    result = []

    for row in matrix:
        new_row = []
        for i in row:
            new_row.append(scalar * i)
        result.append(new_row)

    return result

# using list comprehension
# def scalar_multiply_1(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
#     return [[element * scalar for element in row] for row in matrix]

print(scalar_multiply(matrix=[[1, 2], [3, 4]], scalar=2))  # [[2, 4], [6, 8]]
