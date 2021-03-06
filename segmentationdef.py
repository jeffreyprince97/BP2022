from cv2 import cv2
import os
import math


import practicalities as ofs

# user inputs:
def seg1(f):
    ofs.setoutfolder(f)
    filename = ofs.getoutfolder()
    vidcap = cv2.VideoCapture(f)

    fps = int(vidcap.get(cv2.CAP_PROP_FPS))
    length = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
    time = str(length/fps)
    ofs.settime(time)

    framerate = 10
    ###

    success,image = vidcap.read()

    count = 1
    while success:
        if count == 26:
            break
        frameId = vidcap.get(1)
        success,image = vidcap.read()

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


