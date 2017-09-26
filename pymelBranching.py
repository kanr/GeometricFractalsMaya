import maya.cmds as cmds
from pymel.core import *
"""
Josh Lopez-Binder May 2015

Connor Aitken 2017


Make a geometric branching fractal with "residue"
Run script in Maya. Then select base-object and run MakeArray(<nLevels>) in Python Command Line. Move around the
two children of the root node. Try scaling them by about 0.5 to get not-self-intersecting
patterns.

"""
# Global Variables
axes = ['X', 'Y', 'Z']
translate = ['translate'+x for x in axes]
rot = ['rotate'+x for x in axes]
scale = ['scale'+x for x in axes]
attrs = translate + rot + scale

def makeArray(nBranch=2,nLevels=7):

    # selected = cmds.ls(sl=1)
    # Make user selection the base obj or create a cube
    selected = ls(sl=1)
    if len(selected) == 0:
        baseObj = cmds.polyCube(w=1,d=1,h=1)[0]
    else:
        baseObj = selected[0] #right now hard coded for the first selection
        #TODO: filter selection for polygons, nurbs, etc.

    makeTree(baseObj,baseObj,nBranch,nLevels,1)


def makeTree(parentObj,prevGen,nBranch,maxDepth,currDepth):

    if currDepth >= maxDepth:
        return
    else:
        newGen = makeNChildren(nBranch,parentObj,prevGen,currDepth!=1)
        # increment towards the base case currDepth = maxDepth
        currDepth = currDepth+1

        # Generate branch for each level
        for i in xrange(nBranch):
            obj = newGen[i]
            # recursive call
            makeTree(obj,newGen,nBranch,maxDepth,currDepth)

def makeNChildren(nChildren,parentObj,prevGen,makeCon=True):

    objList = []
    prevDup = parentObj
    for i in xrange(nChildren):
        # DUPLICATE
        newObj = duplicate(prevDup,rr=True,ilf=True,rc=True)[0]

        # PARENT
        if i==0:
            parent(newObj,parentObj)

        # CONNECT XFORM ATTRS
        if nChildren == len(prevGen):
            connectAttrs(newObj,prevGen[i])
        elif len(prevGen) <= 1:
            connectAttrs(newObj,parentObj)

        objList.append(newObj)
        prevDup = newObj

    return objList

def connectAttrs(newObj,oldObj):
    for attr in attrs:
        cmds.expression(s = newObj+'.' +attr+ ' = ' + oldObj+'.' +attr)
