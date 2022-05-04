import os

import numpy as np
import matplotlib.pyplot as plt

import practicalities as ofs


outfolder = ofs.getoutfolder()
timespent = ofs.gettime()
os.chdir("/Users/JeffreyPrince/Documents/GitHub/BP/out/"+outfolder)

frame = []
Invalid = []
Done = []


# def runningMeanFast(x, N):
#     return np.convolve(x, np.ones((N,))/N)[(N-1):]


    

file = os.path.join(os.getcwd(),"output.txt")
with open(file,'r') as f:
        for i,l in enumerate(f.readlines()):
            if i > 0: #Skips header
                scale = l.split(";")
                frame.append(float(scale[0]))
                Done.append(float(scale[1]))                
                Invalid.append(float(scale[2]))
                
#########
# Running average:
def moving_average(x, w):
    return np.convolve(x, np.ones(w), 'valid') / w


framearr = np.array(frame)
Invalidarr = np.array(Invalid)
Donearr = np.array(Done)


InvalidMean = moving_average(Invalidarr,24) # 2 sec average
DoneMean = moving_average(Donearr,24) # 2 sec average
#########

timespent = float(timespent)
score = float(600-timespent)

plt.suptitle("Score: "+str(round(score,2)))

plt.subplot(1,2,1).set_ylim([0, 1.1])
plt.plot(DoneMean, '-')
plt.title("Done")
plt.ylabel("Confidence")

plt.subplot(1,2,2).set_ylim([0, 1.1])
plt.plot(InvalidMean, '-')
plt.title("Invalid")
plt.ylabel("Confidence")


plt.show()

# plt.plot(frame,InvalidMean, label = "Invalid")
# plt.plot(frame,DoneMean, label = "Done")
# plt.legend()
# plt.show()




