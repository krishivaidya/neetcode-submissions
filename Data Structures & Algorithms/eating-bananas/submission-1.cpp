class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {

        int l = 1; 
        int r = *std::max_element(piles.begin(), piles.end());
        int res = r;
        while (l <= r){

            int k = (l + r) / 2;
            long long total_t = 0;
            for(int i = 0; i < piles.size(); i++){
                total_t += ceil(static_cast<double>(piles[i])/ k);
            }

            if(total_t > h){
                l = k + 1; 
            } else {
                res = k;
                r = k - 1;
            }
        }
        return res;
        
    }
};
