import unittest
from Solution import Solution


class Solution_test(unittest.TestCase):
    def test_A(self):
       print(Solution().threeSumClosest([-8,-6,-4,1,7,12,19,23],-9),-9)

if __name__ == '__main__':
    unittest.main()
