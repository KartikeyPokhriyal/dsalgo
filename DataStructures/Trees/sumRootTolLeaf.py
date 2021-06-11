class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        def preorder(root, currentSum):

            if root:
                currentSum += str(root.val)
                if not root.left and not root.right:
                    self.ans += int(currentSum, 2)
                    currentSum = ''

                preorder(root.left, currentSum)
                preorder(root.right, currentSum)

        self.ans = 0
        currentSum = ''
        preorder(root, currentSum)

        return self.ans