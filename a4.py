# finding a list divisor of 5

number = int(input("Enter the range of list:"));


list = range(1,number);

result = [];

for x in list:
   if(x%5 ==0):
      result.append(x);

if(len(result)>0):
   result.reverse();
   print result;
else:
   print "list is empty, No divisors in the given range";