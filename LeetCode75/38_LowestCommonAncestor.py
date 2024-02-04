# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if(root == None):
            return None
        pFound = None
        qFound = None
        bothFound = None

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right,p,q)
        
        if(left != None):
            if(left.val == p.val):
                pFound = left
            elif(left.val == q.val):
                qFound = left
            else:
                bothFound = left
            
        if(right != None):
            if(right.val == p.val):
                pFound = right
            elif(right.val == q.val):
                qFound = right
            else:
                bothFound = right
        
        if(root.val == p.val):
            pFound = root
        elif(root.val == q.val):
            qFound = root
        
        if(bothFound != None):
            return bothFound
        elif(pFound != None and qFound != None):
            return root
        elif(pFound != None):
            return pFound
        elif(qFound != None):
            return qFound
    
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
    #vals = [-1, 0,3, -2,4,None,None, 8]
    root = setup(vals)
    node1 = TreeNode(5)
    node2 = TreeNode(4)
    #printTree(root)
    test = Solution()
    temp = test.lowestCommonAncestor(root, node1, node2)
    if(temp != None):
        print(temp.val)
    else:
        print("NONE")
if(__name__ == "__main__"):
    main()