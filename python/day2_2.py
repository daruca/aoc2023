f = open("input2_1.txt","r")
t = f.readlines()

#Game 1: 10 green, 5 blue; 1 red, 9 green, 10 blue; 5 blue, 6 green, 2 red; 7 green, 9 blue, 1 red; 2 red, 10 blue, 10 green; 7 blue, 1 red
# game XX : set1 ; set2
# set XX : #r,#g,#b in any order
games = []
game = []
num_red = 0
num_green = 0
num_blue = 0
max_red = 12
max_green = 13
max_blue = 14
count = 0
total = 0
numgame = 0
gameok = False
print("Conditions")
print("Max Red:", max_red,  "Max Green", max_green, "Max Blue", max_blue)
for line in t:
    lt = line.split(":")
    #print(lt)
    game.append(lt[0])
    numberGame = lt[0].split(" ")[1]
    #print("Game:",numberGame)
    lt.pop(0)
    
    for l in lt: 
        #print("game",numberGame,"content",l)
        max_red = 0
        max_blue = 0
        max_green = 0
        mt = l.split(";")
        num_blue = num_red = num_green = 0
        gameok = False
        for m in mt:
            #print(m)
            num_blue = num_red = num_green = 0
            ct = m.split(",")
            for c in ct:
                    #print ("C:",c)
                r = c.find("red")
                if(r != -1):
                    curr_red = int(c[0:r])
                    #num_red = num_red + int(c[0:r])
                    if (curr_red > max_red):
                        max_red = curr_red
                g = c.find("green")
                if(g != -1):
                    curr_green = int(c[0:g])
                    #num_green = num_green + int(c[0:g])
                    if (curr_green > max_green):
                        max_green = curr_green
                b = c.find("blue")
                if(b != -1):
                    curr_blue =  int(c[0:b])
                    if (curr_blue > max_blue):
                        max_blue = curr_blue
                        #print("blue",int(c[0:b]))
                    #check    
            curr_row = max_blue * max_green * max_red
            #print("______________________________")
            #print("Game", int(numberGame)," correct! adding it to", total)
        total = total + curr_row
        game.append(total)
            
            #calculate 
print("Total:",total)
