class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        result = ransomNote
        
        for char in magazine:
            if char in ransomNote:
                result = result.replace(char, '', 1)
        
        return not result