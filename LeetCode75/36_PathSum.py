# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        if(root == None):
            return 0
        return self.rSearch(self, root, targetSum, 0, True)
    
    def rSearch(self, root: TreeNode, targetSum: int, currSum: int, split : True) -> int:
        if(root == None):
            return 0
        count = 0

        if((currSum + root.val) == targetSum):
            count += 1
            print(currSum, root.val)
        
        count += self.rSearch(self, root.left, targetSum, currSum +root.val, split)
        count += self.rSearch(self, root.right, targetSum, currSum + root.val, split)

        if(split == True):
            count += self.rSearch(self, root.right, targetSum, 0, False)
            count += self.rSearch(self, root.left, targetSum, 0, False)
        return count


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
    vals = [1,None,2,None,None,None,3,None,None,None,None,None,None,None,4,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,5]
    root = setup(vals)
    test = Solution
    print(test.pathSum(test, root, 3))
    #printTree(root)

if(__name__ == "__main__"):
    main()        