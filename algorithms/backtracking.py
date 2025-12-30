from algorithms.base import Algorithm

class BacktrackingAlgorithm(Algorithm):
    def run(self):
        board = [-1] * self.n

        def is_safe(row, col):
            for r in range(row):
                if board[r] == col or abs(board[r] - col) == abs(r - row):
                    return False
            return True

        def backtrack(row):
            if row == self.n:
                yield board.copy()
                return

            for col in range(self.n):
                if is_safe(row, col):
                    board[row] = col
                    self.steps += 1
                    yield board.copy()

                    yield from backtrack(row + 1)

                    board[row] = -1
                    self.steps += 1
                    yield board.copy()

        yield from backtrack(0)
