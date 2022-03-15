import os

myp = "/Users/JeffreyPrince/Documents/GitHub/BP"

def setoutfolder(outfolder):
    with open(myp +os.sep + "outfolder.cames","w") as f:
        f.write(outfolder)

def getoutfolder():
    with open(myp +os.sep + "outfolder.cames","r") as f:
        outfolder = f.readlines()[0]
    return outfolder




