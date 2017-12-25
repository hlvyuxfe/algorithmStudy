import unittest
from SubstringwithConcatenationofAllWords import Solution

class Test_TestSubstringwithConcatenationofAllWords(unittest.TestCase):
    def test_findSubstring(self):
        print(Solution().findSubstring("barfoothefoobarman",["foo", "bar"]))
        print(Solution().findSubstring("babarfoothefoobarman",["foo", "bar"]))
        print(Solution().findSubstring("wordgoodgoodgoodbestword",["word","good","best","good"]))
if __name__ == '__main__':
    unittest.main()
