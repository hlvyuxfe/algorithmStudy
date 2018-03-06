import unittest
from MultiplyStrings import Solution

class Test_MultiplyStrings(unittest.TestCase):
    def test_multiply(self):
        print(Solution().multiply('0','52'))
        print(Solution().multiply('0','520'))
        print(Solution().multiply('11','11'))
        print(Solution().multiply('31','121'))
        print(Solution().multiply('123','123'))
        print(Solution().multiply('15129','15129'))
        print(Solution().multiply('228886641','228886641'))
        print(Solution().multiply('228886641','22888664'))
        print(Solution().multiply('1234567890','228886640'))
        print(Solution().multiply('1234567890987654231','228886640'))
        print(Solution().multiply('1234567890987654231','282576096420050458415373840'))
        print(Solution().multiply('348859375400825725348127613697431128522717040','282576096420050458415373840'))
        print(Solution().multiply('348859375400825725348127613697431128522717040','98579320500302309204859979879321947811513751146838562046418824138233600'))
        print(Solution().multiply('34390320177173278544123418955109500523326224530449795404468368405057209857347021265573972594319077929318818220544000','98579320500302309204859979879321947811513751146838562046418824138233600'))
if __name__ == '__main__':
    unittest.main()
