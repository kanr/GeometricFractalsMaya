# Geometric Fractals In Maya
## take a base object and make copies of it, link translation, rotation and scale (Transform)

### Based on blender array modifiers

#### Branching Arrays
1. Run nBranches.py in Maya python script editor (Windows -> General Editors -> Script Editor) to load the commands for making a tree with nBranches at each node.
2. Next type  ```makeArray()``` in the Python Command line (defautl is MEL). ```makeArray()``` with no inputs will make a cube-base object and a binary tree structure seven levels deep. 
3. If an object is selected before running makeArray, that object will be the base-object. 
4. Optional inputs are the number of branches and the depth of the tree. With the base object selected, running the prune() command will remove the last generation. 
5. To grow the tree run grow(nBranch=N) where N is the number of children at each node that you would like.

The makeArray will make many copies of the base-object in the same place. To "see" the structure, select a child node of the root node in the Outliner (Window -> Outliner), then try scaling, translating and rotating these children nodes. 

#### Linear Arrays (Spirals)
Run linearArray.py in Maya python script editor. Then type ```makeArray()``` in to python command line in Maya. Play with position, rotation and scale of child of root node (pCube1). To view nodes look at Window -> Outliner.


