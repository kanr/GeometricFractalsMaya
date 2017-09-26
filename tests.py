import maya.cmds as cmds
"""
Josh Lopez-Binder May 2015
Make a geometric branching fractal with "residue"


Connor Aitken September 2017


"""

def tests():
    # This is for debbuging purposes
    cmds.select(all=True)
    cmds.delete()
    gen = makeArray(nBranch=2,nLevels=4)

    print "\nTEST getChildren"
    assert ["pCube2","pCube3"] == getChildren("pCube1")
    for obj in gen:
        assert None  == getChildren(obj)
    print "passed getChildren!\n"

    # TEST areLeaves
    print "TEST areLeaves"
    print cmds.listRelatives(gen,c=True, typ="transform")
    assert areLeaves(gen)==True
    assert areLeaves("pCube1")==False
    assert areLeaves("pCube2")==False
    print "passed areLeaves test\n"

    print "TEST getGrandParent"
    assert [u'pCube1']== getGrandParent("pCube4")
    assert getGrandParent("pCube7")== getGrandParent("pCube6")
    print getGrandParent("pCube2")
    print "Passed getGrandParent Test!\n"

    print "TEST getParentGen"
    assert [u'pCube4',u'pCube5']== getParentGen("pCube6")
    print cmds.listRelatives("pCube2",typ="transform",c=True)
    print "Passed getParentGen Test!\n"

    print "TEST prune"
    print "Initial leaf  generation: ",
    print gen
    print "Leaf generation after prune:",
    gen = prune(gen)
    print gen
    print "Finished prune display\n"

    print "TEST grow"
    print "Grown Leafs: ",
    gen = grow(gen,2)
    print gen
    print "Finished grow display\n"

    print "TEST getFinalGen"
    assert True == areLeaves("pCube18")
    assert False== areLeaves("pCube1")
    assert set(getFinalGen("pCube2")) == set([u'pCube16',u'pCube17',u'pCube18',u'pCube19'])
    assert set(getFinalGen("pCube1")) == set(gen)
    print "Passed getFinalGen test!\n"
