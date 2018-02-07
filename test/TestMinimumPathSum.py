import unittest
from MinimumPathSum import Solution

class Test_MinimumPathSum(unittest.TestCase):
    def test_minPathSum(self):
        print(Solution().minPathSum([[1,3,1],[1,5,1],[4,2,1]]))
        print(Solution().minPathSum([[1,3,1]]))
        print(Solution().minPathSum([[1],[1],[4]]))
        print(Solution().minPathSum([[1,3,1],[1,5,1]]))
        print(Solution().minPathSum([[1,3],[1,5],[4,2]]))
        print(Solution().minPathSum([[]]))

if __name__ == '__main__':
    unittest.main()
