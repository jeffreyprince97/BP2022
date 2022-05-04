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
                # Pass.append(float(scale[1]))                
                # Fail.append(float(scale[2]))
                # Invalid.append(float(scale[3]))

                                
                # if (float(scale[1]) > float(0.75)):
                Pass.append(float(scale[1]))
                # else:
                #     Pass.append(float(0))
                # if (float(scale[2]) > float(0.75)):
                Fail.append(float(scale[2]))          
                # else:
                #     Fail.append(float(0))                          
                # if (float(scale[3]) > float(0.1)):
                Invalid.append(float(scale[3]))  
                # else:
                #     Invalid.append(float(scale[3])) 
                
#########
# Running average:
def moving_average(x, w):
    return np.convolve(x, np.ones(w), 'valid') / w

    
framearr = np.array(frame)
Passarr = np.array(Pass)
Failarr = np.array(Fail)
Invalidarr = np.array(Invalid)

PassMean = moving_average(Passarr,12) # 
FailMean = moving_average(Failarr,12) #  
InvalidMean = moving_average(Invalidarr,12) #  
#########

timespent = float(timespent)
score = float(600-timespent)

plt.suptitle("Score: "+str(round(score,2)))
plt.subplot(1,3,1).set_ylim([0, 1.1])
plt.plot(PassMean, '-')
plt.title("pass")
plt.ylabel("Confidence")

plt.subplot(1,3,2).set_ylim([0, 1.1])
plt.plot(FailMean, '-')
plt.title("fail")
plt.ylabel("Confidence")

plt.subplot(1,3,3).set_ylim([0, 1.1])
plt.plot(InvalidMean, '-')
plt.title("invalid")
plt.ylabel("Confidence")

plt.show()



# length1 = len(Pass)
# length2 = len(Fail)
# length3 = len(Invalid)

# plt.plot(length2,Fail, label = "fail")
# plt.plot(length1,Pass, label = "pass")
# plt.plot(length3,Invalid, label = "invalid")
# plt.legend()
# plt.show()

### almindeligt plot:
# plt.plot(frame,Fail, label = "fail")
# plt.plot(frame,Pass, label = "pass")
# plt.plot(frame,Invalid, label = "invalid")
# plt.legend()
# plt.show()


