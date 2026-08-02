class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""
        for i in s:
            if i.isalnum():
                new_s += i.lower()
        
        l = 0
        r = len(new_s) - 1
        while l < r:
            if new_s[l] != new_s[r]:
                return False 
            l += 1
            r -= 1
        
        return True
    
   

        



        