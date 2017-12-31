import unittest
from LongestValidParenttheses import Solution

class Test_LongestValidParentheses(unittest.TestCase):
    def test_longestValidParentheses(self):
        print(Solution().longestValidParentheses(''))
        print(Solution().longestValidParentheses(')'))
        print(Solution().longestValidParentheses('(()'))
        print(Solution().longestValidParentheses('(()()'))
        print(Solution().longestValidParentheses(')))()(()()'))
        print(Solution().longestValidParentheses('()(()))()()'))
        print(Solution().longestValidParentheses('()(())(()()())'))

if __name__ == '__main__':
    unittest.main()
