import unittest

from FourSum import Solution

class Test_FourSum(unittest.TestCase):
    def test_fourSum(self):
        print(Solution().fourSum([1, 0, -1, 0, -2, 2],0))
        print(Solution().fourSum([-3,-2,-1,0,0,1,2,3],0))
        print(Solution().fourSum([0,0,0,0],0))
        print(Solution().fourSum([1,-1,1,-1],0))
        print(Solution().fourSum([-1,-1,0,0,0,2,2,2],0))
        print(Solution().fourSum([5,5,3,5,1,-5,1,-2],4))
        print(Solution().fourSum([-1,-5,-5,-3,2,5,0,4],-7))

if __name__ == '__main__':
    unittest.main()
