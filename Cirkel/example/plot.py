import os

import numpy as np
import matplotlib.pyplot as plt

import practicalities as ofs

outfolder = ofs.getoutfolder()
os.chdir("/Users/JeffreyPrince/Documents/GitHub/BP/out/"+outfolder)

frame = []
Pass = []
Fail = []
Invalid = []



## BAR PLOT:
file = os.path.join(os.getcwd(),"comments.txt")
with open(file,'r') as f:
        for i,l in enumerate(f.readlines()):
            if i > 0: #Skips header
                scale = l.split(";")
                frame.append(float(scale[0]))
                                
                if (float(scale[1]) > float(0.25)):
                    Pass.append(float(scale[1]))
                # else:
                #     Pass.append(float(0))
                if (float(scale[2]) > float(0.25)):
                    Fail.append(float(scale[2]))          
                # else:
                #     Fail.append(float(0))                          
                if (float(scale[3]) > float(0.1)):
                    Invalid.append(float(scale[3]))  
                # else:
                #     Invalid.append(float(scale[3])) 
                
                
                


# plt.plot(frame,Pass, label = "pass")
# plt.plot(frame,Fail, label = "fail")
# plt.plot(frame,Invalid, label = "pass")
# plt.legend()
# plt.show()


plt.subplot(1,3,1).set_ylim([0, 1.1])
plt.plot(Pass, 'o')
plt.title("pass")
plt.ylabel("Confidence")

plt.subplot(1,3,2).set_ylim([0, 1.1])
plt.plot(Fail, 'o')
plt.title("fail")
plt.ylabel("Confidence")

plt.subplot(1,3,3).set_ylim([0, 1.1])
plt.plot(Fail, 'o')
plt.title("invalid")
plt.ylabel("Confidence")


plt.show()

