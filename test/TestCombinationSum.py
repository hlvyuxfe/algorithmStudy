import unittest
from CombinationSum import Solution

class Test_TestCombinationSum(unittest.TestCase):
    def test_A(self):
        print(Solution().combinationSum([2, 3, 6, 7],7))
        print(Solution().combinationSum([8,7,4,3],11))

if __name__ == '__main__':
    unittest.main()
