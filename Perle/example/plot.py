import os

import numpy as np
import matplotlib.pyplot as plt

import practicalities as ofs

outfolder = ofs.getoutfolder()
os.chdir("/Users/JeffreyPrince/Documents/GitHub/BP/out/"+outfolder)

frame = []
InsideDropped = []
NotDropped = []
OutsideDropped = []


## BAR PLOT:
file = os.path.join(os.getcwd(),"comments.txt")
with open(file,'r') as f:
        for i,l in enumerate(f.readlines()):
            if i > 0: #Skips header
                scale = l.split(";")
                frame.append(float(scale[0]))
                InsideDropped.append(float(scale[1]))
                NotDropped.append(float(scale[2]))                
                OutsideDropped.append(float(scale[3])) 

#####
# Running average:


def moving_average(x, w):
    return np.convolve(x, np.ones(w), 'valid') / w

framearr = np.array(frame)
InsideDroppedarr = np.array(InsideDropped)
NotDroppedarr = np.array(NotDropped)
OutsideDroppedarr = np.array(OutsideDropped)


InsideDroppedMean = moving_average(InsideDroppedarr,12) # 4 sec average
NotDroppedMean = moving_average(NotDroppedarr,12) # 4 sec average
OutsideDroppedMean = moving_average(OutsideDroppedarr,12) # 4 sec average

#####

plt.plot(frame,InsideDropped, label = "inside")
plt.plot(frame,NotDropped, label = "not dropped")
plt.plot(frame,OutsideDropped, label = "outside")
plt.legend()
plt.show()

plt.subplot(1,3,1).set_ylim([0, 1.1])
plt.plot(InsideDroppedMean, '-')
plt.title("inside dropped")
plt.ylabel("Confidence")

plt.subplot(1,3,2).set_ylim([0, 1.1])
plt.plot(NotDroppedMean, '-')
plt.title("not dropped")
plt.ylabel("Confidence")

plt.subplot(1,3,3).set_ylim([0, 1.1])
plt.plot(OutsideDroppedMean, '-')
plt.title("outside")
plt.ylabel("Confidence")

plt.show()








###BARPLOT:
# import os

# import numpy as np
# import matplotlib.pyplot as plt

# import practicalities as ofs

# outfolder = ofs.getoutfolder()
# os.chdir("/Users/JeffreyPrince/Documents/GitHub/BP/out/"+outfolder)

# frame = []
# InsideDropped = []
# NotDropped = []
# OutsideDropped = []


# ## BAR PLOT:
# file = os.path.join(os.getcwd(),"comments.txt")
# with open(file,'r') as f:
#         for i,l in enumerate(f.readlines()):
#             if i > 0: #Skips header
#                 scale = l.split(";")
#                 frame.append(float(scale[0]))
                
#                 if (float(scale[1]) > float(0.1)):
#                     InsideDropped.append(float(scale[1]))
#                 if (float(scale[2]) > float(0.1)):
#                     NotDropped.append(float(scale[2]))                
#                 if (float(scale[3]) > float(0.1)):
#                     OutsideDropped.append(float(scale[3]))                 
                                       

# fig = plt.figure()
# # Bar plot:
# number_list = [len(InsideDropped), len(NotDropped), len(OutsideDropped)]
# max_value = max(number_list)
# max_index = number_list.index(max_value)

# ax = fig.add_axes([0,0,1,1])
# langs = ['In', 'Not', 'Out']
# students = [len(InsideDropped),len(NotDropped),len(OutsideDropped)]

# ax.bar(langs,students)
# plt.show()





###BARPLOT:
# import os

# import numpy as np
# import matplotlib.pyplot as plt

# import practicalities as ofs

# outfolder = ofs.getoutfolder()
# os.chdir("/Users/JeffreyPrince/Documents/GitHub/BP/out/"+outfolder)

# frame = []
# Fail = []
# Pass = []
# OutsideDropped = []


# ## BAR PLOT:
# file = os.path.join(os.getcwd(),"comments.txt")
# with open(file,'r') as f:
#         for i,l in enumerate(f.readlines()):
#             if i > 0: #Skips header
#                 scale = l.split(";")
#                 frame.append(float(scale[0]))
                
#                 if (float(scale[1]) > float(0.1)):
#                     Fail.append(float(scale[1]))
#                 if (float(scale[2]) > float(0.1)):
#                     NotDropped.append(float(scale[2]))                
#                 if (float(scale[3]) > float(0.1)):
#                     OutsideDropped.append(float(scale[3]))                 
                                       

# fig = plt.figure()
# # Bar plot:
# number_list = [len(Fail), len(NotDropped), len(OutsideDropped)]
# max_value = max(number_list)
# max_index = number_list.index(max_value)

# ax = fig.add_axes([0,0,1,1])
# langs = ['In', 'Not', 'Out']
# students = [len(Fail),len(NotDropped),len(OutsideDropped)]

# ax.bar(langs,students)
# plt.show()