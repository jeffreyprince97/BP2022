
import subprocess
import os

import practicalities as ofs

# segment small part of video for task recognition.
subprocess.call(['python','segmentation1.py'])
os.chdir(os.path.join(os.getcwd()+"/taskdetection/example/"))
# analysis + write output
subprocess.call(['python','imageanalysis.py'])
# read output + settask()
subprocess.call(['python','taskpredicter.py'])

os.chdir("..")
os.chdir("..")

task = ofs.gettask()
#segment entire video.
if(task == "Skum"):
    subprocess.call(['python','segmentationskum.py'])
elif(task == "Cirkel"):
    subprocess.call(['python','segmentationcirkel.py'])
elif(task == "Vat"):
    subprocess.call(['python','segmentationvat.py'])
else:
    subprocess.call(['python','segmentation2.py'])

#making sure the correct model is being applied.

os.chdir(os.getcwd()+os.sep+task+"/example/")


subprocess.call(['python3','taskevaluation.py'])
subprocess.call(['python','plot.py'])

