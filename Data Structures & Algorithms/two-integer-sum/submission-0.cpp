class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int first_index = 0;
        int second_index = 0;
        vector<int> return_array;
        for(int i = 0; i < nums.size(); i++){
            for(int j = i + 1; j < nums.size(); j++){
                if(nums[i] + nums[j] == target){
                    first_index = i;
                    second_index = j;
                }
            }
        }
        return_array.push_back(first_index);
        return_array.push_back(second_index);
        return return_array;
    }
};
