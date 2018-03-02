"""
AC code of Question:
https://leetcode.com/problems/add-and-search-word-data-structure-design/description/
Using Simple Trie.
"""

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
        return self._r_search(self.root, word)

    def _r_search(self, root, word):
        # this if clause is no needed.
        print "=Start a _r_search"
        if not word:
            print "not word: root[0] is : ", bool(root[0])
            return bool(root[0])

        char = word[0]
        left_word = word[1:] if len(word) > 1 else ''
        print "Whole word is ::: ", word
        if char == '.':
            for ic in root[1:]:
                if ic:
                    search_left = self._r_search(ic, left_word)
                    print "root : to see ic: ", root
                    print "search result of ic %s, left_word %s is ::: %s ." % (ic, left_word, search_left)
                    if search_left:
                        return True
            return False
        else:
            index = ord(char) - 96
            if root[index]:
                return self._r_search(root[index], left_word)
            else:
                return False


#Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord('jay')
obj.addWord('lay')
obj.addWord('joy')
print obj.search('')
print obj.search('j')
print obj.search('ja')
print obj.search('jay')
print obj.search('jayl')
print obj.search('joy')
print obj.search('j.y')

## Your Trie object will be instantiated and called as such:
#obj = Trie()
#word = 'jay'
#prefix = 'ja'
#obj.insert(word)
#param_2 = obj.search(word)
#param_4 = obj.search(word[:2])
#assert param_2 is True
#assert param_4 is False
#print obj.startsWith('')
#print obj.startsWith('j')
#print obj.startsWith('ja')
#print obj.startsWith('jay')
