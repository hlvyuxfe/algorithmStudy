import unittest
from SearchInsertPosition import Solution

class Test_SearchInsertPosition(unittest.TestCase):
    def test_searchInsert(self):
        print(Solution().searchInsert([], 0))
        print(Solution().searchInsert([1,3,5,6], 5))
        print(Solution().searchInsert([1,3,5,6], 2))
        print(Solution().searchInsert([1,3,5,6], 7))
        print(Solution().searchInsert([1,3,5,6], 0))
        print(Solution().searchInsert([1,3,5,6,9,10,14], 14))

if __name__ == '__main__':
    unittest.main()
