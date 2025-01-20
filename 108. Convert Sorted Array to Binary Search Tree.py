''' logic 1:
- recursion
  - take the mid as root
  - slice the array at mid and repeat '''
class Solution(object):
    def sortedArrayToBST(self, nums):
        if not nums:
            return None
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root

''' logic 2:
- slicing takes memory
- more efficient way is to keep track of indices
- helper function ( left , right )
  - give none if left > right - base condition
  - find mid and make it the root
  - recursively call helper
  - call helper from with left == 0 and right == len(nums)-1 '''
class Solution(object):
    def sortedArrayToBST(self, nums):
        def helper(left, right):
            if (left > right):
                return None
            mid = (left + right) // 2
            root = TreeNode(nums[mid])

            root.left = helper(left, mid-1)
            root.right = helper(mid+1, right)

            return root
        return helper(0, len(nums)-1)
