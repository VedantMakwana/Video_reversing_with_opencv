# Importing lib
import cv2

# Creating video capture object
video = "123.mp4" #video address
cap = cv2.VideoCapture(video)

# calculating no of frames
no_of_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# Calculating Hieght(H) and Width(W)
H = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
W = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

# Caclulating fps
fps = int(cap.get(cv2.CAP_PROP_FPS))
print(no_of_frames)

# Creating video writer
out = cv2.VideoWriter('output.mp4',cv2.VideoWriter_fourcc(*'XVID'),fps ,(W,H))

frame_index = no_of_frames-1

# while loop until frame_index==0
while(frame_index!=0):
    cap.set(cv2.CAP_PROP_POS_FRAMES , frame_index) #seting postion of strating frame to last frame
    ret , frame = cap.read() #reading frame
    cv2.imshow('win',frame) #display frame
    out.write(frame) #writing frame
    frame_index=frame_index-1 #decrementing value of frame_index
    if(frame_index%100==0): # Displaying Progression
        print(frame_index)
    if cv2.waitKey(2)==27: 
        break

# releasing the resources
out.release()
cap.release()
cv2.destroyAllWindows()



    
