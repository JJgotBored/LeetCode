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
        return self.rSearch(self, root, targetSum, 0)
    
    def rSearch(self, root: TreeNode, targetSum: int, currSum: int) -> int:
        if(root == None):
            return 0
        count = 0

        if(currSum + root.val == targetSum):
            count += 1
        elif(root.val == targetSum):
            count += 1

        count += self.rSearch(self, root.left, targetSum, currSum +root.val)
        count += self.rSearch(self, root.left, targetSum, root.val)
        count += self.rSearch(self, root.right, targetSum, currSum + root.val)
        count += self.rSearch(self, root.right, targetSum, root.val)

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
    vals = [1,2,5]
    root = setup(vals)
    test = Solution
    print(test.pathSum(test, root, 5))
    #printTree(root)

if(__name__ == "__main__"):
    main()        