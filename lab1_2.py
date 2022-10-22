import cv2

model = cv2.dnn.readNetFromTensorflow(
        '/home/travvy/Desktop/frozen_inference_graph.pb',
        '/home/travvy/Desktop/ssd_mobilenet_v2_coco_2018_03_29.pbtxt')

frame = cv2.imread('img.jpg')

rows = frame.shape[0]
cols = frame.shape[1]
model.setInput(cv2.dnn.blobFromImage(frame, size=(300, 300), swapRB=True))
output = model.forward()
for detection in output[0,0,:,:]:
    score = float(detection[2])
    if score > 0.3:
        left = detection[3] * cols
        top = detection[4] * rows
        right = detection[5] * cols
        bottom = detection[6] * rows
        cv2.rectangle(frame, (int(left), int(top)), (int(right), int(bottom)), (23, 230, 210), thickness=2)

cv2.imwrite('/home/travvy/Desktop/img_1.jpg', frame)
    
        
