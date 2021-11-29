import numpy as np


def is_triangle(triangle):
    x, y, z = int(triangle[0]), int(triangle[1]), int(triangle[2])
    if x < (y+z) and y < (x+z) and z < (x+y):
        return True
    return False


def part1(input_file=''):
    all_sets = np.loadtxt(input_file)

    return sum([1 for tri in all_sets if is_triangle(tri)])


def part2(input_file=''):
    all_sets = np.loadtxt(input_file)

    def find_triangles(np_array):
        np_array.sort(axis=-1)
        return sum(np.sum(np_array[:, :2], axis=-1) > np_array[:, 2])

    return find_triangles(all_sets.T.reshape(-1, 3))
