import re
f = open("input3_tst.txt","r")
t = f.readlines()
matrix = []
regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]') 
for line in t:
    if(regex.search(line)==None):
        print("not found")
    else:
        print("found")
