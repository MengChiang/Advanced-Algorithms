import unittest
import lecture1
import numpy as np


class Lecture1TestCase(unittest.TestCase):
    # def test_GCD_1(self):
    #     expect = 14
    #     actual = lecture1.GCD(56, 42)
    #     self.assertEqual(expect, actual)

    def test_GCD_2(self):
        expect = 20
        actual = lecture1.GCD(100, 20)
        self.assertEqual(expect, actual)

    def test_GCD_3(self):
        expect = 3
        actual = lecture1.GCD(108, 87)
        self.assertEqual(expect, actual)

    # def test_NN_1(self):
    #     A = np.array([
    #         [0, 2, 1, 2, 2],
    #         [2, 0, 2, 1, 1],
    #         [1, 2, 0, 1, 2],
    #         [2, 1, 1, 0, 2],
    #         [2, 1, 2, 2, 0]])

    #     expect = ([0, 2, 3, 1, 4], 4)
    #     actual = lecture1.NN(A, 0)
    #     # print(actual)
    #     self.assertEqual(expect, actual)


if __name__ == '__main__':
    unittest.main()
