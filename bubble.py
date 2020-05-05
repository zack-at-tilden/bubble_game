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
        self.pbubble=randrange(7,20)
        self.pbubbletype=0
        if self.pbubble == 18:
            pbubbletype=randrange(1,6)

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


    def pop(self,pneedles,pbeams,pmines,bubbles,pbombmines,pmineexplosions,pexplosions):
        if self.pbubbletype == 1:
                upneedle=Pneedle(self.win,self.x,self.y,0,28,0,24)
                uprightneedle=Pneedle(self.win,self.x,self.y,21,21,18,18)
                rightneedle=Pneedle(self.win,self.x,self.y,28,0,24,0)
                downrightneedle=Pneedle(self.win,self.x,self.y,21,-21,18,-18)
                downneedle=Pneedle(self.win,self.x,self.y,0,-28,0,-24)
                downleftneedle=Pneedle(self.win,self.x,self.y,-21,-21,-18,-18)
                leftneedle=Pneedle(self.win,self.x,self.y,-28,0,-24,0)
                upleftneedle=Pneedle(self.win,self.x,self.y,-21,21,-18,18)
                pneedles.append(upneedle)
                pneedles.append(uprightneedle)
                pneedles.append(rightneedle)
                pneedles.append(downrightneedle)
                pneedles.append(downneedle)
                pneedles.append(downleftneedle)
                pneedles.append(leftneedle)
                pneedles.append(upleftneedle)
                upneedle=Pneedle(self.win,self.x,self.y,0,28,0,16)
                uprightneedle=Pneedle(self.win,self.x,self.y,21,21,12,12)
                rightneedle=Pneedle(self.win,self.x,self.y,28,0,16,0)
                downrightneedle=Pneedle(self.win,self.x,self.y,21,-21,12,-12)
                downneedle=Pneedle(self.win,self.x,self.y,0,-28,0,-16)
                downleftneedle=Pneedle(self.win,self.x,self.y,-21,-21,-12,-12)
                leftneedle=Pneedle(self.win,self.x,self.y,-28,0,-16,0)
                upleftneedle=Pneedle(self.win,self.x,self.y,-21,21,-12,12)

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
        if self.pbubbletype == 6:
            flashexplosion = Pflash(self.win,self.x,self.y)
            pexplosions.append(flashexplosion)


       

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

    def undraw(self):
        self.polygon.undraw()

class Pmineexplosion:
    def __init__(self,win,x,y):
        self.win=win
        self.x=x
        self.y=y
        self.polygon=Circle(Point(x,y),66)
        self.polygon.setFill('lemonchiffon')
        self.polygon.draw(win)
        self.mineexplosiontimer=0

    def undraw(self):
        self.polygon.undraw()

class Pflash:
    def __init__(self,win,x,y):
        self.win=win
        self.x=x
        self.y=y
        self.polygon=Circle(Point(x,y),126)
        self.polygon.setFill('papayawhip')
        self.polygon.draw(win)
        self.mineexplosiontimer=0


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

    pexplosions=[]    

   

   

    #bubble=Bubble(win,randrange(25,975),0)
    #bubble.yvel=0.1
    #bubbles.append(bubble)


    while True:

        bubbletimer+=1
        if bubbletimer == 16:
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
                    bubble.pop(pneedles,pbeams,pmines,bubbles,pbombmines,pmineexplosions,pexplosions)
                    if bubble in bubbles:
                        bubble.undraw()
                        bubblespeedincrease+=0.005
                    if bubble in bubbles:
                        bubbles.remove(bubble)
                       
        for needle in pneedles:
            needle.move()
            if needle.y > 1000:
                needle.undraw()
                if needle in pneedles:
                    pneedles.remove(needle)
            if needle.x > 1000:
                needle.undraw()
                if needle in pneedles:
                    pneedles.remove(needle)
            if needle.x < 0:
                needle.undraw()
                if needle in pneedles:
                    pneedles.remove(needle)
            if needle.y < 0:
                needle.undraw()
                if needle in pneedles:
                    pneedles.remove(needle)
            for bubble in bubbles:
                if abs(needle.x-bubble.x)<bubble.size and abs(needle.y-bubble.y)<bubble.size:
                    bubble.pop(pneedles,pbeams,pmines,bubbles,pbombmines,pmineexplosions,pexplosions)
                    if bubble in bubbles:
                        bubble.undraw()
                        bubblespeedincrease+=0.005
                    if bubble in bubbles:
                        bubbles.remove(bubble)
                       
        for beam in pbeams:
            for bubble in bubbles:
                if abs(beam.x-bubble.x)<bubble.size+beam.xlength and abs(beam.y-bubble.y)<bubble.size+beam.ylength:
                    bubble.pop(pneedles,pbeams,pmines,bubbles,pbombmines,pmineexplosions,pexplosions)
                    if bubble in bubbles:
                        bubble.undraw()
                    if bubble in bubbles:
                        bubbles.remove(bubble)
            beam.electimer+=1
            if beam.electimer > 400:
                beam.undraw()
                bubblespeedincrease+=0.005
                pbeams.remove(beam)

        for mine in pmines:
            for bubble in bubbles:
                if abs(mine.x-bubble.x)<bubble.size+5 and abs(mine.y-bubble.y)<bubble.size+5:
                    bubble.pop(pneedles,pbeams,pmines,bubbles,pbombmines,pmineexplosions,pexplosions)
                    if bubble in bubbles:
                        bubble.undraw()
                        bubbles.remove(bubble)
                    if mine in pmines:
                        mine.undraw()
                        bubblespeedincrease+=0.005
                        pmines.remove(mine)

        for exmine in pbombmines:
            for bubble in bubbles:
                if abs(exmine.x-bubble.x)<bubble.size+16 and abs(exmine.y-bubble.y)<bubble.size+16:
                    if exmine in pbombmines:
                        exmine.undraw()
                        bubblespeedincrease+=0.005
                        pbombmines.remove(exmine)
                        mineexplosion = Pmineexplosion(exmine.win,exmine.x,exmine.y)
                        pmineexplosions.append(mineexplosion)

        for mineexplosion in pmineexplosions:
            for bubble in bubbles:
                if abs(mineexplosion.x-bubble.x)<bubble.size+60 and abs(mineexplosion.y-bubble.y)<bubble.size+60:
                    bubble.pop(pneedles,pbeams,pmines,bubbles,pbombmines,pmineexplosions,pexplosions)
                    if bubble in bubbles:
                        bubble.undraw()
                        bubbles.remove(bubble)
            mineexplosion.mineexplosiontimer+=1
            if mineexplosion.mineexplosiontimer==5:
                mineexplosion.undraw()
                pmineexplosions.remove(mineexplosion)


main()
