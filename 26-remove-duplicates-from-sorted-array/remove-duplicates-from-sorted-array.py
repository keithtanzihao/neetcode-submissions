class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        num_dict = {}
        i = 0

        while i < len(nums):
            n = nums[i]
            if n not in num_dict:
                num_dict[n] = n
                i+=1
            else:
                nums.pop(i)

        return len(nums)
        