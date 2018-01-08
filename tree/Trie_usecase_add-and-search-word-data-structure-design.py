class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.N = 26
        self.M = self.N + 1
        self.root = [0]*self.M

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        level = self.root
        for c in word:
            print c
            index = ord(c) - 96
            print level[index]
            if not level[index]:
                #add Node
                level[index] = [0]*self.M
            level = level[index]
            print self.root
            print level
        level[0] = 1
        print self.root
        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        if not word == '.':

                # make a queue
            else:
                #normal

    def _r_search(self, root, word):
        found = ''
        level = self.root
        for c in word:
            print c
            index = ord(c) - 96
            print level[index]
            if not level[index]:
                print "Search: Cut down with: ", found
                return False
            found += c
            level = level[index]
        if not level[0]:
            print "Search: Till end, but not stored: ", found
            return False
        else:
            return True




# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

# Your Trie object will be instantiated and called as such:
obj = Trie()
word = 'jay'
prefix = 'ja'
obj.insert(word)
param_2 = obj.search(word)
param_4 = obj.search(word[:2])
assert param_2 is True
assert param_4 is False
print obj.startsWith('')
print obj.startsWith('j')
print obj.startsWith('ja')
print obj.startsWith('jay')
