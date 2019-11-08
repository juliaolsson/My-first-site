from omxplayer.player import OMXPlayer
from pathlib import Path
import time

path = Path('../movie.mp4')

player = OMXPlayer(path)

time.sleep(5)

player.pause()



#import subprocess
#path = '../movie.mp4'
#omx = subprocess.Popen(['omxplayer', path], stdin=subprocess.PIPE)




