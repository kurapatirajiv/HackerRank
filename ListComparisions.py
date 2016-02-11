# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/list-comprehensions

x = int(raw_input());
y = int(raw_input());
z = int(raw_input());
n = int(raw_input());

xi = range(x+1);
yi = [ i for i in range(y+1) ]
zi = [ j for j in range(z+1) ]

result = [];
final = [];
for a in xi:
    for b in yi:
        for c in zi:            
            if (a + b + c) is not n:
                result.extend([a,b,c]);
                final.append(result);
                result = [];
print final;
            