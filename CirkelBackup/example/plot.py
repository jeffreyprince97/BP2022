import os

import numpy as np
import matplotlib.pyplot as plt

import practicalities as ofs

outfolder = ofs.getoutfolder()
os.chdir("/Users/JeffreyPrince/Documents/GitHub/BP/out/"+outfolder)

frame = []
Fail = []
Pass = []



## BAR PLOT:
file = os.path.join(os.getcwd(),"comments.txt")
with open(file,'r') as f:
        for i,l in enumerate(f.readlines()):
            if i > 0: #Skips header
                scale = l.split(";")
                frame.append(float(scale[0]))
                Pass.append(float(scale[1]))                
                Fail.append(float(scale[2]))
                
                


plt.plot(frame,Fail, label = "fail")
plt.plot(frame,Pass, label = "pass")
plt.legend()
plt.show()


plt.subplot(1,2,1).set_ylim([0, 1.1])
plt.plot(Pass, 'o')
plt.title("pass")
plt.ylabel("Confidence")

plt.subplot(1,2,2).set_ylim([0, 1.1])
plt.plot(Fail, 'o')
plt.title("fail")
plt.ylabel("Confidence")


plt.show()

