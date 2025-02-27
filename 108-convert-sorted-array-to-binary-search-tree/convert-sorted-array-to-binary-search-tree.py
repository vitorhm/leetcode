# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.buildTree(nums)
        
    def buildTree(self, nums: List[int]) -> Optional[TreeNode]:
        index = len(nums) // 2
        node = TreeNode(nums[index])

        left_array = nums[:index]
        if len(left_array) > 0:
            node.left = self.buildTree(left_array)
        
        right_array = nums[index + 1:]
        if len(right_array) > 0:
            node.right = self.buildTree(right_array)

        return node