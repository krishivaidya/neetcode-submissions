class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        if(nums.empty()){
            return false;
        }
        for(int i = 0; i <= nums.size(); i++){
            int compare = nums[i];
            for(int j = i + 1; j <= nums.size() ; j++){
                if(compare == nums[j]){
                    return true;
                }
            }
        }
        return false;
    }
};