import cv2
import numpy as np
from playsound import playsound

cam = cv2.VideoCapture(0)

ret, first_frame = cam.read() #ret - True or False (camera access or not)

first_frame = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)
first_frame = cv2.GaussianBlur(first_frame, (21,21), 0)

while True:
    ret, frame = cam.read()
    if not ret:
        break

    # convert the frame to grayscale and apply Gaussian Blur
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame = cv2.GaussianBlur(gray_frame, (21,21), 0)
    
    #Compute the absolute diifference between the current frame and first frame
    delta_frame = cv2.absdiff(first_frame, gray_frame)

    #Threshold the delta image to identify regions with significant change
    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]

    #Dilate the thresholded image to fill in gaps
    thresh_frame = cv2.dilate(thresh_frame, None, iterations = 2)

    #calculate no. of white pixels in threshold frame
    white_pixel_count = np.sum(thresh_frame==255)

    #Trigger an Alert if motion is detected
    if white_pixel_count > 1000: #Adjust the threshold based on your environment
        playsound('alert.mp3')

    cv2.imshow("Motion Detection",frame)

    #Press ESC to quit the program
    if cv2.waitKey(1) == 27: #27 is ASCII code for ESC
        break

cam.release()
cv2.destroyAllWindows()
