class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        s_pt = 0
        e_pt = len(nums) - 1

        while s_pt <= e_pt:
            mid_pt = (s_pt + e_pt) // 2
            mid_val = nums[mid_pt]

            print(f"Before s:{s_pt:<5} e:{e_pt:<5} mid P: {mid_pt:<5} mid V:{mid_val}")

            if mid_val == target:
                return mid_pt
            elif mid_val > target:
                e_pt = mid_pt - 1
            else:
                s_pt = mid_pt + 1

            print(f"After  s:{s_pt:<5} e:{e_pt:<5}")
            print("\n")


        return s_pt


        
        

    
        