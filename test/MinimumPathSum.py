#Given a m x n grid filled with non-negative numbers, 
#find a path from top left to bottom right which minimizes the sum of all numbers along its path.
#Note: You can only move either down or right at any point in time.
#Example 1:
#[[1,3,1],
# [1,5,1],
# [4,2,1]]
#Given the above grid map, return 7. Because the path 1→3→1→1→1 minimizes the sum.
class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        m, n= len(grid), len(grid[0])
        if n==0:
            return 0
        for i in range(1,n):
            grid[0][i] = grid[0][i-1] + grid[0][i]
        for i in range(1,m):
            grid[i][0] = grid[i-1][0] + grid[i][0]
        for i in range(1,m):
            for j in range(1,n):
                grid[i][j] = min(grid[i-1][j],grid[i][j-1]) + grid[i][j]
        return grid[-1][-1]