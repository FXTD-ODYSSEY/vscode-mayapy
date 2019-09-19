from maya import cmds
from maya import OpenMaya

import pymel.core as pm

circle = pm.circle()[0].getShape()

for cv in circle.cv:
    pos = cv.getPosition(space="world")
    loc = pm.spaceLocator(p=pos)
    pm.refresh()
    print(loc,pos)

pm.delete(circle)


