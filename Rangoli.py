# Enter your code here. Read input from STDIN. Print output to STDOUT

import string;
n = int(input())
alphabet = string.ascii_lowercase
col = 4*n - 3;
rows = 2*n - 1;
pos = col/2 + 1;
Queue = ["-"*col]*col;
temp = "";
result = [" "]*rows;
k = 1;
for i in range(0,(rows/2)-1):
    temp = Queue[i];
    for j in range(0,i+1):       
        temp = temp[:pos-j-k] + alphabet[n-j-k] + temp[pos-j:];
        #print temp;
        k = k+2;
    result[i] = temp;     
    result[rows-i-1] = temp;  

for i in result:
    print i;
    
    
    