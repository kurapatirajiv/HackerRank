# Programming on lists

number = input("Enter the number: ");

list  = [ 1,1,23,43,12,4,5,6,7];

result = [];

for x in list:
  if ( x < number) : 
      result.append(x);

print result;