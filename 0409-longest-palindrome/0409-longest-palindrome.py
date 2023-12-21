from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        result = 0
        counter = Counter(s)
        
        for count in counter.values():
            result += (count // 2) * 2
        
        if result < len(s):
            result += 1
                
        return result