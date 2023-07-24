import hou

obj = hou.node("/obj")




for x in range(0,6):

    #Create a set of geo nodes containing sphere
    #Set position of the nodes
    geosphere = obj.createNode("geo", "geo_sphere_" + str(x+1))
    sphere = geosphere.createNode("sphere")
    mypos = (x*2,2+x)
    geosphere.setPosition(mypos)
    #geosphere.moveToGoodPosition()
    
    #Set coordinates of the spheres
    mycoord = (x*2,x *0.4, x)
    #geosphere.parm("tx").set(x*2)
    geosphere.parmTuple("t").set(mycoord)
    geosphere.parm("scale").set(x * .3)