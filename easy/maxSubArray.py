class Solution:
    def maxSubArray(self, nums):
        if len(nums) == 1:
            return nums[0]
        elif max(nums) <=0:
            return max(nums)
        else:
            local_max = nums[0]
            global_max = nums[0]
            for i in range(1,len(nums)):
                local_max = max(nums[i], local_max + nums[i])
                if local_max > global_max:
                    global_max = local_max
            return global_max