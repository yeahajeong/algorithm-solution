import unittest
from solution import solution


class TestSolution(unittest.TestCase):

    def test_case1(self):
        result = solution(n=3, signs=[[0, 1, 0], [0, 0, 1], [1, 0, 0]])
        self.assertEqual(result, [[1, 1, 1], [1, 1, 1], [1, 1, 1]])

    def test_case2(self):
        result = solution(3, [[0, 0, 1], [0, 0, 1], [0, 1, 0]])
        self.assertEqual(result, [[0, 1, 1], [0, 1, 1], [0, 1, 1]])


if __name__ == "__main__":
    unittest.main()