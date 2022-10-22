# import the necessary packages
import numpy as np
import cv2
 
# initialize the HOG descriptor/person detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())



# open webcam video stream


def detect_person(frame):
    
    # using a greyscale picture, also for faster detection
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    # detect people in the image
    # returns the bounding boxes for the detected objects
    boxes, weights = hog.detectMultiScale(frame, winStride=(8,8) )

    boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])
    return boxes

def start_video():
    cv2.startWindowThread()
    cap = cv2.VideoCapture(0)
    boxes = []
    i = 0
    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # resizing for faster detection
        frame = cv2.resize(frame, (640, 480))
        if i == 3:
            boxes = detect_person(frame)
            cv2.imshow('frame',frame)
            for (xA, yA, xB, yB) in boxes:
                cv2.rectangle(frame, (xA, yA), (xB, yB), (0, 255, 0), 2)
            i = 0
        else:
            i += 1
            
        if len(boxes) > 0:
            break

    cv2.destroyAllWindows()
    cap.release()
