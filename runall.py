
import subprocess
import os

import practicalities as ofs

# segment small part of video for task recognition.
subprocess.call(['python','segmentation1.py'])
os.chdir(os.path.join(os.getcwd()+"/tf2/example/"))
subprocess.call(['python','typegenkendelse.py'])
subprocess.call(['python','plot.py'])

os.chdir("..")
os.chdir("..")

#segment entire video.
subprocess.call(['python','vid2frames.py'])

#making sure the correct model is being applied.
task = ofs.gettask()
os.chdir(os.getcwd()+os.sep+task+"/example/")


subprocess.call(['python3','taskevaluation.py'])
subprocess.call(['python','plot.py'])

