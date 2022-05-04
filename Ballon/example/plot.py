import os

import numpy as np
import matplotlib.pyplot as plt

import practicalities as ofs

outfolder = ofs.getoutfolder()
timespent = ofs.gettime()
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
                

#########
# Running average:
def moving_average(x, w):
    return np.convolve(x, np.ones(w), 'valid') / w

    
framearr = np.array(frame)
Passarr = np.array(Pass)
Failarr = np.array(Fail)

PassMean = moving_average(Passarr,12) # 2 sec average
FailMean = moving_average(Failarr,12) # 2 sec average
#########              


# plt.plot(frame,Fail, label = "fail")
# plt.plot(frame,Pass, label = "pass")
# plt.legend()
# plt.show()

timespent = float(timespent)
score = float(600-timespent)

plt.suptitle("Score: "+str(round(score,2)))


plt.subplot(1,2,1).set_ylim([0, 1.1])
plt.plot(PassMean, '-')
plt.title("pass")
plt.ylabel("Confidence")

plt.subplot(1,2,2).set_ylim([0, 1.1])
plt.plot(FailMean, '-')
plt.title("fail")
plt.ylabel("Confidence")


plt.show()

