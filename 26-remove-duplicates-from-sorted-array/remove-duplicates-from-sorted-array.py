class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        curr_v = -101
        pt = 0

        for i in nums:
            if i > curr_v:
                nums[pt] = i
                curr_v = i
                pt += 1

        return pt
        