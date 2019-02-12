from tkinter import *
root = Tk()


#map as a list of lists
testMap=[
["neutral","fastcone","neutral","neutral","neutral","neutral","neutral","neutral","neutral","neutral"],
["neutral","neutral","neutral","neutral","neutral","neutral","neutral","neutral","neutral","neutral"],
["neutral","neutral","neutral","neutral","neutral","neutral","neutral","neutral","neutral","neutral"],
["neutral","neutral","neutral","neutral","neutral","neutral","neutral","neutral","neutral","neutral"],
["neutral","neutral","neutral","neutral","neutral","neutral","neutral","neutral","neutral","neutral"],
["neutral","neutral","neutral","neutral","neutral","neutral","neutral","neutral","neutral","neutral"],
["neutral","neutral","neutral","neutral","neutral","neutral","neutral","neutral","neutral","neutral"],
["neutral","neutral","neutral","neutral","neutral","neutral","neutral","neutral","neutral","neutral"],
["neutral","neutral","neutral","neutral","neutral","neutral","neutral","neutral","neutral","neutral"],
["neutral","neutral","neutral","neutral","neutral","neutral","neutral","neutral","neutral","neutral"],
["neutral","neutral","neutral","neutral","neutral","neutral","neutral","neutral","neutral","neutral"],
["neutral","neutral","neutral","neutral","neutral","neutral","neutral","neutral","neutral","neutral"],
["neutral","neutral","neutral","neutral","neutral","neutral","neutral","neutral","neutral","neutral"],
["neutral","neutral","neutral","neutral","neutral","neutral","neutral","neutral","neutral","neutral"],
["neutral","neutral","neutral","neutral","neutral","neutral","neutral","neutral","neutral","neutral"],
["neutral","neutral","neutral","neutral","neutral","neutral","neutral","neutral","neutral","neutral"],
["neutral","neutral","neutral","neutral","neutral","neutral","neutral","neutral","neutral","neutral"],
["neutral","neutral","neutral","neutral","neutral","neutral","neutral","neutral","neutral","neutral"],
["neutral","neutral","neutral","neutral","neutral","neutral","neutral","neutral","neutral","neutral"],
["neutral","neutral","neutral","neutral","neutral","neutral","neutral","neutral","neutral","neutral"]]


#victorytokens, list of 2xposition
#v0 = []

#energycubes, list of 2xposition
#e0 = []


#for loading in of later, custom maps
board=testMap


#robots, list of
#2xposition, direction, victorytokens, energy, register, deck, discard, hand
r1 = [1,0,"e",0,5,["","","","",""],["1for","1for","1for","1for","1for","2for","2for","2for","3for","1back","left","left","left","right","right","right","uturn","again","again","powerup"], [], []]

r2 = [2,0,"e",0,5,["","","","",""],["1for","1for","1for","1for","1for","2for","2for","2for","3for","1back","left","left","left","right","right","right","uturn","again","again","powerup"], [], []]

r3 = [3,0,"e",0,5,["","","","",""],["1for","1for","1for","1for","1for","2for","2for","2for","3for","1back","left","left","left","right","right","right","uturn","again","again","powerup"], [], []]

r4 = [4,0,"e",0,5,["","","","",""],["1for","1for","1for","1for","1for","2for","2for","2for","3for","1back","left","left","left","right","right","right","uturn","again","again","powerup"], [], []]

r5 = [5,0,"e",0,5,["","","","",""],["1for","1for","1for","1for","1for","2for","2for","2for","3for","1back","left","left","left","right","right","right","uturn","again","again","powerup"], [], []]

r6 = [6,0,"e",0,5,["","","","",""],["1for","1for","1for","1for","1for","2for","2for","2for","3for","1back","left","left","left","right","right","right","uturn","again","again","powerup"], [], []]

r7 = [7,0,"e",0,5,["","","","",""],["1for","1for","1for","1for","1for","2for","2for","2for","3for","1back","left","left","left","right","right","right","uturn","again","again","powerup"], [], []]

r8 = [8,0,"e",0,5,["","","","",""],["1for","1for","1for","1for","1for","2for","2for","2for","3for","1back","left","left","left","right","right","right","uturn","again","again","powerup"], [], []]








#variables for images
neutral = PhotoImage(file="graphics/neutral.gif")
r1n =     PhotoImage(file="graphics/r1n.gif")
r1e =     PhotoImage(file="graphics/r1e.gif")
r1s =     PhotoImage(file="graphics/r1s.gif")
r1w =     PhotoImage(file="graphics/r1w.gif")

r2n =     PhotoImage(file="graphics/r2n.gif")
r2e =     PhotoImage(file="graphics/r2e.gif")
r2s =     PhotoImage(file="graphics/r2s.gif")
r2w =     PhotoImage(file="graphics/r2w.gif")

r3n =     PhotoImage(file="graphics/r3n.gif")
r3e =     PhotoImage(file="graphics/r3e.gif")
r3s =     PhotoImage(file="graphics/r3s.gif")
r3w =     PhotoImage(file="graphics/r3w.gif")

r4n =     PhotoImage(file="graphics/r4n.gif")
r4e =     PhotoImage(file="graphics/r4e.gif")
r4s =     PhotoImage(file="graphics/r4s.gif")
r4w =     PhotoImage(file="graphics/r4w.gif")

r5n =     PhotoImage(file="graphics/r5n.gif")
r5e =     PhotoImage(file="graphics/r5e.gif")
r5s =     PhotoImage(file="graphics/r5s.gif")
r5w =     PhotoImage(file="graphics/r5w.gif")

r6n =     PhotoImage(file="graphics/r6n.gif")
r6e =     PhotoImage(file="graphics/r6e.gif")
r6s =     PhotoImage(file="graphics/r6s.gif")
r6w =     PhotoImage(file="graphics/r6w.gif")

r7n =     PhotoImage(file="graphics/r7n.gif")
r7e =     PhotoImage(file="graphics/r7e.gif")
r7s =     PhotoImage(file="graphics/r7s.gif")
r7w =     PhotoImage(file="graphics/r7w.gif")

r8n =     PhotoImage(file="graphics/r8n.gif")
r8e =     PhotoImage(file="graphics/r8e.gif")
r8s =     PhotoImage(file="graphics/r8s.gif")
r8w =     PhotoImage(file="graphics/r8w.gif")

fastconn= PhotoImage(file="graphics/fastconn.gif")
fastcone= PhotoImage(file="graphics/fastcone.gif")
fastcons= PhotoImage(file="graphics/fastcons.gif")
fastconw= PhotoImage(file="graphics/fastconw.gif")












def square(type):
    if type == "neutral":
        return neutral
    if type == "start":
        return start
    if type == "radar":
        return radar
    if type == "fastcone":
        return fastcone


def r1cursor(d):
    if d == "n":
        return r1n
    if d == "e":
        return r1e
    if d == "s":
        return r1s
    if d == "w":
        return r1w

def r2cursor(d):
    if d == "n":
        return r2n
    if d == "e":
        return r2e
    if d == "s":
        return r2s
    if d == "w":
        return r2w

def r3cursor(d):
    if d == "n":
        return r3n
    if d == "e":
        return r3e
    if d == "s":
        return r3s
    if d == "w":
        return r3w

def r4cursor(d):
    if d == "n":
        return r4n
    if d == "e":
        return r4e
    if d == "s":
        return r4s
    if d == "w":
        return r4w

def r5cursor(d):
    if d == "n":
        return r5n
    if d == "e":
        return r5e
    if d == "s":
        return r5s
    if d == "w":
        return r5w

def r6cursor(d):
    if d == "n":
        return r6n
    if d == "e":
        return r6e
    if d == "s":
        return r6s
    if d == "w":
        return r6w

def r7cursor(d):
    if d == "n":
        return r7n
    if d == "e":
        return r7e
    if d == "s":
        return r7s
    if d == "w":
        return r7w

def r8cursor(d):
    if d == "n":
        return r8n
    if d == "e":
        return r8e
    if d == "s":
        return r8s
    if d == "w":
        return r8w



#draw empty board
def drawBoard():
    x=0
    while x < len(board):
        y=0
        while y < len(board[x]):
            Label(root, height="30", width="30", relief = "groove", image=square(board[x][y])).grid(row=x, column=y)#text=board[x][y]+"\n"+"\n"
            y+=1
        x+=1

    #draw robots
    Label(root, image=r1cursor(r1[2])).grid(row=r1[0], column=r1[1])
    Label(root, image=r2cursor(r1[2])).grid(row=r2[0], column=r2[1])
    Label(root, image=r3cursor(r1[2])).grid(row=r3[0], column=r3[1])
    Label(root, image=r4cursor(r1[2])).grid(row=r4[0], column=r4[1])
    Label(root, image=r5cursor(r1[2])).grid(row=r5[0], column=r5[1])
    Label(root, image=r6cursor(r1[2])).grid(row=r6[0], column=r6[1])
    Label(root, image=r7cursor(r1[2])).grid(row=r7[0], column=r7[1])
    Label(root, image=r8cursor(r1[2])).grid(row=r8[0], column=r8[1])


    #victorytokens
    #draw energycubes

#check tile the robot is on for permanent hazard (i.e. bottomless pit)
def checkTile(robot):
    dummy=0

def forw(robot):
    if robot[2] == "n":
        robot[0] -=1
    elif robot[2] == "e":
        robot[1] +=1
    elif robot[2] == "s":
        robot[0] +=1
    elif robot[2] == "w":
        robot[1] -=1
    else:
        print ("mistake at def forw")
    checkTile(robot)
    drawBoard()

def backw(robot):
    if robot[2] == "n":
        robot[0] +=1
    elif robot[2] == "e":
        robot[1] -=1
    elif robot[2] == "s":
        robot[0] -=1
    elif robot[2] == "w":
        robot[1] +=1
    else:
        print ("mistake at def backw")
    checkTile(robot)
    drawBoard()

'''
            else:
                print ("mistake at def move(), 1for")
        elif self.registers[reg] == "2for":
            if self.direction == "n":
                self.position[0] -= 2
            elif self.direction == "e":
                self.position[1] += 2
            elif self.direction == "s":
                self.position[0] += 2
            elif self.direction == "w":
                self.position[1] -= 2
            else:
                print ("mistake at def move(), 2for")
        elif self.registers[reg] == "3for":
            if self.direction == "n":
                self.position[0] -= 3
            elif self.direction == "e":
                self.position[1] += 3
            elif self.direction == "s":
                self.position[0] += 3
            elif self.direction == "w":
                self.position[1] -= 3
            else:
                print ("mistake at def move(), 3for")
        elif self.registers[reg] == "1back":
            if self.direction == "n":
                self.position[0] += 1
            elif self.direction == "e":
                self.position[1] -= 1
            elif self.direction == "s":
                self.position[0] -= 1
            elif self.direction == "w":
                self.position[1] += 1
            else:
                print ("mistake at def move(), 1back")
        elif self.registers[reg] == "left":
            if self.direction == "n":
                self.direction = "w"
            elif self.direction == "e":
                self.direction = "n"
            elif self.direction == "s":
                self.direction = "e"
            elif self.direction == "w":
                self.direction = "s"
            else:
                print ("mistake at def move(), left")
        elif self.registers[reg] == "right":
            if self.direction == "n":
                self.direction = "e"
            elif self.direction == "e":
                self.direction = "s"
            elif self.direction == "s":
                self.direction = "w"
            elif self.direction == "w":
                self.direction = "n"
            else:
                print ("mistake at def move(), right")
        elif self.registers[reg] == "uturn":
            if self.direction == "n":
                self.direction = "s"
            elif self.direction == "e":
                self.direction = "w"
            elif self.direction == "s":
                self.direction = "n"
            elif self.direction == "w":
                self.direction = "e"
            else:
                print ("mistake at def move(), uturn")
        elif self.registers[reg] == "again":
            if reg > 1:
                move(reg-1)
            else:
                print ("dumbass, you wasted your repeat card")
        elif self.registers[reg] == "powerup":
            self.energy += 1

        #special cards that are added to the deck later go here
        else:
            print ("mistake at def move(reg)")

#create r1
r1=robot
    '''




def test():
    r1[1] +=1
    r1[2] = "s"

drawB=Button(command=drawBoard,text="draw")
drawB.grid(row=0,column=200)

testB=Button(command=test,text="test")
testB.grid(row=0,column=201)


def shuffleDeck(deck):
    dummy=0

drawBoard()
#take 5 cards, if deck is empty, take discard list, shuffle, and make new deck list









root.mainloop()


