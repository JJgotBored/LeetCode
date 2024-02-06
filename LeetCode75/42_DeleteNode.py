# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if(root == None):
            return None
        elif(root.val == key):
            root = self.reorderTree(root)
        elif(key < root.val ):
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root
    
    def reorderTree(self, root: TreeNode) -> TreeNode:
        if(root == None):
            return None
        elif(root.left == None and root.right == None):
            return None
        elif(root.left == None):
            return root.right
        elif(root.right == None):
            return root.left
        else:
            temp = self.findSmallestNode(root.right)
            node = TreeNode(temp.val)
            node.left = root.left
            node.right = self.deleteNode(root.right, temp.val)
            root = node
        return root
    
    def findSmallestNode(self, root: TreeNode) -> TreeNode:
        if(root == None):
            return None
        elif(root.left == None):
            return root
        return self.findSmallestNode(root.left)

######### Testing Functions ########
def buildTree(vals: list) -> TreeNode:
    if(vals == []):
        return None
    root = TreeNode(vals[0])
    ptrList = [root]
    ptrIndex = 0
    
    for i in range(1, len(vals)):
        #print(vals[i])
        if(i % 2 == 1):
            if(vals[i] == None):
                ptrList[ptrIndex].left = None
            else:
                ptrList[ptrIndex].left = TreeNode(vals[i])
                ptrList.append(ptrList[ptrIndex].left)
        else:
            if(vals[i] == None):
                ptrList[ptrIndex].right = None
            else:
                ptrList[ptrIndex].right = TreeNode(vals[i])
                ptrList.append(ptrList[ptrIndex].right)
            ptrIndex +=1
    
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
    vals = [5,3,6,2,4,None,7]
    key = 3
    root = buildTree(vals)
    #printTree(root)

    test = Solution()
    out = test.deleteNode(root, key)
    printTree(out)

if(__name__ == "__main__"):
    main()