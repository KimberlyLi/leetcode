"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2,2,1]
Output: 1

Solution:
since we know there is exactly 2 of each element except for 1, we can utilize XOR to find the 1 element
XOR is commutative and associative so there is no need for sorting

1. A number XOR itself is 0: a ^ a = 0
2. 0 XOR a number is just that number: 0 ^ a = a
3. XOR is commutative: a ^ b = b ^ a.

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        single_number = 0
        for num in nums:
            single_number = num ^ single_number

        return single_number



if __name__ == '__main__':
    test_sol = Solution()
    assert test_sol.singleNumber([2, 2, 1]) == 1
    assert test_sol.singleNumber([4, 1, 2, 1, 2]) == 4
    assert test_sol.singleNumber([1]) == 1
