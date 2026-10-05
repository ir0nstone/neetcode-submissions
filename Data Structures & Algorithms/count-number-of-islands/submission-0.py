class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            # left
            if i > 0 and grid[j][i-1] == '1':
                grid[j][i-1] = '0'
                dfs(i-1, j)
            
            # right:
            if i < len(grid[0]) - 1 and grid[j][i+1] == '1':
                grid[j][i+1] = '0'
                dfs(i+1, j)
            
            # up
            if j > 0 and grid[j-1][i] == '1':
                grid[j-1][i] = '0'
                dfs(i, j-1)
            
            # down
            if j < len(grid) - 1 and grid[j+1][i] == '1':
                grid[j+1][i] = '0'
                dfs(i, j+1)
        
        islands = 0

        for y, row in enumerate(grid):
            for x, _ in enumerate(row):
                if grid[y][x] == '1':
                    islands += 1
                    dfs(x, y)
        
        return islands
