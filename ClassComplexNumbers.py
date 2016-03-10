# https://www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers
from math import sqrt

class ComplexNumber:
    # Constructor 
    def __init__(self,rpart=0,ipart=0):
        self.real = rpart
        self.img  = ipart         
    def __add__(self,arg2):
        ans = ComplexNumber()
        ans.real = self.real + arg2.real
        ans.img  = self.img  + arg2.img 
        return ans
    def __sub__(self,arg2):
        ans = ComplexNumber()
        ans.real = self.real - arg2.real
        ans.img  = self.img  - arg2.img
        return ans
    def __mul__(self,arg2):
        ans = ComplexNumber()
        ans.real = self.real * arg2.real - self.img * arg2.img
        ans.img  = self.real * arg2.img  + self.img * arg2.real
        return ans
    #truediv for Python3, else use div and for // use floordiv
    def __truediv__(self,arg2):
        ans=ComplexNumber()
        ans.real=(self.real*arg2.real+self.img*arg2.img)/(arg2.real**2+arg2.img**2)
        ans.img=(self.img*arg2.real-self.real*arg2.img)/(arg2.real**2+arg2.img**2)
        return ans
    # Print function calls repr or str function for formatting, so we are overidding repr function more official manner  ;)
    def __repr__(self):
        if self.img < 0:
            return str("%.2f" %float(self.real))+ "-" + str("%.2f" %abs(float(self.img))) + "i"
        elif self.img ==0:
            return str("%.2f" %float(self.real))+ "+" + str("%.2f" %float(self.img))+ "i"
        elif self.real ==0:
            return str("%.2f" %float(self.real))+ "+" + str("%.2f" %float(self.img)) + "i"
        elif self.img > 0:
            return str("%.2f" %float(self.real))+ "+" + str("%.2f" %float(self.img)) + "i"
    # Calling operand.methodname()    
    def ModVal(self):
        ans = ComplexNumber()
        # On square rooting the value is assigned to real part of the number the img part would be zeros
        ans.real = "%.2f" % sqrt(self.real**2+self.img**2)
        return ans         
    
a,b = map(float,input().split())
c,d = map(float,input().split())
no1 = ComplexNumber(a,b)
no2 = ComplexNumber(c,d)
print (no1+no2)
print (no1-no2)
print (no1*no2)
print (no1/no2)
print (no1.ModVal())
print (no2.ModVal())
        
    