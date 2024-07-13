import numpy as np


# using numpy
def reshape_matrix(a: list[list[int | float]], new_shape: tuple[int, int]) -> list[list[int | float]]:
    np_array = np.array(a)
    reshaped_matrix = np_array.reshape(new_shape).tolist()
    return reshaped_matrix


# using list comprehension
def reshape_matrix_1(a: list[list[int | float]], new_shape: tuple[int, int]) -> list[list[int | float]]:
    reshaped_matrix = []
    all_elements = [num for row in a for num in row]
    count = 0
    row = []
    for i in range(len(all_elements)):
        count += 1
        row.append(all_elements[i])
        if count == new_shape[1]:
            reshaped_matrix.append(row)
            row = []
            count = 0

    return reshaped_matrix


print(reshape_matrix(a=[[1, 2, 3, 4], [5, 6, 7, 8]], new_shape=(4, 2)))  # [1, 2], [3, 4], [5, 6], [7, 8]]

