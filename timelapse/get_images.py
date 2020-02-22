# import necessary libraries
import time
import picamera
from datetime import datetime

"""
Test No. 1 on the morning of 05/07/2019, sunrise at 6:09am
Duration = .1 hrs = 60/10=6 mins = 360 seconds
Time interval = 6 mins = 360 seconds
Frames = 360/360 = 360 frames/min
"""

# initialize some variables
frames = 60
interval = 1 # seconds
finalframestr = 'pics/img%03d.jpg' % frames


# Take pictures
with picamera.PiCamera() as camera:
    camera.start_preview()
    time.sleep(5) # 5 second warm up
    for filename in camera.capture_continuous('pics/img{counter:03d}.jpg'):
        now = datetime.now()
        print('captured %s on %s' % (filename, str(now)))
        time.sleep(interval)
        if(filename == finalframestr):
            break
    
    camera.stop_preview()

# output ending time
now = datetime.now()
print("Finished: %s" % str(now))
