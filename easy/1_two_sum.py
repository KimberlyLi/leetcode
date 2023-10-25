"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Edge case:
Solution:
Iterate through nums list and create a dictionary using the num as a key, and the index as value. Then iterate through the
list again, and check if the (target - num) exists in the dictionary. Make sure to account for if the index is itself

Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = dict((value, idx) for idx, value in enumerate(nums))
        for idx, num in enumerate(nums):
            if (target - num) in d and idx != d[target - num]:
                return [idx, d[target - num]]


# if __name__ == '__main__':
#     test_sol = Solution()
#     input_list = [3, 2, 4]
#     target = 6
#     print(test_sol.twoSum(input_list, target))
