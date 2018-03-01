#Given a collection of candidate numbers (C) and a target number (T), 
#find all unique combinations in C where the candidate numbers sums to T.
#Each number in C may only be used once in the combination.
#Note:
#All numbers (including target) will be positive integers.
#The solution set must not contain duplicate combinations.
#For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8, 
#A solution set is: 
#[
#  [1, 7],
#  [1, 2, 5],
#  [2, 6],
#  [1, 1, 6]
#]
class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        temp, start = [], 0
        resultset =set()
        self.combinate(start,candidates,temp, target, resultset)
        result = []
        for i in resultset:
            result.append(list(i))
        return result

    def combinate(self, start, candidates, temp, remain, resultset):
        if remain < 0:
            return
        elif remain == 0:
            resultset.add(tuple(temp))
            return 
        else:
            for i in range(start, len(candidates)):
                if candidates[i]>remain:
                    break
                temp.append(candidates[i])
                self.combinate(i+1,candidates,temp,remain-candidates[i],resultset)
                temp.pop()

#public List<List<Integer>> combinationSum2(int[] nums, int target) {
#    List<List<Integer>> list = new ArrayList<>();
#    Arrays.sort(nums);
#    backtrack(list, new ArrayList<>(), nums, target, 0);
#    return list;
    
#}

#private void backtrack(List<List<Integer>> list, List<Integer> tempList, int [] nums, int remain, int start){
#    if(remain < 0) return;
#    else if(remain == 0) list.add(new ArrayList<>(tempList));
#    else{
#        for(int i = start; i < nums.length; i++){
#            if(i > start && nums[i] == nums[i-1]) continue; // skip duplicates key point
#            tempList.add(nums[i]);
#            backtrack(list, tempList, nums, remain - nums[i], i + 1);
#            tempList.remove(tempList.size() - 1); 
#        }
#    }
#} 