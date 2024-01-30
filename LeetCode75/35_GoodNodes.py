# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
    
        if(root == None):
            return 0
        
        currMax = root.val

        return self.rSearch(self, root, currMax)

    def rSearch(self, root: TreeNode, currMax: int) -> int:
        count = 0
        if(root == None):
            return 0
        
        if(root.val >= currMax):
            count += 1
            currMax = root.val
        
        count += self.rSearch(self, root.left, currMax)
        count += self.rSearch(self, root.right, currMax)

        return count

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
    vals = [1,2,3]
    root = setup(vals)
    test = Solution
    print(test.goodNodes(test, root))
    printTree(root)

if(__name__ == "__main__"):
    main()