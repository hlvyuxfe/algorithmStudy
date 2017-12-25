#You are given a string, s, and a list of words, words, that are all of the same 
#length. Find all starting indices of substring(s) in s that is a concatenation of each word 
#in words exactly once and without any intervening characters.

#For example, given:
#s: "barfoothefoobarman"
#words: ["foo", "bar"]

#You should return the indices: [0,9].
#(order does not matter).
class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not words:
            return []
        result = []
        wordlength= len(words[0])
        wordcount = len(words)
        for i in range(len(s)-wordcount*wordlength+1):
            count=0
            wordsdict={}
            for word in words:
                if word not in wordsdict:
                    wordsdict[word]=1
                else:
                    wordsdict[word]+=1
            while True:
                word = s[i+count*wordlength:i+(count+1)*wordlength]
                if word not in wordsdict or wordsdict[word]==0:
                    break
                else:
                    wordsdict[word]-=1
                    count+=1
                    if count==wordcount:
                        result.append(i)
                        break
        return result