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
        
        return self.rSearch(root, -1, 0)
    
    def rSearch(self, root: TreeNode, dir: int, currLen: int) -> int:
        if(root == None):
            return currLen -1
        maxLen = 0
        if(dir == 0):
            maxLen = max(self.rSearch(root.left,0,1),self.rSearch(root.right,1, currLen+1))
        elif(dir == 1):
            maxLen = max(self.rSearch(root.left,0,currLen+1),self.rSearch(root.right,1,1))
        else:
            maxLen = max(self.rSearch(root.left,0,1), self.rSearch(root.right,1,1))
        
        #print(maxLen)
        return maxLen
   
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
    #vals = [1, None, 1]
    vals = [1, 1,1, None,1,None,None, None,None,1,1,None,None,None,None, None,None,None,None,None,1]
    #vals = [1]
    #vals = [1,1,1,None,1,None,None]
    #vals = [1, None,1, None,None,1,1, None,None,None,None,None,None,1,1, None,None,None,None,None,None,None,None,None,None,None,None,None,1,None,None,
    #         None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,1,None,None,None,None]
    root = setup(vals)
    #printTree(root)
    test = Solution()
    print(test.longestZigZag(root))

if(__name__ == "__main__"):
    main()
        