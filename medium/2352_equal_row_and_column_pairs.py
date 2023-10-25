"""
Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.
A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1
Explanation: There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]
"""

from collections import defaultdict


class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = defaultdict(int)
        for row in grid:
            rows[tuple(row)] += 1

        return sum(rows[col] for col in zip(*grid))

# if __name__ == '__main__':
#     test_sol = Solution()
#     test_input = [[3, 2, 1], [1, 7, 6], [2, 7, 7]]
#     print(test_sol.equalPairs(test_input))
#     assert test_sol.equalPairs(test_input) == 1
