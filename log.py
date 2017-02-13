from os.path import expanduser
from datetime import date

#Figure out how many days are remaining from today until
#the end of March - thats the current target - change as needed.
stringDate = date(2017, 3, 31) - date.today()
dateList = str(stringDate).split()
daysRemaining = float(dateList[0])

#initialise float for the total count
totalCount = 0.0

#initialise float for the target distance
targetDistance = 600.0


#Get the delimiter to identify user
whoAmI = raw_input("What is your code ? dermot=dlog: aidan=alog: Enter here:  ")

## Open the file with read only permit
home = expanduser("~")
f = open(home+"/Desktop/chat.txt")
## Read the first line 
line = f.readline()

## If the file is not empty keep reading line one at a time
## utill the file is empty
while line:
	line = f.readline()
	lineList = line.split()
		
	for number in lineList:
  		wordAsString = str(number)

 		if wordAsString.startswith(whoAmI):
  			insideString = wordAsString.lstrip(whoAmI)
  			totalCount = float(insideString) + totalCount
   
f.close()

remaingAveragePerDay = (targetDistance - totalCount) / daysRemaining

print "So far you have done: %f" % totalCount
print "There are %f days remaining until the end of March" % daysRemaining
print "That means you need to average %f per day until the end of March to make it to 600" % remaingAveragePerDay