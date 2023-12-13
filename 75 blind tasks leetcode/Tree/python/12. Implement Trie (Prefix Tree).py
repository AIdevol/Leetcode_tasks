class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = [None] * 26

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            index = ord(c) - ord('a')
            if not node.children[index]:
                node.children[index] = TrieNode()
            node = node.children[index]
        node.is_word = True
        
    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            index = ord(c) - ord('a')
            if not node.children[index]:
                return False
            node = node.children[index]
        return node.is_word
    
    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            index = ord(c) - ord('a')
            if not node.children[index]:
                return False
            node = node.children[index]
        return True