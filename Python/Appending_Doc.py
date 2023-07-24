#declare paths with double slashes
file = "E:\\Houdini\\Programming\\Creating_Tools\\newdoc.txt"

#attempts to create specified document in the event that it doesn't exist
#if it does, it writes into it

try:
    doc = open(file, "x")
except:
    doc = open(file, "a")
doc.write("Changing Document..." + """
""")
#need this when changing docs
doc.close()