# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
S =raw_input()
pattern = raw_input()
result = []
for i in range(len(S)):
    m = re.match(pattern, S[i:])
    if m:
        result.append((i + m.start(), i + m.end()-1))
        print (i + m.start(), i + m.end()-1)
if not result:
    print (-1, -1)