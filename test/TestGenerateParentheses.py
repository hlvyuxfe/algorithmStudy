import unittest
from GenerateParentheses import Solution

class Test_TestGenerateParentheses(unittest.TestCase):
    #def test_addFromLast(self):
    #    Solution().addFromLast(2)
    #    print(Solution().table[2])
    #    Solution().addFromLast(3)
    #    print(Solution().table[3])
    #    Solution().addFromLast(4)
    #    print(Solution().table[4])

    def test_generateParenthesis(self):
        #print(Solution().generateParenthesis(0))
        #print(Solution().generateParenthesis(1))
        #print(Solution().generateParenthesis(2))
        #print(Solution().generateParenthesis(3))
        #print(Solution().generateParenthesis(4))
        #print(Solution().generateParenthesis(4))
        print(Solution().generateParenthesis(8))
        print(len(Solution().table[8]))


if __name__ == '__main__':
    unittest.main()
