class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(m: int, n: int):
            if m < 0 or n < 0 or m >= len(grid) or n >= len(grid[m]) or grid[m][n] != '1':
                return

            grid[m][n] = '#'
            dfs(m - 1, n)
            dfs(m, n - 1)
            dfs(m + 1, n)
            dfs(m, n + 1)

        res = 0
        for m in range(len(grid)):
            for n in range(len(grid[m])):
                if grid[m][n] == '1':
                    dfs(m, n)
                    res += 1
        
        return res