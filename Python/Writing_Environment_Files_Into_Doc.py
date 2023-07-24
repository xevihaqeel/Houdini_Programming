import os

#environ is a dictionary, so you need to loop through it
mycontent = os.environ

#declare paths with double slashes
file = "E:\\Houdini\\Programming\\Creating_Tools\\newdoc.txt"

#attempts to create specified document in the event that it doesn't exist
#if it does, it writes into it

try:
    doc = open(file, "x")
except:
    doc = open(file, "w")

for key, path in mycontent.items():
    myline = key  + ": " + path
    doc.write(myline + """
""")

doc.close()
doc = open(file, "r")
for x in doc:
    print(x)