
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'MJPG')

fps = cap.get(cv2.CAP_PROP_FPS)
H = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
W = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))


out = cv2.VideoWriter('output.mp4', fourcc, fps, (W, H))

while(True):

	ret, frame = cap.read()

	
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	
	out.write(gray)
	
	cv2.imshow('Original', frame)

	cv2.imshow('frame', gray)

	if cv2.waitKey(1) & 0xFF == ord('a'):
		break

cap.release()

cv2.destroyAllWindows()
