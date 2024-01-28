# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def leafSimilar(self, root1:TreeNode, root2: TreeNode) -> bool:
        lst1 = []
        lst2 = []
        self.getLeaves(self, root1, lst1)
        self.getLeaves(self, root2, lst2)
        print(lst1)
        print(lst2)
        if(lst1 == lst2):
            return True
        return False

    def getLeaves(self, root: TreeNode, lst: list):
        if(root == None):
            return
        elif(root.left == None and root.right == None):
            lst.append(root.val)
            return
        self.getLeaves(self, root.left, lst)
        self.getLeaves(self, root.right, lst)
        
        return

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
    vals1 = [1,2,3]
    vals2 = [1,3,2]
    root1 = setup(vals1)
    root2 = setup(vals2)
    #printTree(root2)
    test = Solution
    print(test.leafSimilar(test, root1, root2))

if(__name__ == "__main__"):
    main()
        