# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/polar-coordinates
import cmath;
number = raw_input();
print abs(complex(number));
print cmath.phase(complex(number));

