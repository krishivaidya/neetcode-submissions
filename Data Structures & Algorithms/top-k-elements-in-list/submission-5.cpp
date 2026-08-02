class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        map<int, int> m;
        for(int i = 0; i < nums.size(); i++){
           if(m.find(nums[i]) != m.end()){ 
            m[nums[i]]++; 
            } else{ 
                m[nums[i]]++; 
            }
        }


        vector<int> result;

        for(int i = 0; i < k; i++){
        int max = -1;
        int ind = 0;
            for(auto p : m){
                if(p.second > max){
                    max = p.second;
                    ind = p.first;
                }
                 
            }
            
            result.push_back(ind);
            m[ind] = -1;

            
        }

        return result;
        }

        
    };
