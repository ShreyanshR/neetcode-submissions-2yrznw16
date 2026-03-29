class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        length = 0
        visit = set()

        queue.append((0,0))
        visit.add((0,0))

        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()

                if r == rows - 1 and c == cols - 1:
                    return length

                directions = [[1,0],[-1,0],[0,1],[0,-1]]

                for dr, dc in directions:
                    r, c = r + dr, c + dc

                    if (min(r,c) < 0 or
                        r == rows or c == cols or
                        (r,c) in visit or
                        grid[r][c] == 1
                    ):
                        continue

                    queue.append((r,c))
                    visit.add((r,c))
                    

            length += 1

        return -1
        