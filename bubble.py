from graphics import *
from random import *
from math import *
from time import *




class Bubble:

    def __init__(self,win,x,y):
        self.win=win
        self.x=x
        self.y=y
        self.size=randrange(18,32)
        self.polygon=Circle(Point(x,y),self.size)
        self.pbubble=randrange(5,20)
        self.pbubbletype=0
        if self.pbubble == 18:
            pbubbletype=randrange(1,5)
            self.pbubbletype=pbubbletype
            self.polygon.setFill('lightcyan')
            if pbubbletype==1:
                self.polygon.setFill('orange')#needleoctodirectional
            if pbubbletype==2:
                self.polygon.setFill('yellow')#electrobeamsquare
            if pbubbletype==3:
                self.polygon.setFill('limegreen')#mineranddirectional
            if pbubbletype==4:
                self.polygon.setFill('skyblue')#bubblestanieria
            if pbubbletype==5:
                self.polygon.setFill('darkviolet')#explodemine
            if pbubbletype==6:
                self.polygon.setFill('red')#flashomnidirectionalexplosion
            if pbubbletype==7:
                self.polygon.setFill('black')#3bombcollumndrop
            if pbubbletype==8:
                self.polygon.setFill('darkred')#bispiraling
        else:
            self.polygon.setFill('lightcyan')
        self.xvel=0
        self.yvel=0
        self.polygon.draw(win)
   

    def move(self):
        self.y+=self.yvel
        self.polygon.move(self.xvel,self.yvel)


    def undraw(self):
        self.polygon.undraw()


    def pop(self,pneedles,pbeams,pmines,bubbles,pbombmines,pmineexplosions):
        if self.pbubbletype == 1:
            for i in range(2):
                needlespeed=randrange(5,9)
                upneedle=Pneedle(self.win,self.x,self.y,0,28,0,4*needlespeed)
                uprightneedle=Pneedle(self.win,self.x,self.y,21,21,3*needlespeed,3*needlespeed)
                rightneedle=Pneedle(self.win,self.x,self.y,28,0,4*needlespeed,0)
                downrightneedle=Pneedle(self.win,self.x,self.y,21,-21,3*needlespeed,-3*needlespeed)
                downneedle=Pneedle(self.win,self.x,self.y,0,-28,0,-4*needlespeed)
                downleftneedle=Pneedle(self.win,self.x,self.y,-21,-21,-3*needlespeed,-3*needlespeed)
                leftneedle=Pneedle(self.win,self.x,self.y,-28,0,-4*needlespeed,0)
                upleftneedle=Pneedle(self.win,self.x,self.y,-21,21,-3*needlespeed,3*needlespeed)
                pneedles.append(upneedle)
                pneedles.append(uprightneedle)
                pneedles.append(rightneedle)
                pneedles.append(downrightneedle)
                pneedles.append(downneedle)
                pneedles.append(downleftneedle)
                pneedles.append(leftneedle)
                pneedles.append(upleftneedle)
        if self.pbubbletype == 2:
            if self.y > 100:
                squarebeam = Pelecbeam(self.win,self.x,self.y,80,80)
                pbeams.append(squarebeam)
        if self.pbubbletype == 3:
            if self.y > 115:
                for i in range(randrange(8,15)):
                    mine = Pmine(self.win,self.x+randrange(-8,8)*(i+2*4),self.y+randrange(-8,8)*(i+2*4))
                    pmines.append(mine)
        if self.pbubbletype == 4:
            for i in range(randrange(6,11)):
                bubble=Bubble(self.win,self.x+randrange(-90,90),self.y+randrange(-90,90))
                bubble.yvel=1
                bubbles.append(bubble)
        if self.pbubbletype == 5:
            exmine = Pbombmine(self.win,self.x,self.y)
            pbombmines.append(exmine)

class Pneedle:

    def __init__(self,win,x,y,xlength,ylength,xvel,yvel):
        self.win=win
        self.x=x
        self.y=y
        self.xlength=xlength
        self.ylength=ylength
        self.polygon=Polygon(Point(x+self.xlength,y+self.ylength),Point(x+int(self.ylength/6),y-int(self.xlength/6)),Point(x-int(self.ylength/6),y+int(self.xlength/6)))
        self.xvel=xvel
        self.yvel=yvel
        self.polygon.setFill('orange')
        self.polygon.draw(win)
   

    def move(self):
        self.y+=self.yvel
        self.x+=self.xvel
        self.polygon.move(self.xvel,self.yvel)


    def undraw(self):
        self.polygon.undraw()


class Pelecbeam:
    def __init__(self,win,x,y,xlength,ylength):
        self.win=win
        self.x=x
        self.y=y
        self.xlength=xlength
        self.ylength=ylength
        self.polygon=Rectangle(Point(x+xlength,y+ylength),Point(x-xlength,y-ylength))
        self.polygon.setFill('yellow')
        self.polygon.draw(win)
        self.electimer=0

    def undraw(self):
        self.polygon.undraw()


class Pmine:
    def __init__(self,win,x,y):
        self.win=win
        self.x=x
        self.y=y
        self.polygon=Circle(Point(x,y),6)
        self.polygon.setFill('limegreen')
        self.polygon.draw(win)

    def undraw(self):
        self.polygon.undraw()

class Pbombmine:
    def __init__(self,win,x,y):
        self.win=win
        self.x=x
        self.y=y
        self.polygon=Circle(Point(x,y),18)
        self.polygon.setFill('darkviolet')
        self.polygon.draw(win)

class Pmineexplosion:
    def __init__(self,win,x,y):
        self.win=win
        self.x=x
        self.y=y
        self.polygon=Circle(Point(x,y),36)
        self.polygon.setFill('lemonchiffon')
        self.polygon.draw(win)


def main():
    win=GraphWin("Bubbles",800,800)
    win.setCoords(0,0,1000,1000)

    bubbles=[]

    bubbletimer=0

    bubblespeedincrease=0

    pneedles=[]

    pbeams=[]

    pmines=[]

    pbombmines=[]

    pmineexplosions=[]

   

   

    #bubble=Bubble(win,randrange(25,975),0)
    #bubble.yvel=0.1
    #bubbles.append(bubble)


    while True:

        bubbletimer+=1
        if bubbletimer == 17:
            bubble=Bubble(win,randrange(25,975),-30)
            bubble.yvel=0.075*randrange(6,16) + bubblespeedincrease
            bubbles.append(bubble)
            bubbletimer=0

        pt=win.checkMouse()
        for bubble in bubbles:
            #movement
            bubble.move()
            #check if at top
            if (bubble.y>1020):
                bubble.undraw()
                bubbles.remove(bubble)
                #bubble.yvel = 0
            #check against mouse
            bubblepop = randrange(0,1000)
            if bubblepop == 28:
                if bubble.pbubble != 18:
                    #print("ceased")
                    if bubble in bubbles:
                        bubble.undraw()
                        bubbles.remove(bubble)
            if pt!=None:
                if abs(pt.getX()-bubble.x)<bubble.size+10 and abs(pt.getY()-bubble.y)<bubble.size+10:
                    bubble.pop(pneedles,pbeams,pmines,bubbles,pbombmines,pmineexplosions)
                    if bubble in bubbles:
                        bubble.undraw()
                        bubblespeedincrease+=0.005
                    if bubble in bubbles:
                        bubbles.remove(bubble)
                       
        for needle in pneedles:
            needle.move()
            if needle.y > 1000:
                pneedles.remove(needle)
                needle.undraw()
            for bubble in bubbles:
                if abs(needle.x-bubble.x)<bubble.size and abs(needle.y-bubble.y)<bubble.size:
                    bubble.pop(pneedles,pbeams,pmines,bubbles,pbombmines,pmineexplosions)
                    if bubble in bubbles:
                        bubble.undraw()
                        bubblespeedincrease+=0.005
                    if bubble in bubbles:
                        bubbles.remove(bubble)
                       
        for beam in pbeams:
            for bubble in bubbles:
                if abs(beam.x-bubble.x)<bubble.size+beam.xlength and abs(beam.y-bubble.y)<bubble.size+beam.ylength:
                    bubble.pop(pneedles,pbeams,pmines,bubbles,pbombmines,pmineexplosions)
                    if bubble in bubbles:
                        bubble.undraw()
                    if bubble in bubbles:
                        bubbles.remove(bubble)
            beam.electimer+=randrange(1,3)
            if beam.electimer > 560:
                beam.undraw()
                bubblespeedincrease+=0.005
                pbeams.remove(beam)

        for mine in pmines:
            for bubble in bubbles:
                if abs(mine.x-bubble.x)<bubble.size+5 and abs(mine.y-bubble.y)<bubble.size+5:
                    bubble.pop(pneedles,pbeams,pmines,bubbles,pbombmines,pmineexplosions)
                    if bubble in bubbles:
                        bubble.undraw()
                        bubbles.remove(bubble)
                    if mine in pmines:
                        mine.undraw()
                        bubblespeedincrease+=0.005
                        pmines.remove(mine)

        for exmine in pbombmines:
            for bubble in bubbles:
                if abs(exmine.x-bubble.x)<bubble.size+5 and abs(exmine.y-bubble.y)<bubble.size+5:
                    mineexplosion = Pmineexplosion(exmine.win,exmine.x,exmine.y)
                    if bubble in bubbles:
                        bubble.undraw()
                        bubbles.remove(bubble)
                    if exmine in pbombmines:
                        exmine.undraw()
                        bubblespeedincrease+=0.005
                        pbombmines.remove(exmine)

main()
