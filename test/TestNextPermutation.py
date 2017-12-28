import unittest
from Nextpermutation import Solution

class Test_TestNextPermutation(unittest.TestCase):
    def test_nextPermutation(self):
        numsList = [[1,2],[1],[1,2,3],[3,2,1],[1,1,5],[3,4,5,2,1],[1,2,5,4,3],[5,1,1],[1,5,1]]
        for nums in numsList:
            print(nums)
            Solution().nextPermutation(nums)
            print(nums)

if __name__ == '__main__':
    unittest.main()
