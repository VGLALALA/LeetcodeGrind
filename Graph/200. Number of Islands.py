def numIslands(grid):
    rows, cols = len(grid), len(grid[0])

    def DFS(grid, start, visited):
        stack = []
        stack.append(start)
        rows, cols = len(grid), len(grid[0])
        neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while stack:
            r, c = stack.pop()
            if grid[r][c] == "0" or (r, c) in visited:
                continue
            visited.add((r, c))
            for neighbor in neighbors:
                ar, ac = neighbor
                nr, nc = r + ar, c + ac
                if nr < 0 or nr > rows - 1 or nc < 0 or nc > cols - 1:
                    continue
                new_state = (nr, nc)
                stack.append(new_state)
        return visited

    islands = 0
    visited = set()
    for i in range(rows):
        for j in range(cols):
            if (i, j) not in visited and grid[i][j] == "1":
                visited = DFS(grid, (i, j), visited)
                print(visited)
                islands += 1
    return islands

def numIslands2(grid):
    rows, cols = len(grid), len(grid[0])

    def DFS(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1':
            return
        grid[r][c] = '0'
        DFS(r + 1, c)
        DFS(r - 1, c)
        DFS(r, c + 1)
        DFS(r, c - 1)

    islands = 0
    visited = set()
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "1":
                islands += 1
                DFS(i, j)
    return islands


grid = [["1","1","1","1","1","1"],
        ["1","0","0","0","0","1"],
        ["1","0","1","1","0","1"],
        ["1","0","0","0","0","1"],
        ["1","1","1","1","1","1"]]
print(numIslands(grid))

