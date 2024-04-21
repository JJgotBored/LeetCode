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
        tempChild = None
        for i in (word):
            tempChild = temp.children[ord(i) -97]
            if(tempChild == None):
                tempChild = TrieNode()
            temp = tempChild
        
        temp.endOfWord = True

        return

class Solution:
    def suggestedProducts(self, products: list[str], searchWord: str) -> list[list[str]]:
        return None
    
def main():
    test = Solution()
    products = []
    search = ""

if(__name__ == "__main__"):
    main()