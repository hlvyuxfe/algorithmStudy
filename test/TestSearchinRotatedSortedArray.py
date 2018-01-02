import unittest
from SearchinRotatedSortedArray import Solution

class Test_SearchinRotatedSortedArray(unittest.TestCase):
    def test_search(self):
        print(Solution().search([],1))
        print(Solution().search([1],1))
        print(Solution().search([4,5,6,7,0,1,2],1))
        print(Solution().search([4,5,6,7,0,1,2],7))
        print(Solution().search([0,1,2,4,5,6,7],1))
        print(Solution().search([42,53,61,71,0,12,15,19,22],15))
        print(Solution().search([42,53,61,71,0,12,15,19,22],18))

if __name__ == '__main__':
    unittest.main()
