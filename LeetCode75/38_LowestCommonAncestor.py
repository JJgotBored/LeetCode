# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pFound = False
        qFound = False

        if(root == None):
            return None
        elif(root.val == p.val):
            pFound = True
        elif(root.val == q.val):
            qFound = True
        print(root.val)
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if(left != None):
            if(left.val == p.val):
                pFound = True
            elif(left.val == q.val):
                qFound = True
            else:
                return left

        if(right != None):
            if(right.val == p.val):
                pFound = True
            elif(right.val == q.val):
                qFound = True
            else:
                return right

        print(pFound, qFound)

        if(pFound == True and qFound == True):
            return root
        elif(left != None):
            return left
        elif(right != None):
            return right
        
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