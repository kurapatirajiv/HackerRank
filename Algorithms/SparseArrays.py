# https://www.hackerrank.com/challenges/sparse-arrays
# Utilizes Count function 
inList1 = []
for i in range(int(input())):
    inList1.append(input())
for i in range(int(input())):
    print (inList1.count(input()))
