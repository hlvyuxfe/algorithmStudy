import unittest
from FirstMissingPositive import Solution

class Test_FirstMissingPositive(unittest.TestCase):
    def test_firstMissingPositive(self):
        print(Solution().firstMissingPositive([3,4,-1,1]))
        print(Solution().firstMissingPositive([2, 3, 4, -1,7, 9, 6, 10, 1,5,7]))

if __name__ == '__main__':
    unittest.main()
