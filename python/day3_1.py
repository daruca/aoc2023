f = open("input3_tst.txt","r")
t = f.readlines()
matrix = []
for line in t:
    values = line.split(".")
    matrix.append(values)
    
print(matrix)