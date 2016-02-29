# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/maximize-it
from itertools import product
k,m = raw_input().split()
primaryList = []
modList = []
for _ in range(int(k)):    
    primaryList.append(list(map(int,raw_input().split()[1:])))    
#This will feed all the pairs as separate arguments to product, which will then give you the cartesian product of them.    
for x in list(product(*primaryList)):   
    aggr = 0
    for y in range(len(x)):
        aggr = aggr + x[y]*x[y]
    modList.append(aggr % int(m))
print max(modList)    
