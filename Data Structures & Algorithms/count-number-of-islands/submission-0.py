class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        def dfs(r, c):
            if r < 0 or  c < 0 or r >= rows or c >= cols or (r, c) in visited or grid[r][c] == "0":
                return False
            
            visited.add((r,c))

            dfs(r+1, c)
            dfs(r, c+1)
            dfs(r-1, c)
            dfs(r, c-1)
    
        ans = 0
        for i in range(rows):
            for j in range(cols):
                
                if (i, j) not in visited and grid[i][j] == "1":
                    dfs(i, j)
                    ans += 1
        return ans