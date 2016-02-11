# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/swap-case
S = raw_input();
output = '';
for x in range(len(S)):
    if (S[x].isupper()):
        output = output + S[x].lower();
    else:
        output = output + S[x].upper();

print output;