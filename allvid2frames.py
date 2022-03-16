from cv2 import cv2
import os
import math

###
# user inputs:
framerate = 10
wd = '/Users/JeffreyPrince/Documents/GitHub/BP/'
###
infolder = "in/perler/"

for wd, dirs, files in os.walk(infolder, topdown=True):
    for d in files: # names in procedures
        if d.endswith('.MOV'):
            
            filename = d
            vidcap = cv2.VideoCapture(infolder+filename)
            success,image = vidcap.read()

            count = 0
            while success:
                frameId = vidcap.get(1)
                success,image = vidcap.read()

                if not os.path.exists("out/"+filename):
                    os.mkdir("out/"+filename)

                if (frameId % math.floor(framerate) == 0):    
                    cv2.imwrite("out/"+filename+"/frame%d.jpg" % count, image)     # save frame as JPEG file
                    if cv2.waitKey(10) == 27:                     # exit if Escape is hit
                        break
                    count += 1
        
        else:
            pass

