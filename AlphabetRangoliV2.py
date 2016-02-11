# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/alphabet-rangoli

import string;
n = int(input())
# Generate list of Alphabets
alphabet = string.ascii_lowercase
col = 4*n - 3;
rows = 2*n - 1;
mid = col/2 + 1;
Queue = ["-"*col]*rows;
temp = "";

#Repeat for the number of rows divided by 2
for i in range(0,(rows/2)+1):
    temp = Queue[i];
    #Generate the middle element      
    temp = temp[:mid-1] + alphabet[n-i-1] + temp[mid:];
    lpos = col/2 + 1;
    rpos = col/2 - 1;  
    #Identify the index of the middle element to generate the previous elements
    index = alphabet.index(temp[len(temp)/2]);
    #Generate the left and tree tree elements
    for l in range(0,i):
        if((rpos > 0) and (lpos > 0)):
            temp  = temp[:lpos-3] + alphabet[index+1] + temp[lpos-2:];
            temp  = temp[:rpos+3] + alphabet[index+1] + temp[rpos+4:];
            index = index + 1;
            rpos  = rpos + 2;
            lpos  = lpos - 2;
# 1 and last elements are the same, so generate 1 to mid and copy the same to mid+1 to N    
    Queue[i] = temp;     
    Queue[rows-i-1] = temp;  
    
#Printing the Elements in the Tree
for i in Queue:
    print i;
    
    
    