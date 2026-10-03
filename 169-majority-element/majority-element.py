class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        r = {}
        for i in nums:
            if i not in r:
                r[i] = 1
            else:
                r[i] += 1
            
            if r[i] > (len(nums) / 2):
                return i