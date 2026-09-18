from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])

        queue = deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    queue.append((i, j, 0))
        
        while queue:
            ii, jj, distance = queue.popleft()
            if ii + 1 < rows and grid[ii+1][jj] == 2147483647:
                grid[ii+1][jj] = distance + 1
                queue.append((ii+1, jj, distance+1))
            if jj + 1 < cols and grid[ii][jj+1] == 2147483647:
                grid[ii][jj+1] = distance + 1
                queue.append((ii, jj+1, distance+1))
            if jj - 1 >= 0 and grid[ii][jj-1] == 2147483647:
                grid[ii][jj-1] = distance + 1
                queue.append((ii, jj-1, distance+1))
            if ii - 1 >= 0 and grid[ii-1][jj] == 2147483647:
                grid[ii-1][jj] = distance + 1
                queue.append((ii-1, jj, distance+1))