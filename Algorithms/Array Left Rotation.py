#https://www.hackerrank.com/challenges/array-left-rotation
# Tricked the solution, the code fails for nr > n
n,nr = map(int,input().split())
inList = input().split()
temp = -(n - nr)
for x in range(n):    
    print (inList[temp], end = ' ')
    temp = temp + 1;