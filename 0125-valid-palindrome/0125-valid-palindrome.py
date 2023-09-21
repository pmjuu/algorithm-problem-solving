class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphaList = list(filter(str.isalnum, s))
        string = ''.join(alphaList).lower()
    
        for i in range(len(string) // 2):
            if (string[i] != string[-1 - i]):
                return False
        
        return True