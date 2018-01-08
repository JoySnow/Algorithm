class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.N = 26
        self.M = self.N + 1
        self.root = [0]*self.M

    def insert(self, word):
        """
        Inserts a word into the trie.
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
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
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


    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        found = ''
        level = self.root
        for c in prefix:
            print c
            index = ord(c) - 96
            print level[index]
            if not level[index]:
                print "Search: Cut down with: ", found
                return False
            found += c
            level = level[index]
        print "Search: Till end, is pre ", found
        return True
        


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
