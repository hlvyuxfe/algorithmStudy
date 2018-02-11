import unittest
from CountandSay import Solution

class Test_CountandSay(unittest.TestCase):
    def test_countAndSay(self):
        print(Solution().countAndSay(1))
        print(Solution().countAndSay(4))
        print(Solution().countAndSay(6))
        print(Solution().countAndSay(7))
        print(Solution().countAndSay(8))
        print(Solution().countAndSay(9))
        print(Solution().countAndSay(30))

if __name__ == '__main__':
    unittest.main()
