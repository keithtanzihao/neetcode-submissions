# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        if len(nums) == 0:
            return

        mid = len(nums) // 2
        origin = TreeNode(val=nums[mid])

        if len(nums) == 1:
            return origin
    
        origin.left = self.sortedArrayToBST(nums[:mid])
        origin.right = self.sortedArrayToBST(nums[mid+1:])

        return origin