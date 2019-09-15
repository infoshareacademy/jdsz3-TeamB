import cv2 as cv
import time
from imutils.video import FPS
import urllib
import numpy as np
import time
import statistics

cv.setUseOptimized(onoff=True)

fpsList = []

# Measure elapsed time
s = time.time()

# Load the model.
net = cv.dnn.readNet('face-detection-adas-0001.xml',
                     'face-detection-adas-0001.bin')

# Get IP adress of camera
ipAdress = str(input('Wprowadź adres IP kamery: '))

# Count FPS
fps = FPS().start()

while True:
    try:
        # Read an image.
        imgResp = urllib.request.urlopen('http://'+ipAdress+':8080/shot.jpg')
        imgNp = np.array(bytearray(imgResp.read()), dtype=np.uint8)
        image = cv.imdecode(imgNp, -1)
    except:
        print('Connection lost...')
        break

# Prepare input blob and perform an inference.
    blob = cv.dnn.blobFromImage(image, ddepth=cv.CV_8U)
    net.setInput(blob)
    out = net.forward()

# Draw detected faces on the frame.
    for detection in out.reshape(-1, 7):
        confidence = float(detection[2])
        xmin = int(detection[3] * image.shape[1])
        ymin = int(detection[4] * image.shape[0])
        xmax = int(detection[5] * image.shape[1])
        ymax = int(detection[6] * image.shape[0])
        if confidence > 0.5:
            percentage = str(int(confidence*100))
            cv.rectangle(image, (xmin, ymin), (xmax, ymax), color=(0, 255, 0), thickness=2)
            cv.putText(image, percentage, (xmin, (ymin - 5)), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            if len(percentage) == 2:
                cv.putText(image, '%', ((xmin + 40), (ymin - 5)), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            elif len(percentage) == 3:
                cv.putText(image, '%', ((xmin + 60), (ymin - 5)), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    fps.update()
    fps.stop()
    fpsList.append(round(fps.fps(), 2))
    fpsShow = str(round(fps.fps(), 2))
    cv.putText(image, fpsShow, (520, 25), cv.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0))
    cv.putText(image, 'FPS', (590, 25), cv.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0))
    cv.putText(image, '''Press 'Q' to exit...''', (10, 470), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0))
    cv.imshow('Frame', image)
    key = cv.waitKey(1) & 0xFF

    if key == ord("q"):
        break

print('[INFO]', round(statistics.mean(fpsList), 2), 'average FPS')
print('[INFO]', int(time.time() - s), 'seconds elapsed')
