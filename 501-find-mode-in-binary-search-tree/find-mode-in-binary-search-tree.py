# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMode(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        self.prev = None
        self.count = 0
        self.maxval = 0
        self.mode = []

        #inorder and baki logic
        def inorder(node):
            if not node:
                return
            inorder(node.left)

            if self.prev == node.val:
                self.count = self.count + 1
            else:
                self.count = 1
            if self.count > self.maxval:
                self.maxval = self.count
                self.mode = [node.val]
            elif self.count == self.maxval:
                self.mode.append(node.val)
            
            self.prev = node.val

            inorder(node.right)
        inorder(root)
        return self.mode