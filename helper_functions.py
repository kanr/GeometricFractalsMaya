import maya.cmds as cmds
"""
Josh Lopez-Binder May 2015
Make a geometric branching fractal with "residue"


Connor Aitken September 2017


"""

def prune(generation=None):
    """Run this function with the root node selected to remove a level from
    from the branching structure"""
    if generation==None:
        generation = getFinalGen(cmds.ls(sl=1)[0])
    updatedGen = getParents(generation)
    cmds.delete(generation)
    return updatedGen

def grow(generation=None,nBranch=3):
    """run the function with the root node selected to add another level
    to the structure"""
    if generation==None:
        generation=getFinalGen(cmds.ls(sl=1)[0])
    assert areLeaves(generation), "generation was not the final one!"
    updatedGen = []
    for obj in generation:
        updatedGen.extend(makeNChildren(nBranch,obj,getParentGen(obj),makeCon=True))
    return updatedGen

def getParentGen(obj):
    grandParent = getGrandParent(obj)
    assert grandParent!=None
    return cmds.listRelatives(grandParent,typ="transform",c=True)

def getGrandParent(obj):
    parent = cmds.listRelatives(obj,p=True)
    return cmds.listRelatives(parent,p=True)


def areLeaves(generation):
    if None == cmds.listRelatives(generation,c=True, typ="transform"):
        return True
    else:
        return False


def getParents(generation):
    # get parent nodes of each even individual in a generation
    redundantList =  cmds.listRelatives(generation, p=True)
    return list(set(redundantList))

def getChildren(obj):
    children = cmds.listRelatives(obj,c=True,typ="transform")
    return children

def getFinalGen(root):
    # get the final gen from the root
    def getChildrenRec(obj,finalGen):
        if areLeaves(obj)==True:
            finalGen.append(obj)
            return
        else:
            for child  in getChildren(obj):
                getChildrenRec(child,finalGen)
    finalGen = []
    getChildrenRec(root,finalGen)
    return finalGen

    
