class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        dir = {}
        for i in range(26):
            c = chr(ord('A')+i)
            dir[c] = i+1
        res = 0
        for i in range(len(s)):
            k = len(s)-i-1
            res += (26**i)*dir[s[k]]
        return res
