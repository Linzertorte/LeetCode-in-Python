class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x<0:
            return False
        def palindrome(x,i,j):
            if j-i<=0:
                return True
            return (x/10**i)%10 == (x/10**j)%10 and palindrome(x,i+1,j-1)
        
        y = x
        n = 0
        if y == 0:
            n = 1
        while y!=0:
            n+=1
            y/=10
        return palindrome(x,0,n-1)
