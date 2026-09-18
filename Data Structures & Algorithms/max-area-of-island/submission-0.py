class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()

        def dfs(r, c):
            if r < 0 or  c < 0 or r >= rows or c >= cols or (r, c) in visited or grid[r][c] == 0:
                return False
            
            visited.add((r,c))

            dfs(r+1, c)
            dfs(r, c+1)
            dfs(r-1, c)
            dfs(r, c-1)
    
        ans = 0
        for i in range(rows):
            for j in range(cols):
                before = len(visited)
                if (i, j) not in visited and grid[i][j] == 1:
                    dfs(i, j)
                    after = len(visited)
                    ans = max(after-before, ans)
        return ans