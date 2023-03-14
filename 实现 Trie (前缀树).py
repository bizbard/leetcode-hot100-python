import collections
from typing import List, Optional


class Trie:
    def __init__(self):
        self.childern = [None] * 26
        self.isEnd = False

    def searchPrefix(self, prefix: str) -> "Trie":
        node = self
        for char in prefix:
            ch = ord(char) - ord('a')
            if not node.childern[ch]:
                return None
            else:
                node = node.childern[ch]

        return node

    def insert(self, word: str) -> None:
        node = self
        for char in word:
            ch = ord(char) - ord('a')
            if not node.childern[ch]:
                node.childern[ch] = Trie()
            node = node.childern[ch]

        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self.searchPrefix(word)

        return node is not None and node.isEnd

    def startsWith(self, prefix: str) -> bool:
        
        return self.searchPrefix(prefix) is not None
        

if __name__ == "__main__":
    # ======= Test Case =======
    trie = Trie()
    trie.insert("apple")
    trie.search("apple")
    trie.search("app")
    trie.startsWith("app")
    trie.search("app")
    # ====== Driver Code ======