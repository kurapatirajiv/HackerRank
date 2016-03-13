# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/validate-a-roman-number
# Ref : http://stackoverflow.com/questions/267399/how-do-you-match-only-valid-roman-numerals-with-a-regular-expression
# M is ranged till 3 digits to accept till 3000 only on 4 it will accept 4000 but the code requirement does not wish to validate
import re
print True if (re.search(r'^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$',raw_input())) else False    