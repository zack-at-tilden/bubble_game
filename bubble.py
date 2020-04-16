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
        self.pbubble=randrange(18,22)
        self.pbubbletype=0
        if self.pbubble == 18:
            pbubbletype=randrange(1,4)
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
                self.polygon.setFill('black')#bombdrop
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


    def pop(self,pneedles,pbeams):
        if self.pbubbletype == 1:
            upneedle=Pneedle(self.win,self.x,self.y,0,24,0,20)
            uprightneedle=Pneedle(self.win,self.x,self.y,18,18,15,15)
            rightneedle=Pneedle(self.win,self.x,self.y,24,0,20,0)
            downrightneedle=Pneedle(self.win,self.x,self.y,18,-18,15,-15)
            downneedle=Pneedle(self.win,self.x,self.y,0,-24,0,-20)
            downleftneedle=Pneedle(self.win,self.x,self.y,-18,-18,-15,-15)
            leftneedle=Pneedle(self.win,self.x,self.y,-24,0,-20,0)
            upleftneedle=Pneedle(self.win,self.x,self.y,-18,18,-15,15)
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
                horibeam = Pelecbeam(self.win,self.x,self.y,80,20)
                vertbeam = Pelecbeam(self.win,self.x,self.y,20,80)
                diagbeam1 = Pelecbeam(self.win,self.x,self.y,-80,80)
                diagbeam2 = Pelecbeam(self.win,self.x,self.y,80,-80)
                pbeams.append(horibeam)
                pbeams.append(vertbeam)
                pbeams.append(diagbeam1)
                pbeams.append(diagbeam2)              

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


def main():
    win=GraphWin("Bubbles",800,800)
    win.setCoords(0,0,1000,1000)

    bubbles=[]

    bubbletimer=0

    bubblespeedincrease=0

    pneedles=[]

    pbeams=[]

   

   

    #bubble=Bubble(win,randrange(25,975),0)
    #bubble.yvel=0.1
    #bubbles.append(bubble)


    while True:

        bubbletimer+=1
        if bubbletimer == 24:
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
                if abs(pt.getX()-bubble.x)<bubble.size and abs(pt.getY()-bubble.y)<bubble.size:
                    bubble.pop(pneedles,pbeams)
                    if bubble in bubbles:
                        bubble.undraw()
                        bubblespeedincrease+=0.01
                    if bubble in bubbles:
                        bubbles.remove(bubble)
                       
        for upneedle in pneedles:
            upneedle.move()
            if upneedle.y > 1000:
                pneedles.remove(upneedle)
            for bubble in bubbles:
                if abs(upneedle.x-bubble.x)<bubble.size and abs(upneedle.y-bubble.y)<bubble.size:
                    bubble.pop(pneedles,pbeams)
                    if bubble in bubbles:
                        bubble.undraw()
                    if bubble in bubbles:
                        bubbles.remove(bubble)
                       
        for beam in pbeams:
            for bubble in bubbles:
                if abs(beam.x-bubble.x)<bubble.size+beam.xlength and abs(beam.y-bubble.y)<bubble.size+beam.ylength:
                    bubble.pop(pneedles,pbeams)
                    if bubble in bubbles:
                        bubble.undraw()


                    if bubble in bubbles:
                        bubbles.remove(bubble)
            beam.electimer+=1
            if beam.electimer > 300:
                beam.undraw()
                pbeams.remove(beam)

main()
