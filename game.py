#kwe.k.u from KEYstroke's version of connect the dots
from random import choice

nwn, nne = False, False
nww, nc, nee=False, False, False
wc,ce,=False, False
sws, sse=False,False
nwc, nec, sec, swc= False,False,False,False
nw,ne,se,sw= False,False,False,False

currentplayer ="Player"
currentposition=choice(("North","Northwest","Northeast"))

lefttopowner, righttopowner= None, None
leftbottomowner, rightbottomowner= None, None

def updateSquare(sq):
    global leftbottomowner, rightbottomowner, lefttopowner, righttopowner
    if sq=="LeftTop" and lefttopowner==None and nwn and nww and nc and wc:
        lefttopowner= currentplayer
        return True
    elif sq=="RightTop" and righttopowner==None and nne and nee and ce and wc:
        righttopowner= currentplayer
        return True
    elif sq=="LeftBottom" and leftbottomowner==None and wc and cs and sws and wsw:
        leftbottomowner= currentplayer
        return True
    elif sq=="RightBottom" and rightbottomowner==None and ce and ese and sse and cs:
        rightbottomowner = currentplayer
        return True
    else:
        return False

def updateSquares():
    lt= updateSquare("LeftTop")
    rt=updateSquare("RightTop")
    lb=updateSquare("LeftBottom")
    rb=updateSquare("RightBottom")

def addLine(line):
    global nwn, nne, nww, nc, nee, wc, ce, wsw, cs, ese, sws, sse, nwc, nec,sec, swc,nw,ne,se,sw, currentplayer

    lineadded=False
    if line=="NorthwestNorth" and not nwn:
        nwn=True
        lineadded=True
    elif line=="NorthNortheast" and not nne:
        nne=True
        lineadded=True
    elif line=="NorthwestWest" and not nww:
        nww=True
        lineadded=True
    elif line=="NorthCenter" and not nc:
        nc=True
        lineadded=True
    elif line=="NortheastEast" and not nee:
        nee=True
        lineadded=True
    elif line=="WestCenter" and not wc:
        wc=True
        lineadded=True
    elif line=="CenterEast" and not ce:
        ce=True
        lineadded=True
    elif line=="WestSouthwest" and not wsw:
        wsw=True
        lineadded=True
    elif line=="CenterSouth" and not cs:
        cs=True
        lineadded=True
    elif line=="EastSoutheast" and not ese:
        ese=True
        lineadded=True
    elif line=="SouthwestSouth" and not sws:
        sws=True
        lineadded=True
    elif line=="NorthwestCenter" and not nwc:
        nwc=True
        lineadded=True
    elif line=="NorthWest" and not nw:
        nw=True
        lineadded=True
    elif line=="NortheastCenter" and not nec:
        nec=True
        lineadded=True
    elif line=="NorthEast" and not ne:
        ne=True
        lineadded=True
    elif line=="SoutheastCenter" and not sec:
        sec=True
        lineadded=True
    elif line=="SouthEast" and not se:
        se=True
        lineadded=True
    elif line=="SouthwestCenter" and not swc:
        swc=True
        lineadded=True
    elif line=="SouthWest" and not sw:
        sw=True
        lineadded=True
    elif line=="SouthSoutheast" and not sse:
        sse=True
        lineadded=True
    if lineadded and not updateSquares():
        if currentplayer=="Player":
            currentplayer=="Y"
        else:
            currentplayer= "Player"
        return lineadded

def squareOwner(sq):
    if sq=="LeftTop":
        return lefttopowner
    elif sq=="RighTop":
        return righttopowner
    elif sq=="LeftBottom":
        return leftbottomowner
    elif sq=="RightBottom":
        return rightbottomowner
    else:
        return None

def checkLine(line):
    if line=="NorthwestNorth":
        return nwn
    elif line=="NorthNortheast":
        return nne
    elif line=="NorthwestWest":
        return nww
    elif line=="NorthCenter":
        return nc
    elif line=="NortheastEast":
        return nee
    elif line=="WestCenter":
        return wc
    elif line=="CenterEast":
        return ce
    elif line=="WestSouthwest":
        return wsw
    elif line=="CenterSouth":
        return cs
    elif line=="EastSoutheast":
        return ese
    elif line=="SouthwestSouth":
        return sws
    elif line=="SouthSoutheast":
        return sse
    elif line=="NorthwestCenter":
        return nwc
    elif line=="NorthWest":
        return nw
    elif line=="NortheastCenter":
        return nec
    elif line=="NorthEast":
        return ne
    elif line=="SoutheastCenter":
        return sec
    elif line=="SouthEast":
        return se
    elif line=="SouthwestCenter":
        return swc
    elif line=="SouthWest":
        return sw
    else:
        return False

#winner()
def initializeBoard():
    global nwn, nne, nww, nc, nee, wc, ce, wsw, cs, ese,\
           sws, sse, currentplayer, lefttopowner, leftbottomowner,\
           righttopowner, rightbottomowner, nwc,nw,nec,ne,sec,se,swc,sw
    nwn=nne= nww=nc= nee=wc=ce=wsw=cs=ese=sws=sse=nwc=nw=nec=ne=sec=se=swc=sw=False

    lefttopowner=righttopowner=leftbottomowner=rightbottomowner=None
    currentplayer="Player"

def currentPlayer():
    return currentplayer

#full function additions start here
