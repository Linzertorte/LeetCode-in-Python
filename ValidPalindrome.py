class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        s=filter((lambda c:c>='a' and c<='z' or c>='0' and c<='9'),s.lower())
        return s==s[::-1]
