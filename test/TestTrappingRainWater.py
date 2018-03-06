import unittest
from TrappingRainWater import Solution

class Test_TrappingRainWater(unittest.TestCase):
    def test_trap(self):
        print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))
        print(Solution().trap([0,1,2,3,4,5,6,7,6,5,4,3,2,1]))
        print(Solution().trap([0,1,2,3,4,5,6,7,6,5,4,3,2,7]))

if __name__ == '__main__':
    unittest.main()
