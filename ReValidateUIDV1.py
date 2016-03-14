# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/validating-uid
import re
flag = "Invalid"

for _ in range(int(raw_input())):
    strIn = raw_input()
    if ((re.search(r'(?=[A-Za-z0-9])(([A-Z].*){2})',strIn)) and (len(strIn)==10)):
        if (re.search(r'([0-9].*){3}',strIn)):
            for i in range(len(strIn)):
                if strIn[i] in strIn[i+1:]:
                    flag = "Invalid"
                    break
                else: 
                    flag = "Valid"               
    print flag
    flag = "Invalid"

                
                
        
                    