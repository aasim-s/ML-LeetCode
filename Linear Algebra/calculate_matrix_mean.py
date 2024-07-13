import numpy as np


def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    np_matrix = np.array(matrix)

    if mode == "row":
        means = np.mean(np_matrix, axis=1).tolist()
    elif mode == "column":
        means = np.mean(np_matrix, axis=0).tolist()
    else:
        raise ValueError("Invalid mode. Choose 'row' or 'column'.")

    return means


def calculate_matrix_mean_1(matrix: list[list[float]], mode: str) -> list[float]:
    if mode == 'column':
        return [sum(col) / len(matrix) for col in zip(*matrix)]
    elif mode == 'row':
        return [sum(row) / len(row) for row in matrix]
    else:
        raise ValueError("Invalid mode. Choose 'row' or 'column'.")


print(calculate_matrix_mean(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], mode='column'))  # [4.0, 5.0, 6.0]
print(calculate_matrix_mean_1(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], mode='row'))  # [2.0, 5.0, 8.0]
