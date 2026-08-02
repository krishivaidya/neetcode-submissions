#include "unordered_map"
class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.size() != t.size()){
            return false;
        }
        map <char, int> m;
        for(int i = 0; i < s.size(); i++){
                m[s[i]]++;
            }
        for(int i = -0 ; i <t.size(); i++){
                m[t[i]]--;
        }
        
        for(int i = 0 ; i <s.size(); i++){
            if(m[t[i]] == -1 || m[s[i]] != 0){
                return false;
            } 
        }
        return true;
    }
};
