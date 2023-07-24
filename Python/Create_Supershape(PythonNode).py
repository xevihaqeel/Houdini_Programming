import math
import random

node = hou.pwd()
geo = node.geometry()

def supershape(theta,a,b,m, n1, n2, n3):
    theta = theta
    a = a
    b = b
    m = m
    n1 = n1
    n2 = n2
    n3 = n3

    t1 = abs((1/a)*math.cos(m * theta/4))
    t1 = math.pow(t1,n2)

    t2 = abs(1/b * math.sin(m * theta/4))
    t2 = math.pow(t2,n3)
    t3 = t1 + t2
    r = math.pow(t3, -1/n1)


    return r

r = hou.parm('../python1/r').eval()
a = hou.parm('../python1/a').eval()
b = hou.parm('../python1/b').eval()
m = hou.parm('../python1/m').eval()
n1 = hou.parm('../python1/n1').eval()
n2 = hou.parm('../python1/n2').eval()
n3 = hou.parm('../python1/n3').eval()
total = 100

for i in range(total+1):
        if(i < total):
            i+=1 
            lat = hou.hmath.fit(i,0,total,-(math.pi/2),(math.pi/2))
            r2 = supershape(lat,a,b,m,n1,n2,n3)
            for j in range(total):
                if(j < total +1):
                    j+=1
                    lon = hou.hmath.fit(j,0,total,-math.pi,math.pi)
                    r1 = supershape(lon,a,b,m,n1,n2,n3)
                    x = r * r1 * math.cos(lon) * r2 * math.cos(lat)
                    y = r * r1 *  math.sin(lon)* r2 * math.cos(lat)
                    z = r * r2 * math.sin(lat)
                    position = (x,y,z)
                    point = geo.createPoint()
                    point.setPosition(position)

    
                    
              
