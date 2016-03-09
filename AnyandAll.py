# Enter your code here. Read input from STDIN. Print output to STDOUT
myListCount,myList = int(raw_input()),map(int, raw_input().split())
print (all(element>0 for element in myList) and any(str(item) == str(item)[::-1] for item in myList))