class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.size() != t.size()){
            return false;
        }

        unordered_map <char, int> frequency;
        for(int i = 0; i < s.size(); i++){
            frequency [s[i]]++;
        }
        
        for(int i = 0; i < t.size(); i++){
            frequency [t[i]]--;
            if(frequency[t[i]] < 0){
                return false;
            }
        }
        return true;
    }
};
