class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        # hash solution
        # r = {}
        # for i in nums:
        #     if i not in r:
        #         r[i] = 1
        #     else:
        #         r[i] += 1
            
        #     if r[i] > (len(nums) / 2):
        #         return i
        i = 1
        c = nums[0]
        v = 1
        while i < len(nums):
            if v == 0:
                c = nums[i]
                v += 1

            elif nums[i] == c:
                v += 1

            elif nums[i] != c:
                v -= 1  
            i += 1
        return c
            