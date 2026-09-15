class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        pt1 = m-1
        pt2 = n-1
        i = len(nums1)-1

        if not nums2:
            return nums1

        while pt1 >= 0 and pt2 >= 0:
            v1 = nums1[pt1]
            v2 = nums2[pt2]
            if v2 >= v1:
                nums1[i] = v2
                pt2-=1
            else:
                nums1[i] = v1
                pt1-=1
            i-=1
        
        if pt2 >= 0:
            nums1[:i+1] = nums2[:pt2+1] 

        return nums1
        
