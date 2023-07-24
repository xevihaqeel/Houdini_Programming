import os

file = "E:\\Houdini\\Programming\\Creating_Tools\\readme.txt"
#checks to see if path exists | Returns True/False
test = os.path.exists(file)
print(test)

if test == True:
    os.remove(file)