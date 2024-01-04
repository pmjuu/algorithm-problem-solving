class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        row_num = len(grid)
        col_num = len(grid[0])
        
        def removeLand(row, col):
            if row < 0 or row >= row_num or col < 0 or col >= col_num or grid[row][col] == "0":
                return
            
            grid[row][col] = "0"
            
            removeLand(row - 1, col)
            removeLand(row + 1, col)
            removeLand(row, col + 1)
            removeLand(row, col - 1)
            
        for i in range(row_num):
            for j in range(col_num):
                if grid[i][j] == "1":
                    removeLand(i, j)
                    count += 1
        
        return count