import os

import numpy as np
import matplotlib.pyplot as plt

import outfolderscript as ofs

outfolder = ofs.getoutfolder()
os.chdir("/Users/JeffreyPrince/Documents/GitHub/BP/out/"+outfolder)

frame = []
Ballon = []
Cirkel = []
Perle = []
Skum = []
Vat = []


## BAR PLOT:
file = os.path.join(os.getcwd(),"comments.txt")
with open(file,'r') as f:
        for i,l in enumerate(f.readlines()):
            if i > 0: #Skips header
                scale = l.split(";")
                frame.append(float(scale[0]))
                if (float(scale[1]) < float(0.1)):
                    pass
                else: 
                    Ballon.append(float(scale[1]))
                if (float(scale[2]) < float(0.1)):
                    pass
                else: 
                    Cirkel.append(float(scale[2]))                    
                if (float(scale[3]) < float(0.1)):
                    pass
                else: 
                    Perle.append(float(scale[3]))                    
                if (float(scale[4]) < float(0.1)):
                    pass
                else: 
                    Skumballon.append(float(scale[4]))                    
                if (float(scale[5]) < float(0.1)):
                    pass
                else: 
                    Vat.append(float(scale[5]))                    

fig = plt.figure()

# fig.suptitle(outfolder) 
# viser filens navn, men det er ikke så hensigtsmæssigt, 
# hvis den hedder noget med dato og tid fra optagelsestidspunkt.

# Prediction:
number_list = [len(Ballon), len(Cirkel), len(Perle), len(Skumballon), len(Vat)]
max_value = max(number_list)
max_index = number_list.index(max_value)

# kan erstattes med funktioner, der kører specifikke lobe models for øvelserne.
if (max_index == 0):
    fig.suptitle('Prediction: Ballon')
elif (max_index == 1):
    fig.suptitle('Prediction: Cirkel')
elif (max_index == 2):
    fig.suptitle('Prediction: Perle')
elif (max_index == 3):
    fig.suptitle('Prediction: Skumballon')
elif (max_index == 4):
    fig.suptitle('Prediction: Vat')

# plot:
ax = fig.add_axes([0,0,1,1])
langs = ['Ballon', 'Cirkel', 'Perle', 'Skumballon', 'Vat']
students = [len(Ballon),len(Cirkel),len(Perle),len(Skumballon),len(Vat)]

ax.bar(langs,students)
plt.show()




## subplot: 
# file = os.path.join(os.getcwd(),"comments.txt")
# with open(file,'r') as f:
#         for i,l in enumerate(f.readlines()):
#             if i > 0: #Skips header
#                 scale = l.split(";")
#                 frame.append(float(scale[0]))                
#                 Ballon.append(float(scale[1]))
#                 Cirkel.append(float(scale[2]))
#                 Perle.append(float(scale[3]))
#                 Skumballon.append(float(scale[4]))
#                 Vat.append(float(scale[5]))


# plt.subplot(2,3,1).set_ylim([0, 1.1])
# plt.plot(Ballon, 'o')
# plt.title("Ballon")
# plt.ylabel("Confidence")

# plt.subplot(2,3,2).set_ylim([0, 1.1])
# plt.plot(Cirkel, 'o')
# plt.title("Cirkel")
# plt.ylabel("Confidence")

# plt.subplot(2,3,3).set_ylim([0, 1.1])
# plt.plot(Perle, 'o')
# plt.title("Perle")
# plt.ylabel("Confidence")

# plt.subplot(2,3,4).set_ylim([0, 1.1])
# plt.plot(Skumballon, 'o')
# plt.title("Skumballon")
# plt.ylabel("Confidence")

# plt.subplot(2,3,5).set_ylim([0, 1.1])
# plt.plot(Vat, 'o')
# plt.title("Vat")
# plt.ylabel("Confidence")

# plt.show()