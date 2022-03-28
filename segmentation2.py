from cv2 import cv2
import os
import math


import practicalities as ofs

###
# user inputs:
ofs.getoutfolder()
# IMG_0321,IMG_0323
filename = ofs.getoutfolder()
vidcap = cv2.VideoCapture('in/'+filename)

#check framerate
length = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
print(length/int(1800))
framerate = 10 # IKKE FRAMERATE: skipper n-1 billeder hver gang den gemmer 1.
###

success,image = vidcap.read()

count = 0
while success:
    frameId = vidcap.get(1)
    success,image = vidcap.read()
    # if count == 100: break

    if not os.path.exists("out/"+filename):
        os.mkdir("out/"+filename)

    if (frameId % math.floor(framerate) == 0):    
        cv2.imwrite("out/"+filename+"/frame%d.jpg" % count, image)     # save frame as JPEG file
        print("Segmenting video... Frame%d" % count)
        if cv2.waitKey(10) == 27:                     # exit if Escape is hit
            break
        count += 1
print("Segmentation finished.")
print("Starting image analysis...")


