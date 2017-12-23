import unittest
from DivideTwoIntegers import Solution


class Test_DivideTwoIntegers(unittest.TestCase):
    def test_divide(self):
        print(Solution().divide(5,3))
        print(Solution().divide(-5,-3))
        print(Solution().divide(-5,3))
        print(Solution().divide(5,-3))
        print(Solution().divide(2,-3))
        print(Solution().divide(1,1))
        print(Solution().divide(56,7))
        print(Solution().divide(0,7))
        print(Solution().divide(56,0))
        print(Solution().divide(2147483647,7))
        print(Solution().divide(2147483647,-1))
        print(Solution().divide(-2147483648,-1))
if __name__ == '__main__':
    unittest.main()
