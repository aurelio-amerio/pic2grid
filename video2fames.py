import cv2

filepath=""

capture = cv2.VideoCapture(filepath)
 
frameNr = 0
 
while (True):
 
    success, frame = capture.read()
 
    if success:
        cv2.imwrite(f'video_split/frame_{frameNr}.png', frame)
 
    else:
        break
 
    frameNr = frameNr+1
 
capture.release()