# Note : To Capitalize each word preserving the spaces between the words.
# Python 3
instr = input();
for x in instr[:].split():
    # Since we are replacing the actual value we are preserving the spaces.
    instr = instr.replace(x, x.capitalize());
print(instr);