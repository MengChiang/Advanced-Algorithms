import unittest
import lecture1
import numpy as np

class Lecture1TestCase(unittest.TestCase):
    def setUp(self):
        self.array = [-21, -5, -1, 0, 1, 3, 11]
    
    def test_GCD_1(self):
        expect = 14
        actual = lecture1.GCD(56, 42)
        self.assertEqual(expect, actual)

    def test_GCD_2(self):
        expect = 20
        actual = lecture1.GCD(100, 20)
        self.assertEqual(expect, actual)

    def test_GCD_3(self):
        expect = 3
        actual = lecture1.GCD(108, 87)
        self.assertEqual(expect, actual)

    def test_simple_NN_1(self):
        expect = ([3, 4, 2, 5, 1, 6, 0], 63)
        actual = lecture1.Nearest_Neighbor_Tour(self.array, 3)
        self.assertEqual(expect, actual)

    def test_simple_NN_2(self):
        expect = ([6, 5, 4, 3, 2, 1, 0], 32)
        actual = lecture1.Nearest_Neighbor_Tour(self.array, 6)
        self.assertEqual(expect, actual)

    def test_simple_NN_3(self):
        expect = ([0, 1, 2, 3, 4, 5, 6], 32)
        actual = lecture1.Nearest_Neighbor_Tour(self.array, 0)
        self.assertEqual(expect, actual)
    
    def test_simple_NN_4(self):
        expect = ([1, 2, 0, 3, 4, 5, 6], 56)
        actual = lecture1.Nearest_Neighbor_Tour(self.array, 1)
        self.assertEqual(expect, actual)


if __name__ == '__main__':
    try:
        unittest.main()
    except:
        print("An exception occurred")
