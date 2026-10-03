class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid:
            return 0

        directions = [(-1,0), (1,0), (0,1), (0,-1)]
        visited = set()
        rows = len(grid)
        columns = len(grid[0])

        def bfs(i, j):
            queue = deque()
            queue.append((i,j))
            visited.add((i,j))
            
            while queue:
                r, c = queue.popleft() # bc we are doing bfs, change to .pop for dfs(iterative-style)

                for x,y in directions:
                    newr = r + x
                    newc = c + y

                    if newr in range(rows) and newc in range(columns) and grid[newr][newc] == "1" and (newr, newc) not in visited:

                        queue.append((newr, newc))
                        visited.add((newr, newc))
            



        answers = 0
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == "1" and (i,j) not in visited:
                    bfs(i , j)
                    answers += 1
        
        return answers
        