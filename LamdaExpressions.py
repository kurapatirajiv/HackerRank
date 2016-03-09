# https://www.hackerrank.com/challenges/map-and-lambda-expression
series = []
# Return the number if is less than 2, otherwise recurse the function
fib = lambda n: n if n < 2 else fib(n-1) + fib(n-2)
# Another way : fib = lambda n:reduce(lambda x,n:[x[1],x[0]+x[1]], range(n),[0,1])[0] : we have to import functools import reduce 
# Lambda to generate cube of individual items, replaced map function instead of using for loop   
print (map(lambda x: x**3, map(fib, range(input()))))
#print (map(lambda x: x**3, map(fib,range(int(input())))))