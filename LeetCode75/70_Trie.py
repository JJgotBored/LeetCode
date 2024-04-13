class TrieNode:
    def __init__(self):
        self.children = [None for i in range(26)]
        self.endOfWord = False

class Trie:

    def __init__(self):
        #self.words = []
        return

    def insert(self, word: str) -> None:
        #self.words.append(word)
        return

    def search(self, word: str) -> bool:
        """
        for i in self.words:
            if(i == word):
                return True
        """
        return False

    def startsWith(self, prefix: str) -> bool:
        """
        n = len(prefix)
        for i in self.words:
            if(n <= len(i)):
                for j in range(n):
                    if (prefix[j] != i[j]):
                        break
                    elif(j == n-1):
                        return True
        """            
        return False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)