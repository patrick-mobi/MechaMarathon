from tkinter import *
root = Tk()

def test():
    i=1

#variables for images
neutral = PhotoImage(file="graphics/neutral.gif")
r1n =     PhotoImage(file="graphics/r1n.gif")
r1e =     PhotoImage(file="graphics/r1e.gif")
r1s =     PhotoImage(file="graphics/r1s.gif")
r1w =     PhotoImage(file="graphics/r1w.gif")

class robot():
    def __init__(self):
        self.postion = [0,0]
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

#create r1
r1=robot
    

    
#define all squares
l00=Label(width=30, height=30, image=neutral)
l10=Label(width=30, height=30, image=neutral)
l20=Label(width=30, height=30, image=neutral)
l30=Label(width=30, height=30, image=neutral)
l40=Label(width=30, height=30, image=neutral)
l01=Label(width=30, height=30, image=neutral)
l11=Label(width=30, height=30, image=neutral)
l21=Label(width=30, height=30, image=neutral)
l31=Label(width=30, height=30, image=neutral)
l41=Label(width=30, height=30, image=neutral)
l02=Label(width=30, height=30, image=neutral)
l12=Label(width=30, height=30, image=neutral)
l22=Label(width=30, height=30, image=neutral)
l32=Label(width=30, height=30, image=neutral)
l42=Label(width=30, height=30, image=neutral)
l03=Label(width=30, height=30, image=neutral)
l13=Label(width=30, height=30, image=neutral)
l23=Label(width=30, height=30, image=neutral)
l33=Label(width=30, height=30, image=neutral)
l43=Label(width=30, height=30, image=neutral)
l04=Label(width=30, height=30, image=neutral)
l14=Label(width=30, height=30, image=neutral)
l24=Label(width=30, height=30, image=neutral)
l34=Label(width=30, height=30, image=neutral)
l44=Label(width=30, height=30, image=neutral)

lr1n=Label(width=30, height=30, image=r1n)

b1for=Button(command=test(), width=0, text="1for")

#draw all squares
def drawBoard():
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
    lr1n.grid(row=0,column=0)
    
    #draw buttons
    b1for.grid(row=0,column=5)



def shuffleDeck(deck):
    dummy=0


#take 5 cards, if deck is empty, take discard list, shuffle, and make new deck list









drawBoard()
root.mainloop()


