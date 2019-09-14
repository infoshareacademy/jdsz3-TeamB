import cv2 as cv
import time
from imutils.video import FPS
import urllib
import numpy as np

# Load the model.
net = cv.dnn.readNet('face-detection-adas-0001.xml',
                     'face-detection-adas-0001.bin')
# Specify target device.
#net.setPreferableTarget(cv.dnn.DNN_TARGET_MYRIAD)
# Read an image.
#camera = cv.VideoCapture(0)
#camera.resolution = (640, 480)
#camera.framerate = 16
#rawCapture = cv.PiRGBArray(camera, size=(640, 480))

#time.sleep(0.1)
fps = FPS().start()

while True:
    imgResp = urllib.request.urlopen('http://10.58.74.150:8080/shot.jpg')
    imgNp = np.array(bytearray(imgResp.read()), dtype=np.uint8)
    camera = cv.imdecode(imgNp, -1)
    image = camera
    #ret, image = camera.read()
#    image = frame.array
    
# frame = cv.imread('/home/pi/Pictures/street_and_person.jpg')
# if frame is None:
#     raise Exception('Image not found!')

# Prepare input blob and perform an inference.
    blob = cv.dnn.blobFromImage(image, ddepth=cv.CV_8U)
    net.setInput(blob)
    out = net.forward()
    #print(out.shape)
# Draw detected faces on the frame.
    for detection in out.reshape(-1, 7):
        #print(detection)
        confidence = float(detection[2])
        xmin = int(detection[3] * image.shape[1])
        ymin = int(detection[4] * image.shape[0])
        xmax = int(detection[5] * image.shape[1])
        ymax = int(detection[6] * image.shape[0])
        if confidence > 0.5:
            #print(confidence)
            cv.rectangle(image, (xmin, ymin), (xmax, ymax), color=(0, 255, 0))
            cv.putText(image, str(confidence), (xmin, ymin), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0))
    cv.imshow("Frame", image)
    key = cv.waitKey(1) & 0xFF
    #rawCapture.truncate(0)
    fps.update()
            
    if key == ord("q"):
        break
        
fps.stop()
print('FPS:', fps.fps())
# Save the frame to an image file.
# cv.imwrite('out.png', frame)
