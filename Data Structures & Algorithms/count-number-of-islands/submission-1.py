class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]

        answer = 0
        visited = set()
        queue = deque()
        
        def bfs(i , j):
            visited.add((i , j))

            queue.append((i,j))

            while queue:
                checker = queue.popleft()

                for x,y in dirs:
                    if x + checker[0] in range(len(grid)) and y + checker[1] in range(len(grid[0])) and grid[x + checker[0]][y + checker[1]] == "1" and  (x + checker[0] , y + checker[1]) not in visited:
                        queue.append((x + checker[0] , y + checker[1]))
                        visited.add((x + checker[0] , y + checker[1]))


            
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if grid[i][j] == "1" and (i , j) not in visited:
                    bfs(i , j)
                    answer += 1

        return answer
            