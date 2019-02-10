from tkinter import *
root = Tk()

def test():
    i=1

#counts drawn squares
squareCount = 0

class robot:
    def __init__(self):
        self.postion = [1,1]
        self.direction = "n"
        self.tokens = 0
        self.energy = 5
        self.registers = ["","","","",""]
        self.deck = ["1for","1for","1for","1for","1for","2for","2for","2for","3for","1back","left","left","left","right","right","right","uturn","again","again","powerup"]
        self.discard = []
        self.hand = []

    #reads a given register and moves the robot accordingly
    def move(reg):
        if self.registers[reg] == "1for":
            if self.direction == "n":
                self.position[0] -= 1
            elif self.direction == "e":
                self.position[1] += 1
            elif self.direction == "s":
                self.position[0] += 1
            elif self.direction == "w":
                self.position[1] -= 1
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


def drawSquare(row,column):
    global squareCount
    

    
#define all squares
neutral1=Label(width=3, height=3, text="[ ]")
neutral2=Label(width=3, height=3, text="[ ]")
neutral3=Label(width=3, height=3, text="[ ]")
neutral4=Label(width=3, height=3, text="[ ]")
test=Button(command=test(), width=1)

#draw all squares
def drawBoard():
    global squareCount
    squareCount = 0
    neutral1.grid(row=0,column=0)
    neutral2.grid(row=0,column=1)
    neutral3.grid(row=1,column=0)
    neutral4.grid(row=1,column=1)
    
    test.grid(row=3,column=3)



def shuffleDeck(deck):
    dummy=0


#take 5 cards, if deck is empty, take discard list, shuffle, and make new deck list









drawBoard()
root.mainloop()


