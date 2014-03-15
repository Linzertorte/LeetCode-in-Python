class Solution:
    # @return a string
    def digit(self,d,X,V,I):
        if d == 9:
            return I+X
        elif d>=5:
            return V+I*(d-5)
        elif d==4:
            return I+V
        elif d>0:
            return I*d
        else:
            return ''
    def intToRoman(self, num):
        return 'M'*(num/1000)+self.digit((num/100)%10,'M','D','C')\
        +self.digit((num/10)%10,'C','L','X')\
        +self.digit(num%10,'X','V','I')
