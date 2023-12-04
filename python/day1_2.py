#Now taking into account spelled numbers
#It looks like some of the digits are actually spelled out 
#with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".
import re

f = open("input1_1.txt","r")
t = f.readlines()
total = int(10)
total = 0
for line in t:
    values = {
        "one": 1, "1": 1,
	    "two": 2, "2": 2,
	    "three": 3, "3": 3,
	    "four": 4, "4": 4,
	    "five": 5, "5": 5,
	    "six": 6, "6": 6,
	    "seven": 7, "7": 7,
	    "eight": 8, "8": 8,
	    "nine": 9, "9": 9
    }
    #line = line[::-1]
    #print(line)

   
    digits = re.findall("(?=(one|two|three|four|five|six|seven|eight|nine|[1-9]))", line)
    parsed_values = [values[num] for num in digits]
        
        #res = [int (i) for i in x if i.isdigit()]
    ret = str(parsed_values[0]) + str(parsed_values[-1])

        #print (res,"-->",ret)
        #accumulate partial results
    parc = int(ret)
    total = total + parc
    print ("partial ", total, " and added ",parc, "partial calib: ", total)
        

print ("calibration: ",total)