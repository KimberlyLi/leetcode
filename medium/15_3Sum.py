from itertools import combinations
from collections import defaultdict

'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.



Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Approach:
1. sort into a positive, negative and zero list for iteration, as well as sets for positive and negative for O(1) lookup
2. add (0,0,0) if 3 or more zeros
3. if one or more 0 in nums, look for complements. I.e. (-1, 0 ,1)
4. per pair of positive and negatives, look for the complement in the set i.e (-1, -2, 3)
'''

class Solution(object):
    def threeSum(self, nums):
        """
        :param nums: List[int]
        :return: List[List[int]]
        """
        p = []
        n = []
        z_count = 0
        p_set = set()
        n_set = set()
        ret = set()
        for num in nums:
            if num > 0:
                p.append(num)
                p_set.add(num)
            elif num < 0:
                n.append(num)
                n_set.add(num)
            else:
                z_count += 1
        if z_count >= 3:
            ret.add((0, 0, 0))
        if z_count > 0:
            for num in p:
                if -1 * num in n_set:
                    ret.add(tuple(sorted([num, 0, -1 * num])))
            for num in n:
                if -1 * num in p_set:
                    ret.add((tuple(sorted([num, 0, -1 * num]))))

        for comb in combinations(p, 2):
            if -1 * (comb[0] + comb[1]) in n_set:
                ret.add(tuple(sorted([comb[0], comb[1], -1 * (comb[0] + comb[1])])))

        for comb in combinations(n, 2):
            if -1 * (comb[0] + comb[1]) in p_set:
                ret.add(tuple(sorted([comb[0], comb[1], -1 * (comb[0] + comb[1])])))
        return [list(triple) for triple in ret]


if __name__ == '__main__':
    test_sol = Solution()
    assert (set(tuple(triple) for triple in test_sol.threeSum([-1, 0, 1, 2, -1, -4]))) == {(-1, -1, 2), (-1, 0, 1)}
