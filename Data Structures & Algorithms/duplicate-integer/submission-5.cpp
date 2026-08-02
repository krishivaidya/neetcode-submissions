class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        if(nums.size() == 0){
            return false;
        }
            std::unordered_set<int> check;
        for(int i = 0; i <= nums.size() ; i++){
            if(check.find(nums[i]) != check.end()){
                return true;
            } else{
                check.insert(nums[i]);
            }
           
        }
        return false;
        
    
    }
};