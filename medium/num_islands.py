"""
Problem: Count Number of Islands With Sum Divisible by K

You are given a grid of integers grid with dimensions m x n and an integer k.
Two cells belong to the same island if they are adjacent up, down, left, or right and both have values > 0.

For each island:
Compute the sum of its values.
Count how many islands have a total sum divisible by k.

Return that count.
"""

# Output should be: 2
grid = [
  [3, 0, 1],
  [3, 3, 0],
  [0, 0, 6]
]
k = 3

def count_islands_divisible(grid, k):
    m, n = len(grid), len(grid[0])
    visited = [[False]*n for _ in range(m)]
    
    def dfs(r, c):
        if r<0 or r>=m or c<0 or c>=n or visited[r][c] or grid[r][c]==0:
            return 0
        visited[r][c] = True
        s = grid[r][c]
        s += dfs(r+1, c)
        s += dfs(r-1, c)
        s += dfs(r, c+1)
        s += dfs(r, c-1)
        return s
    
    count = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] > 0 and not visited[i][j]:
                total = dfs(i,j)
                if total % k == 0:
                    count += 1
    return count

print(count_islands_divisible(grid, k))