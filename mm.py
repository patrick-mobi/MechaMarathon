from tkinter import *
root = Tk()


#variables for images
neutral = PhotoImage(file="graphics/neutral.gif")
r1n =     PhotoImage(file="graphics/r1n.gif")
r1e =     PhotoImage(file="graphics/r1e.gif")
r1s =     PhotoImage(file="graphics/r1s.gif")
r1w =     PhotoImage(file="graphics/r1w.gif")

#robots, list of
#position, direction, tokens, energy, register, deck, discard, hand
r1 = [2,2,"n",0,5,["","","","",""],["1for","1for","1for","1for","1for","2for","2for","2for","3for","1back","left","left","left","right","right","right","uturn","again","again","powerup"], [], []]

#define all squares
l00=Label(root, width=30, height=30, image=neutral)
l10=Label(root, width=30, height=30, image=neutral)
l20=Label(root, width=30, height=30, image=neutral)
l30=Label(root, width=30, height=30, image=neutral)
l40=Label(root, width=30, height=30, image=neutral)
l01=Label(root, width=30, height=30, image=neutral)
l11=Label(root, width=30, height=30, image=neutral)
l21=Label(root, width=30, height=30, image=neutral)
l31=Label(root, width=30, height=30, image=neutral)
l41=Label(root, width=30, height=30, image=neutral)
l02=Label(root, width=30, height=30, image=neutral)
l12=Label(root, width=30, height=30, image=neutral)
l22=Label(root, width=30, height=30, image=neutral)
l32=Label(root, width=30, height=30, image=neutral)
l42=Label(root, width=30, height=30, image=neutral)
l03=Label(root, width=30, height=30, image=neutral)
l13=Label(root, width=30, height=30, image=neutral)
l23=Label(root, width=30, height=30, image=neutral)
l33=Label(root, width=30, height=30, image=neutral)
l43=Label(root, width=30, height=30, image=neutral)
l04=Label(root, width=30, height=30, image=neutral)
l14=Label(root, width=30, height=30, image=neutral)
l24=Label(root, width=30, height=30, image=neutral)
l34=Label(root, width=30, height=30, image=neutral)
l44=Label(root, width=30, height=30, image=neutral)

lr1n=Label(width=30, height=30, image=r1n)
lr1e=Label(width=30, height=30, image=r1e)
lr1s=Label(width=30, height=30, image=r1s)
lr1w=Label(width=30, height=30, image=r1w)




#draw all squares
def drawBoard():
    global r1
    #draw empty board
    l00.grid(row=0,column=0)
    l10.grid(row=1,column=0)
    l20.grid(row=2,column=0)
    l30.grid(row=3,column=0)
    l40.grid(row=4,column=0)
    l01.grid(row=0,column=1)
    l11.grid(row=1,column=1)
    l21.grid(row=2,column=1)
    l31.grid(row=3,column=1)
    l41.grid(row=4,column=1)
    l02.grid(row=0,column=2)
    l12.grid(row=1,column=2)
    l22.grid(row=2,column=2)
    l32.grid(row=3,column=2)
    l42.grid(row=4,column=2)
    l03.grid(row=0,column=3)
    l13.grid(row=1,column=3)
    l23.grid(row=2,column=3)
    l33.grid(row=3,column=3)
    l43.grid(row=4,column=3)
    l04.grid(row=0,column=4)
    l14.grid(row=1,column=4)
    l24.grid(row=2,column=4)
    l34.grid(row=3,column=4)
    l44.grid(row=4,column=4)

    #draw robots on board
    lr1n.grid(row=r1[0],column=r1[1])
    print ("board drawn")

def test():
    r1[1] +=1

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




drawB=Button(command=drawBoard,text="draw")
drawB.grid(row=0,column=7)

testB=Button(command=test,text="test")
testB.grid(row=0,column=8)


def shuffleDeck(deck):
    dummy=0

drawBoard()
#take 5 cards, if deck is empty, take discard list, shuffle, and make new deck list









root.mainloop()


