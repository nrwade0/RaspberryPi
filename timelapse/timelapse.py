# Import OpenCV to compile timlapse images
import cv2

# Some generic video data
frames = 60
width = 1920
height = 1080


# --------------------------- STEP 1 ------
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
v = cv2.VideoWriter('timelapse.mp4', fourcc, 1, (width, height))

print('Step 1: Build video file            -- completed')


# --------------------------- STEP 2 ------
finalframestr = 'pics/img%03d.jpg' % frames

str = ["pics/img%03d.jpg" % (i+1) for i in range(frames)]
for filename in str:
    print('%s added to video' % filename)
    img = cv2.imread(filename)
    v.write(img)
    
    if(filename == finalframestr):
        break

print('Step 2: Collect and write frames    -- completed')


# --------------------------- STEP 3  ------
v.release()
cv2.destroyAllWindows()
print('Step 3: Send all video data         -- completed')
