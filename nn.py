    # def test_NN_1(self):
    #     A = np.array([
    #         [0, 2, 1, 2, 2],
    #         [2, 0, 2, 1, 1],
    #         [1, 2, 0, 1, 2],
    #         [2, 1, 1, 0, 2],
    #         [2, 1, 2, 2, 0]])

    #     expect = ([0, 2, 3, 1, 4], 4)
    #     actual = lecture1.NN(A, 0)
    #     print(actual)
    #     self.assertEqual(expect, actual)

    # def NN(A, start):
    # """Nearest neighbor algorithm.
    # A is an NxN array indicating distance between N locations
    # start is the index of the starting location
    # Returns the path and cost of the found solution
    # """
    # path = [start]
    # cost = 0
    # N = A.shape[0]
    # mask = np.ones(N, dtype=bool)  # boolean values indicating which
    # # locations have not been visited
    # mask[start] = False

    # for i in range(N-1):
    #     last = path[-1]
    #     # find minimum of remaining locations
    #     next_ind = np.argmin(A[last][mask])
    #     next_loc = np.arange(N)[mask][next_ind]  # convert to original location
    #     path.append(next_loc)
    #     mask[next_loc] = False
    #     cost += A[last, next_loc]

    # print(path, cost)
    # return path, cost