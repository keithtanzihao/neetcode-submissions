class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        s_pt = 0
        e_pt = len(nums) - 1

        while s_pt <= e_pt:
            mid_pt = (s_pt + e_pt) // 2
            mid_val = nums[mid_pt]

            if mid_val == target:
                return mid_pt
            elif mid_val > target:
                e_pt = mid_pt - 1
            else:
                s_pt = mid_pt + 1

        return s_pt


        
        

    
        