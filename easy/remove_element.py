class Solution:
    def removeDuplicates(self, nums):
        i = 0
        length = len(nums)
        while i < length:
            if nums[i] == nums[i+1]:
                nums.remove(nums[i])
                length = length - 1
            else:
                i = i+1
        return len(nums)