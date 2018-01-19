import unittest
from SearchforaRange import Solution

class Test_SearchforaRange(unittest.TestCase):
    def test_searchRange(self):
        print(Solution().searchRange([],8))
        print(Solution().searchRange([1],8))
        print(Solution().searchRange([1,10],10))
        print(Solution().searchRange([1,10],1))
        print(Solution().searchRange([5, 7, 7, 8, 8, 10],8))
        print(Solution().searchRange([1, 8, 8,8, 8,8, 8, 10],8))
        print(Solution().searchRange([8, 8, 8,8, 8,8, 8, 8],8))
        print(Solution().searchRange([1, 8, 8,8, 8,8, 8, 10],7))
        print(Solution().searchRange([1, 8],7))

if __name__ == '__main__':
    unittest.main()
