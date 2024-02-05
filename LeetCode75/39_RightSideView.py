# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> list[int]:
        if(root == None):
            return []
        lst = [root.val] + self.rightSideView(root.right)

        return lst
    

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
    #vals = [1,2,3,None,5,None,4]
    #vals = [1,None,3 ]
    vals = []
    root = buildTree(vals)
    #printTree(root)
    test = Solution()
    print(test.rightSideView(root))

if(__name__ == "__main__"):
    main()