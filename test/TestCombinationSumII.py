import unittest
from CombinationSumII import Solution


class Test_CombinationSumII(unittest.TestCase):
    def test_combinationSum2(self):
        print(Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5],8))
        print(Solution().combinationSum2([10, 1, 2, 1, 7, 6, 1, 5],8))
        print(Solution().combinationSum2([10, 1, 2, 2, 7, 6, 1, 5],8))

if __name__ == '__main__':
    unittest.main()
