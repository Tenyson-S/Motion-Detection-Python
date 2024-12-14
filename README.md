Motion Detection System using Python 

It might useful for Baby Sitting, Security Purpose and some other purposes 
Using Open CV Package we create frames and modify, allow to change format

step 1 : Capture Starting frame 
step 2 : Open camera and capture videos
step 3 : change BGR color to Grayscale 
step 4 : apply threshold for grayscale image to black and white image
step 5 : dilate the threshold image because it may have small leftovers of image
step 6 : count the total white pixels in the frame
step 7 : if white_pixels is greater than 1000 :
                play the downloaded sound
step 8 : else:
              the frame would run infinitely
step 9 : press esc key to exit the frame tab
step 10 : destroy all windows created by cv2

