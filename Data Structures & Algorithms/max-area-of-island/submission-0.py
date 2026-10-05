class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            grid[j][i] = 0
            size = 1

            # left
            if i > 0 and grid[j][i-1] == 1:
                grid[j][i-1] = 0
                size += dfs(i-1, j)
            
            # right:
            if i < len(grid[0]) - 1 and grid[j][i+1] == 1:
                grid[j][i+1] = 0
                size += dfs(i+1, j)
            
            # up
            if j > 0 and grid[j-1][i] == 1:
                grid[j-1][i] = 0
                size += dfs(i, j-1)
            
            # down
            if j < len(grid) - 1 and grid[j+1][i] == 1:
                grid[j+1][i] = 0
                size += dfs(i, j+1)
            
            return size
        
        max_size = 0

        for y, row in enumerate(grid):
            for x, _ in enumerate(row):
                if grid[y][x] == 1:
                    max_size = max(max_size, dfs(x, y))
        
        return max_size
