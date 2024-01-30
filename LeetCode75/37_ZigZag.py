# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        if(root == None):
            return 0
        currMax = max(self.left(self, root.left), self.right(self, root.right))
        return max(currMax, self.longestZigZag(self, root.left), self.longestZigZag(self, root.right))

    def left(self, root: TreeNode) -> int:
        if(root == None):
            return 0
        return self.right(self, root.right) +1
    
    def right(self, root: TreeNode) ->int:
        if(root == None):
            return 0
        return self.left(self, root.left) +1
    
#### Testing Functions #####
def setup(vals: list)->TreeNode:
    if(vals == []):
        return None
    #root = TreeNode(vals[0])
    root = buildTree(vals, len(vals), 0, 0)
    return root

def buildTree(vals:list, length:int, depth: int, rIndex: int)->TreeNode:
    root = None
    index = pow(2, depth) - 1 + rIndex
    if(index >= length):
        return root
    elif(vals[index] == None):
        return root
    
    root = TreeNode(vals[index])
    root.left = buildTree(vals, length, depth+1, rIndex*2)
    root.right= buildTree(vals, length, depth+1, rIndex*2 +1)
    return root

def printTree(root: TreeNode):
    if(root == None):
        print(None)
    else:
        print(root.val)
        printTree(root.left)
        printTree(root.right)
    return

def main():
    vals = [1, 1,1, None,1,None,None, None,None,1,1,None,None,None,None, None,None,None,None,None,1]
    #vals = [1]
    root = setup(vals)
    #printTree(root)
    test = Solution
    print(test.longestZigZag(test, root))

if(__name__ == "__main__"):
    main()
        