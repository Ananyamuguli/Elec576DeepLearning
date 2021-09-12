import numpy as np
from scipy import linalg


def matrix_multiplication(x, y):
    return x*y


def matrix_inverse(x):
    return linalg.inv(x)


if __name__ == '__main__':
    a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    b = np.random.random((3, 3))
    m = matrix_multiplication(a, b)
    print('Product of a and b : ', m)
    inve = matrix_inverse(b)
    print('Inverse of b : ', inve)



