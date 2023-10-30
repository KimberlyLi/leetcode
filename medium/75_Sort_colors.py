class Solution(object):
    def swap(self, left, right, nums):
        temp = nums[left]
        nums[left] = nums[right]
        nums[right] = temp

    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left = 0
        zero = 0
        two = len(nums) - 1
        while left < len(nums) and left <= two:
            if nums[left] == 0:
                self.swap(left, zero, nums)
                zero += 1
                left += 1
            elif nums[left] == 2:
                self.swap(left, two, nums)
                two = two - 1
            else:
                left += 1
                
if __name__ == '__main__':
    test_sol = Solution()
    nums = [2,0,2,1,1,0]
    test_sol.sortColors(nums)
    print(nums)