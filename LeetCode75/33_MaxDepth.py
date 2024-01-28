# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if(root == None):
            return 0     
        leftDepth = self.maxDepth(self, root.left) + 1
        rightDepth = self.maxDepth(self, root.right) + 1

        return max(leftDepth, rightDepth)


def setup()-> TreeNode:
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    return root


def printTree(root: TreeNode):
    if(root != None):
        print(root.val)
        printTree(root.left)
        printTree(root.right)
    else:
        print("Null")

    return

def main():
    #vals = [3,9,20,None,None,15,7]
    test = Solution
    root = setup()
    #printTree(root)
    print(test.maxDepth(test, root))

if(__name__ == "__main__"):
    main()