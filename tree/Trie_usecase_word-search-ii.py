"""
https://leetcode.com/problems/word-search-ii/description/

Detail:
    Most of others are using Trie & DFS(recusive).
    Not sure if there are any other approch.
    Wait to see ...
"""
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


class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        char_index = self._get_char_index(board)
        trie = Trie()
        for word in words:
            trie.search

        
    def _get_char_index(self, board):
        M = len(board)
        N = len(board[0]) if M else 0
        res = []*27
        for i in xrange(0, M):
            for j in xrange(0, N):
                char = ord(board[i][j]) - 96
                res[char].append((i, j))
        return res


