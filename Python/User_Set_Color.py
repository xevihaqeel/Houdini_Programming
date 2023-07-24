#Allows user to set color of created houdini nodes

import hou
obj = hou.node("/obj")
blue = 0
colorui = hou.ui.selectColor()
print(colorui)
for x in range(0,12):
    geosphere = obj.createNode("geo", "geo_sphere_" + str(x+1))
    mypos = (x*2, 2+x)
    geosphere.setPosition(mypos)
    
    cl = (0.5,0.2,blue)
    geosphere.setColor(colorui)
    blue += 0.1