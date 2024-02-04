# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.rSearch(root,p.val, q.val)
        
        return None
    
    def rSearch(self, root: TreeNode, p, q) -> TreeNode:
        if(root == None):
            return None
        print(root.val)
        left = self.rSearch(root.left, p, q)

        right = self.rSearch(root.right,p,q)

        if(root.val == p):
            return root
        elif(root.val == q):
            return root
        return None

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
    vals = [3,5,1,6,2,0,8,None,None,7,4]
    root = setup(vals)
    node1 = TreeNode(5)
    node2 = TreeNode(1)
    #printTree(root)
    test = Solution()
    print(test.lowestCommonAncestor(root, node1, node2))
if(__name__ == "__main__"):
    main()