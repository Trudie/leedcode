"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.
Example 1:

Input:
11110
11010
11000
00000

Output: 1

Example 2:

Input:
11000
11000
00100
00011

Output: 3
[0,0] [1,0] [0,1]
[1,0] [0,1] [1,1]
[0,1] [1,1]

"""


class BFS():
    def __init__(self, grid):
        self.grid = grid
        self.n_row = len(grid)
        self.n_col = len(grid[0])
        self.size = self.n_row * self.n_col
        self.queue = [[0, 0] for _ in range(self.size)]
        self.front = -1
        self.rear = -1

    def isEmpty(self):
        return self.front == self.rear == -1

    def isFull(self):
        return self.rear == self.size - 1

    def push(self, val: list):
        if self.isEmpty():
            self.front += 1
        if self.isFull():
            return False
        self.rear += 1
        self.queue[self.rear] = val

    def pop(self):
        if self.isEmpty():
            return False
        self.front += 1
        if self.front - 1 == self.rear:
            self.front = -1
            self.rear = -1
        return

    def peek(self):
        return self.queue[self.front]

    def traverse(self, row, col):
        """
        queue[root, child_node, child_node,...]
        for grid the child_node will be 4 directions
        :param row: root_row
        :param col: root_col
        :return:
        """
        # push the root
        self.push([row, col])
        while not self.isEmpty():
            row, col = self.peek()
            # mark been visited in queue
            if self.grid[row][col] == '1':
                self.grid[row][col] = '0'
                # push the neighbor
                for i, j in [(row + 1, col), (row, col + 1), (row - 1, col), (row, col - 1)]:
                    if 0 <= i < self.n_row and 0 <= j < self.n_col and self.grid[i][j] == '1':
                        self.push([i, j])
                self.pop()

        return self.grid


class Solution:
    def numIslands(self, grid) -> int:
        if not grid or not grid[0]:
            return 0
        n_row, n_col = len(grid), len(grid[0])
        n_island = 0

        for i in range(n_row):
            for j in range(n_col):
                if grid[i][j] == '1':
                    bfs = BFS(grid)
                    grid = bfs.traverse(i, j)
                    print('='*10)
                    n_island += 1

        return n_island
