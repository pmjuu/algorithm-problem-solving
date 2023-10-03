class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        prevColor = image[sr][sc]
        
        def fill(r: int, c: int):
            if (r < 0 or r >= len(image) or c < 0 or c >= len(image[0]) or image[r][c] != prevColor):
                return
            
            image[r][c] = color
            
            fill(r - 1, c)
            fill(r + 1, c)
            fill(r, c - 1)
            fill(r, c + 1)
        
        if (color != prevColor): fill(sr, sc)
        
        return image