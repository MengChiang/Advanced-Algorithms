import numpy as np
import copy


def GCD(num1, num2):
    times = 0
    while num2 != 0:
        times += 1
        print("iterative {0}: {1}, {2}".format(times, num1, num2))
        remainder = num1 % num2
        num1 = num2
        num2 = remainder
    print("GCD = ", num1)
    return num1


def NN(A, start):
    """Nearest neighbor algorithm.
    A is an NxN array indicating distance between N locations
    start is the index of the starting location
    Returns the path and cost of the found solution
    """
    path = [start]
    cost = 0
    N = A.shape[0]
    mask = np.ones(N, dtype=bool)  # boolean values indicating which
    # locations have not been visited
    mask[start] = False

    for i in range(N-1):
        last = path[-1]
        # find minimum of remaining locations
        next_ind = np.argmin(A[last][mask])
        next_loc = np.arange(N)[mask][next_ind]  # convert to original location
        path.append(next_loc)
        mask[next_loc] = False
        cost += A[last, next_loc]

    print(path, cost)
    return path, cost


def Nearest_Neighbor_Tour(array, start):

    n = len(array)

    result = []
    cost = None
    states = [False] * n
    states[start] = True

    # for i in range(n):
    # array[start] =
    # print(i)
    # print(states)

# Nearest_Neighbor_Tour([-21, -5, -1, 0, 1, 3, 11], 3)


A = np.array([
    [0, 2, 1, 2, 2],
    [2, 0, 2, 1, 1],
    [1, 2, 0, 1, 2],
    [2, 1, 1, 0, 2],
    [2, 1, 2, 2, 0]])
NN(A, 0)
