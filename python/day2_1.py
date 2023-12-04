
import re 

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
                    num_red = num_red + int(c[0:r])                  
                        #print("red",int(c[0:r]))
                g = c.find("green")
                if(g != -1):
                    num_green = num_green + int(c[0:g])
                        #print("green",int(c[0:g]))
                b = c.find("blue")
                if(b != -1):
                    num_blue = num_blue + int(c[0:b])   
                        #print("blue",int(c[0:b]))
                    #check    
            if (num_red > max_red or
                num_blue > max_blue or
                num_green > max_green):
                    print("exceeded limits red", num_red,"green", num_green, "blue", num_blue)
                    gameok = False
                    numberGame = num_blue = num_red = num_green = 0
                    exit
            else:
                    gameok = True
                    print("red", num_red, "blue", num_blue,"green", num_green) 
                    num_blue = num_red = num_green = 0
            print("______________________________")
        if(gameok==True):
            #print("Game", int(numberGame)," correct! adding it to", total)
            total = total + int(numberGame)
            print("Game", int(numberGame)," correct! Total:", total)
        else:
            print("Game", int(numberGame)," incorrect! Total:", total)
        gameok = False
        game.append(total)
            
            #calculate 
#print("Total:",total)
