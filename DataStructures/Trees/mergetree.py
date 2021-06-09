class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def mergetree(self, treeOne, treeTwo):
    if treeOne and treeTwo:
        mergedTree = TreeNode(treeOne.val + treeTwo.val)
        mergedTree.left = self.mergetree(treeOne.left, treeTwo.left)
        mergedTree.right = self.mergetree(treeOne.right, treeTwo.right)
        return mergedTree

    return treeOne or treeTwo