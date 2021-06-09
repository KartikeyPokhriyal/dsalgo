class TreeNode:
    def __init__(self, val):
        self.val = val


def increasingBST(self, root: TreeNode) -> TreeNode:
    def inorder(node):
        if node:
            inorder(node.left)
            node.left = None
            self.curr.right = node
            self.curr = node
            inorder(node.right)

        ans = self.curr = TreeNode(None)
        inorder(root)
        return ans.right