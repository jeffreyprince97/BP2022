import os

import numpy as np
import matplotlib.pyplot as plt

import practicalities as ofs

outfolder = ofs.getoutfolder()
timespent = ofs.gettime()
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
                                
                # if (float(scale[1]) > float(0.25)):
                Pass.append(float(scale[1]))
                # else:
                #     Pass.append(float(0))
                # if (float(scale[2]) > float(0.25)):
                Fail.append(float(scale[2]))          
                # else:
                #     Fail.append(float(0))                          
                # if (float(scale[3]) > float(0.1)):
                Invalid.append(float(scale[3]))  
                # else:
                #     Invalid.append(float(scale[3])) 
                
                
# Running average:

def moving_average(x, w):
    return np.convolve(x, np.ones(w), 'valid') / w


framearr = np.array(frame)
Invalidarr = np.array(Invalid)
Passarr = np.array(Pass)
Failarr = np.array(Fail)


PassMean = moving_average(Passarr,12) # 2 sec average
FailMean = moving_average(Failarr,12) # 2 sec average
InvalidMean = moving_average(Invalidarr,12) # 2 sec average
#########

timespent = float(timespent)
score = float(600-timespent)

plt.suptitle("Score: "+str(round(score,2)))

plt.subplot(1,3,1).set_ylim([0, 1.1])
plt.plot(PassMean, '-')
plt.title("Pass")
plt.ylabel("Confidence")

plt.subplot(1,3,2).set_ylim([0, 1.1])
plt.plot(FailMean, '-')
plt.title("Fail")
plt.ylabel("Confidence")

plt.subplot(1,3,3).set_ylim([0, 1.1])
plt.plot(InvalidMean, '-')
plt.title("Invalid")
plt.ylabel("Confidence")


plt.show()
                


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

