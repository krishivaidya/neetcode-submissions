class Solution:
    def isPalindrome(self, s: str) -> bool:
       
        new_s = ""
        for i in s:
            if i.isalnum():
                c = i.lower()
                new_s += c
        length = len(new_s)
        for i in range(length):
            if new_s[i] != new_s[length - 1 - i]:
                return False 

        return True


        