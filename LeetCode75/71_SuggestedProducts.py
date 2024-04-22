class TrieNode:
    def __init__(self):
        self.children = [None for i in range(26)]
        self.endOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        return
    
    def insert(self, word: str) -> None:
        temp = self.root
        j = 0
        for i in (word):
            j = ord(i) -97
            if(temp.children[j] == None):
                temp.children[j] = TrieNode()
            temp = temp.children[j]
        
        temp.endOfWord = True

        return

class Solution:
    def suggestedProducts(self, products: list[str], searchWord: str) -> list[list[str]]:
        return None

#******************************************
#           Testing Below
#******************************************
def printTrie(root: Trie):
    printTrieNode(root.root, "")
    return

def printTrieNode(root: TrieNode, curr: str):
    print(curr, " \t\t ", root.endOfWord)
    for i in range(26):
        if root.children[i] != None:
            printTrieNode(root.children[i], curr + chr(i +97))
    return

def main():
    print("main")
    test = Solution()
    root = Trie()
    root.insert("word")
    root.insert("worst")
    root.insert("wanted")
    printTrie(root)
    products = []
    search = ""

if(__name__ == "__main__"):
    main()