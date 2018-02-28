#Given a set of candidate numbers (C) (without duplicates) and a target number (T), 
#find all unique combinations in C where the candidate numbers sums to T.
#The same repeated number may be chosen from C unlimited number of times.
#Note:
#All numbers (including target) will be positive integers.
#The solution set must not contain duplicate combinations.
#For example, given candidate set [2, 3, 6, 7] and target 7, 
#A solution set is: 
#[
#  [7],
#  [2, 2, 3]
#]
class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        temp, start = [], 0
        result =[]
        self.combinate(start,candidates,temp, target, result)
        return result

    def combinate(self, start, candidates, temp, remain, result):
        if remain < 0:
            return
        elif remain == 0:
            result.append(temp.copy())
            return 
        else:
            for i in range(start, len(candidates)):
                if candidates[i]>remain:
                    break
                temp.append(candidates[i])
                self.combinate(i,candidates,temp,remain-candidates[i],result)
                temp.pop()

                