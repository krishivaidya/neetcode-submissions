class Solution {
public:
    bool isPalindrome(string s) {
        int left = 0;
        int right = s.size() - 1;

        while(left < right){

            while(left < right && !isValid(s[left])){
                left++;
            }

            while(left < right && !isValid(s[right])){
                right--;
            }

            if(tolower(s[left]) != tolower(s[right])){
                return false;
            }
            
            left++;
            right--;
        }
        return true;
        
    }

    bool isValid(char c){
        if(('0' <= c && c <= '9') || ('a' <= c && c <= 'z') || ('A' <= c && c <= 'Z' )){
            return true;
        } else{
            return false;
        }
    }
};
