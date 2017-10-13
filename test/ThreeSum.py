class Solution {
public:
        vector<vector<int> > threeSum(vector<int>& nums) {
            sort(nums.begin(),nums.end());
            vector<vector<int> > result;
            for(int i=0;i!=nums.size();){
                int start=i+1;
                int end = nums.size()-1;
                while(start <end){
                    if (nums[i]+nums[start]+nums[end]==0){
                        result.push_back({nums[i],nums[start],nums[end]});
                        start++;
                        end--;
                        while(start<end && nums[start]==nums[start-1])
                            start++;
                        while(start <end && nums[end]==nums[end+1])
                            end--;
                    }
                    else if (nums[i]+nums[start]+nums[end]>0){
                        end--;
                    }
                    else
                        start++;
                }
                i++;
                while (i<nums.size() && nums[i]==nums[i-1])
                    i++;
            }
            return result;
        }
};