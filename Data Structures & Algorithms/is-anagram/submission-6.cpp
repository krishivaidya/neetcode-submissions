class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.size() != t.size()){
            return false;
        } 

        unordered_map<int, int> m;
        for(int i = 0; i < s.size(); i++ ){
            m[s[i]]++;
        }

        for(int j = 0; j < s.size(); j++ ){
            m[t[j]]--;
            if(m[t[j]] == -1){
                return false;
            }

           
        }
        return true;

   

        
    }
};
