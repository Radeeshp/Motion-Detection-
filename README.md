# Motion-Detection
To detect motion in a camera feed or video/recording
##Theory/Working:
This project is to detect motion in camera feed or video recording .
It detects motion by storing a frame where there is no motion or the intial frame say i_frame ,and it takes the current frame say cur_frame(from the camera feed or recording) now it compares the i_frame and cur_frame for difference and when the difference of a set of pixels is higher than the threshold it considers it to be motion and marks it with a rectangle.
##Applications:
Motion detection can be used in various feilds.Its used in Intruder alarms,Automatic ticket gates,Entry way lighting,Security lighting,Automated sinks/toilet flusher,Hand dryers,Automatic doors
##Imports Used:
import cv2
##Functions Used:
cv2.VideoCapture
video.read()
cv2.cvtColor
cv2.GaussianBlur
cv2.absdiff
cv2.threshold
cv2.findContours
cv2.contourArea
cv2.boundingRect
cv2.imshow
video.release()
cv2.waitKey(1)
##Algorithm:
##
