import cv2
import numpy as np 
import matplotlib.pyplot as plt

cap = cv2.VideoCapture("123.mp4")

no_of_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
H = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
W = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
fps = int(cap.get(cv2.CAP_PROP_FPS))
print(no_of_frames)

out = cv2.VideoWriter('output.mp4',cv2.VideoWriter_fourcc(*'XVID'),fps ,(W,H))

frame_index = no_of_frames-1

while(frame_index!=0):
    cap.set(cv2.CAP_PROP_POS_FRAMES , frame_index)
    ret , frame = cap.read() 
    cv2.imshow('win',frame)
    out.write(frame)
   
    
    frame_index=frame_index-1
    if(frame_index%100==0):
        print(frame_index)
    if cv2.waitKey(2)==27:
        break

out.release()
cap.release()
cv2.destroyAllWindows()



    
