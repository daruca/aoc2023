f = open("input1_1.txt","r")
t = f.readlines()
total = int(10)
total = 0
for line in t:
    tmp = chr(2)
    ret = chr(2)
    res = [int (i) for i in line if i.isdigit()]
    
    tmp = res
    x = len(tmp)
    if x == 1:
        ret = str(tmp[0]) + str(tmp[0])
    elif x == 2:
        ret = str(tmp[0]) + str(tmp[1])
    else:
        ret = str(tmp[0]) + str(tmp[x-1])
    

   # print (res,"-->",ret)
    #accumulate partial results
    parc = int(ret)
    #print ("partial ", ret, " and added ",parc, "partial calib: ", total)
    total = total + parc
    
print ("calibration: ",total)