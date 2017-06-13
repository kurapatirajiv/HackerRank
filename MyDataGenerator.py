## My Fake News Data Generator using a list of news headlines and trusted Websites

import random
import sys

if(len(sys.argv) < 2 ):
    print("Usage: MyDataGenerator.py <numofRecords : Positive value>")
    sys.exit(0)

numRecords = int(sys.argv[1])

newsDataFile = open('/Users/Rajiv/Desktop/Capstone Project/News.txt','r')
RealsitesDataFile = open('/Users/Rajiv/Desktop/Capstone Project/Real News Sites.txt','r')
FakesitesDataFile = open('/Users/Rajiv/Desktop/Capstone Project/Fake news Sites.txt','r')

sitesData = []
newsData = []

fakesNewsOutput = open('/Users/Rajiv/Desktop/Capstone Project/MyRawNewsInput.txt','w')

inputDates = ["2017-05-01","2017-05-08","2017-05-09","2017-05-14","2017-05-12","2017-05-12","2017-05-12","2017-05-09","2017-05-11","2017-05-11","21090-12-1212","9999-999-999"]

for data in RealsitesDataFile:
	sitesData.append(data)

for data in FakesitesDataFile:
	sitesData.append(data)

for data in newsDataFile:
	newsData.append(data)

for x in range(0,numRecords):
	fakesNewsOutput.write(random.choice(inputDates)+","+random.choice(sitesData).rstrip("\n")+","+str(random.choice(newsData)))

