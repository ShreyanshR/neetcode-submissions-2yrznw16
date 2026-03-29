class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        ROWS, COLS = len(grid), len(grid[0])
        isIsland = 0

        def DFS(r, c):
            if (r < 0 or c < 0 or 
                r >= ROWS or c >= COLS or
                grid[r][c] == "0"
                ):
                return 
            
            grid[r][c] = "0" # we visited the island

            for drows, dcols, in directions:
                DFS(r + drows, c + dcols)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    DFS(r,c)
                    isIsland += 1

        
        return isIsland