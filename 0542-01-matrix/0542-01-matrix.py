from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        result = [[float('inf')] * cols for _ in range(rows)]
        
        queue = deque()
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        for row in range(rows):
            for col in range(cols):
                if mat[row][col] == 0:
                    result[row][col] = 0
                    queue.append((row, col))
        
        while queue:
            row, col = queue.popleft()
            
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                
                if 0 <= nr < rows and 0 <= nc < cols and result[nr][nc] > result[row][col] + 1:
                    result[nr][nc] = result[row][col] + 1
                    queue.append((nr, nc))
        
        return result