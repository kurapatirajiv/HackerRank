
# Clean the data before sending it to Kinesis Stream

import re

Data_raw = open('/Users/Rajiv/Desktop/Capstone Project/RealNewsInputVerOne.txt','r')
Data_clean = open('/Users/Rajiv/Desktop/Capstone Project/RealNewsInputVerOneClean.txt','w')
regex = re.compile("^[w]{3}")

invalidRec = 0

for data in Data_raw:
	inDate = data.split(",")[0]
	email = data.split(",")[1]
	if regex.match(email):
		if(len(inDate)==10):
			Data_clean.write(data.rstrip()+"\n")		
                else:
			invalidRec = invalidRec + 1		
	else:
		invalidRec = invalidRec + 1

print("Number of invalid records dropped:",invalidRec)

