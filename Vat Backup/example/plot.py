import os

import numpy as np
import matplotlib.pyplot as plt

import practicalities as ofs

outfolder = ofs.getoutfolder()
os.chdir("/Users/JeffreyPrince/Documents/GitHub/BP/out/"+outfolder)

frame = []
Invalid = []
Done = []




file = os.path.join(os.getcwd(),"output.txt")
with open(file,'r') as f:
        for i,l in enumerate(f.readlines()):
            if i > 0: #Skips header
                scale = l.split(";")
                frame.append(float(scale[0]))
                Done.append(float(scale[1]))                
                Invalid.append(float(scale[2]))
                
                


plt.plot(frame,Invalid, label = "Invalid")
plt.plot(frame,Done, label = "Done")
plt.legend()
plt.show()


plt.subplot(1,2,1).set_ylim([0, 1.1])
plt.plot(Done, 'o')
plt.title("Done")
plt.ylabel("Confidence")

plt.subplot(1,2,2).set_ylim([0, 1.1])
plt.plot(Invalid, 'o')
plt.title("Invalid")
plt.ylabel("Confidence")


plt.show()

