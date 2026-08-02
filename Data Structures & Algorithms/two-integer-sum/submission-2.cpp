class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map <int, int> m; 
        for(int i = 0; i < nums.size(); i++){
            int tofind = target - nums[i];
            if (m.find(tofind) == m.end()){
                m[nums[i]] = i;
            } else{
                if(i < m[tofind]){
                    return {i, m[tofind]};
                } else{
                    return {m[tofind] , i};
                }
            }

        }
        return {};
    }
};
