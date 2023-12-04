#Now taking into account spelled numbers
#It looks like some of the digits are actually spelled out 
#with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".
import re

f = open("input1_1.txt","r")
t = f.readlines()
total = int(10)
total = 0
for line in t:
    tmp = chr(2)
    ret = chr(2)
    text = []
    x = ""
    #Add the logic to parse number as text
    #textNumbers = ["one", "two", "three", "four", "five", "six", "seven", "eight","nine"]
    #line = line.strip()

    #line = line[::-1]
    print(line)
    for l in line:
        #print(l)
        x += l
        
        #print(x)
        x = x.replace("one","1")
        x = x.replace("two","2")
        x = x.replace("three","3")
        x = x.replace("four","4")
        x = x.replace("five","5")
        x = x.replace("six","6")
        x = x.replace("seven","7")
        x = x.replace("eight","8")
        x = x.replace("nine","9")  
    
    #x = line.replace("one","1")
    #x = x.replace("two","2")
    #x = x.replace("three","3")
    #x = x.replace("four","4")
    #x = x.replace("five","5")
    #x = x.replace("six","6")
    #x = x.replace("seven","7")
    #x = x.replace("eight","8")
    #x = x.replace("nine","9")        
    #print("origin",line, "dest",x)
    #for i in textNumbers:
        #print ("line: ", line, " against ",i)
    #    if i in line:
    #     text.append(i)
         
         #print("found!!")
    #print ("line: ", line, "text: ",str(text))
    res = [int (i) for i in x if i.isdigit()]
    
    tmp = res
    x = len(tmp)
    if x == 1:
        ret = str(tmp[0]) + str(tmp[0])
    elif x == 2:
        ret = str(tmp[0]) + str(tmp[1])
    else:
        ret = str(tmp[0]) + str(tmp[x-1])
    

    #print (res,"-->",ret)
    #accumulate partial results
    parc = int(ret)
    #print ("partial ", total, " and added ",parc, "partial calib: ", total)
    total = total + parc
    #print("parc",parc,"total",total)
print ("calibration: ",total)