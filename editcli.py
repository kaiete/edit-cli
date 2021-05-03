appname = "App name: {name}"
import random
appname = appname.format(name = "Edit CLI")
print(appname)
openfile = str(input("What is the path of the file? "))
editoropen = str(input("Do you want to add to, overwrite, view the file, create it or corrupt the file? a/o/v/c/cr respectively "))
if editoropen == "v":
    print("Opening file...")
    print("---------------")
    filecontents = open(openfile,"r")
    print(filecontents.read())
elif editoropen == "a":
    print("Opening file for editing...")
    print("---------------------------")
    filecontents = open(openfile,"r")
    print(filecontents.read())
    print("---------------------------")
    linetoadd = str(input("Please enter a line to add to this file... "))
    filecontents = open(openfile,"a")
    filecontents.write("\n" + linetoadd)
    print("Added")
elif editoropen == "o":
    print("Opening file for editing...")
    print("---------------------------")
    filecontents = open(openfile,"r")
    print(filecontents.read())
    print("---------------------------")
    linetoadd = str(input("Please enter a line that will replace the content of this file... "))
    filecontents = open(openfile,"w")
    filecontents.write(linetoadd)
    print("Added")
elif editoropen == "c":
    filenametocreate = openfile
    newfile = open(filenametocreate,"a")
    newfile.write("")
    newfile.close()
    print("Done, file created.\nIf the file already existed, nothing will be changed.")
elif editoropen == "cr":
    if input("Are you ABSOLUTELY SURE? The file's contents will be gone INDEFINITELY! (y/N)") == "y":
        corruptfile = open(openfile,"w")
        y = random.randint(1,100101010147859723578650684086498348645864868543638574867948567094670945678567506730565605638456546757866587540863)
        corruptfile.write(y)
    else:
        print("Nothing has been changed.")
