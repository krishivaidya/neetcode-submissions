class Solution {
private: 
    int helper(vector<int> & nums, int target, int start, int end){

        int mid = start + (end - start) / 2;
        while (start <= end){
            if(target < nums[mid]){
                end = mid - 1; 
            return helper(nums, target, start, end);
        } else if(target > nums[mid]){
            start = mid + 1;
            return helper(nums, target, start, end);
        } else if (target == nums[mid]){
            return mid;
        }
        }
        return -1;

    }


public:

    int search(vector<int>& nums, int target) {
      
      return helper(nums, target, 0, nums.size() - 1);
    }   
};
