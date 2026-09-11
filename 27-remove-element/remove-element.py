class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pt = 0
        while pt < len(nums):
            if val == nums[pt]:
                nums.pop(pt)
            else:
                pt += 1
        
        return pt
        