# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/validating-named-email-addresses
import re
import email.utils
for  _ in range(int(raw_input())):
    strIn = raw_input()
    emailIn = email.utils.parseaddr(strIn)[1]
    if re.match(r'^([a-zA-Z])([\w.-]*)@([a-zA-Z]+)\.([a-z]{1,3})$',emailIn):
        print strIn
 