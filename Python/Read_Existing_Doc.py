#declare paths with double slashes
file = "E:\\Houdini\\Programming\\Creating_Tools\\readme.txt"
doc = open(file, "r")

for x in doc:
    print(x)