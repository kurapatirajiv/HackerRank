# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/re-sub-regex-substitution
import re
logAnd = '&&'
logOR  = '\|\|'
for _ in range(int(raw_input())):
    strIn  = raw_input()
    modStr = re.sub(r'(?<= )('+logAnd+')(?= )',"and",strIn)
    print re.sub(r'(?<= )('+logOR+')(?= )',"or",modStr)