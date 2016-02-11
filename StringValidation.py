# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/string-validators
instr = raw_input();
alphaflag = False;
digflag = False;
lowflag = False;
upflag = False;
alphanumflag = False;
splflag = False;
alphacount = 0;
digcount = 0;

# Looping through all the char's
for x in range(len(instr)):
    if instr[x].isalpha():
        alphacount = alphacount + 1;
        alphaflag  = True; 
        # if the char is alpha check for the case
        if instr[x].islower():    
            lowflag    = True; 
        else:    
            upflag     = True; 
    # if the char is a digit         
    elif instr[x].isdigit():    
        digcount   = digcount + 1;
        digflag    = True;
    # Other than alpha or digit    
    else:
        splflag    = True;

# Alphanumeric is having either alpha or dig (surprise!)        
if(digflag > 0 or alphaflag > 0):
    alphanumflag = True;
        
                
print alphanumflag;
print alphaflag;
print digflag;
print lowflag;
print upflag;
    

