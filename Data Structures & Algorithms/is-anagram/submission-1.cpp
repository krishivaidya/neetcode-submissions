class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.length() != t.length()){
            return false;
        }
        std::unordered_map<char, int> freq;
        for(int i = 0; i < s.length(); i++){
            char c = s[i]; 
            freq[c]++;
        }
        for(int i = 0; i < t.length(); i++){
            char c = t[i]; 
            freq[c]--;
            if(freq[c] < 0){
                return false;
            }

        }
        return true;

    }
};
