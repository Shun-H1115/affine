import numpy as np
import pandas


def affine(df, point_lists):
    src_points, dst_points = point_lists

    initial_guess = [1,0,0,1,0,0]
    result = optimize.minimize(error_func, initial_guess, args=(src_points, dst_points))
    affine = affine_transform_matrix(result.x)

    return 

def affine_transform_matrix(params):
    a, b, c, d, e, f = params

    return np.array([[a, b, c], [d, e, f], [0, 0, 1]])

def error_func(params, src_points, dst_points):
    transform = affine_transform_matrix(params)
    error = 0

    for (x, y), (X, Y) in zip(src_points, dst_points):
        src = np.array([x, y, 1])
        dst = np.array([X, Y, 1])

        error += np.sum((np.dot(transform, src) - dst) ** 2)

    return