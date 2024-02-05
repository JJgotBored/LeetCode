# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        if(root == None):
            return 0
        level = 1
        currLevel = 1
        maxSum = root.val
        currSum = 0
        currLayer = [root]
        nextLayer = []

        while(len(currLayer) > 0 or len(nextLayer) > 0):
            #print(len(currLayer), len(nextLayer))
            
            if(len(currLayer) > 0):
                if(currLayer[0].left != None):
                    nextLayer.append(currLayer[0].left)
                if(currLayer[0].right != None):
                    nextLayer.append(currLayer[0].right)
                currSum += currLayer[0].val
                currLayer.pop(0)

            if(len(currLayer) == 0):
                if(maxSum < currSum):
                    maxSum = currSum
                    level = currLevel
                currLayer = nextLayer[:]
                nextLayer = []
                currLevel += 1
                currSum = 0

        return level

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
    #vals = [1,7,0,7,-8,None,None]
    #vals = [1,2,3]
    vals = [-100,-200,-300,-20,-5,-10,None]
    root = buildTree(vals)
    #printTree(root)
    test = Solution()
    print(test.maxLevelSum(root))

if(__name__ == "__main__"):
    main()
        