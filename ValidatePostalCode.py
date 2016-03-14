# https://www.hackerrank.com/challenges/validating-postalcode
import re
inStr = input()
try:
    oddStr  = int(inStr[1]+inStr[3]+inStr[5])
    evenStr = int(inStr[0]+inStr[2]+inStr[4])
    match = str(bool(re.search(r'.*(.)\1{1}',str(oddStr)))) + str(bool(re.search(r'.*(.)\1{1}',str(evenStr)))) + str(len(inStr))
    print (bool(re.search(r'([F].*){1}6$',match)))
except (IndexError,ValueError) as e:
    print (False)