# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
n,m = map(int,raw_input().split());
#Used a default dictionary to save each occurrence of the element and store them of type list=
groupA = defaultdict(list)
groupB = []
for i in range(n):
    #Appending the index for each element that is read
    groupA[raw_input()].append(str(i+1))
for i in range(m):
    groupB.append(raw_input())
for i in groupB:
    if (i in groupA):
        # Join the elements with a space between them
        print ' '.join(groupA[i])
    else:
        print -1

    