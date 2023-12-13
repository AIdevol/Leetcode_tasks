
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_word = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return node.is_word
            if word[i] == '.':
                for child in node.children.values():
                    if dfs(child, i+1):
                        return True
            else:
                if word[i] in node.children and dfs(node.children[word[i]], i+1):
                    return True
            return False
        
        return dfs(self.root, 0)

 







# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)