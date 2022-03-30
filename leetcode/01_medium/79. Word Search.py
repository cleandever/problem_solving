"""
https://leetcode.com/problems/word-search/
"""
class Solution:
    def exist(self, board, word):
        m = len(board)
        n = len(board[0])
        path = set()

        def bt(row, col, idx):
            if idx >= len(word):
                return True

            # board boundary check
            if not (0 <= row < m):
                return False
            if not (0 <= col < n):
                return False

            if board[row][col] != word[idx]:
                return False

            if (row, col) in path:
                return False

            path.add((row, col))
            res = bt(row - 1, col, idx + 1) or bt(row + 1, col, idx + 1) or bt(row, col - 1, idx + 1) or bt(row,
                                                                                                            col + 1,
                                                                                                            idx + 1)
            path.remove((row, col))
            return res

        for r in range(m):
            for c in range(n):
                if bt(r, c, 0):
                    return True
        return False