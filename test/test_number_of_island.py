from solution.number_of_island import Solution


class TestClass:
    def test_1(self):
        grid = [['1', '1', '1', '1', '0'],
                ['1', '1', '0', '1', '0'],
                ['1', '1', '0', '0', '0'],
                ['0', '0', '0', '0', '0']]
        solu = Solution()
        ans = solu.numIslands(grid)
        assert ans == 1

    def test_2(self):
        grid = [['0', '0', '0', '1', '1'],
                ['1', '1', '0', '0', '0'],
                ['1', '1', '0', '0', '0'],
                ['0', '0', '1', '0', '0']]
        solu = Solution()
        ans = solu.numIslands(grid)
        assert ans == 3

    def test_3(self):
        grid = [['0']]
        solu = Solution()
        ans = solu.numIslands(grid)
        assert ans == 0

    def test_4(self):
        grid = [[]]
        solu = Solution()
        ans = solu.numIslands(grid)
        assert ans == 0

    def test_5(self):
        grid = [['1', '1', '1', '1'],
                ['1', '1', '1', '1'],
                ['1', '1', '1', '1']]
        solu = Solution()
        ans = solu.numIslands(grid)
        assert ans == 1

    def test_6(self):
        grid = [['1', '1', '1', '1'],
                ['0', '0', '0', '0'],
                ['1', '1', '1', '1']]
        solu = Solution()
        ans = solu.numIslands(grid)
        assert ans == 2

    def test_7(self):
        grid = [['1', '1', '1'],
                ['1', '0', '1'],
                ['1', '1', '1']]
        solu = Solution()
        ans = solu.numIslands(grid)
        assert ans == 1

    def test_8(self):
        grid = [['0', '0', '0'],
                ['0', '1', '0'],
                ['0', '0', '0']]
        solu = Solution()
        ans = solu.numIslands(grid)
        assert ans == 1

    def test_9(self):
        grid = [['0', '0', '0'],
                ['0', '0', '0'],
                ['0', '0', '0']]
        solu = Solution()
        ans = solu.numIslands(grid)
        assert ans == 0

    def test_10(self):
        grid = [['1', '1', '0'],
                ['1', '0', '0'],
                ['1', '1', '0']]
        solu = Solution()
        ans = solu.numIslands(grid)
        assert ans == 1
