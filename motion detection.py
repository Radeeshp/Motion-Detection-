import cv2


first_frame=None
video=cv2.VideoCapture("d:\\EDUCATION\\DEEP LEARNING COURSE\\PROJECTS\\MINI PROJECTS\\Motion detection\\1.mp4")
status=0
while True:
    check,frame=video.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray,(21,21),0)
    
    if first_frame is None:
        first_frame=gray
        continue
    delta_frame=cv2.absdiff(first_frame,gray)
    thresh_frame=cv2.threshold(delta_frame,30,255,cv2.THRESH_BINARY)[1]
    thresh_frame=cv2.dilate(thresh_frame,None,iterations=2)
    (cnts,_)=cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    
    for contours in cnts:
        if cv2.contourArea(contours)< 1000 :
            continue
        status=1
        (x,y,h,w)=cv2.boundingRect(contours)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,55,55),3)
            
    
    cv2.imshow("Gray FRame",gray)
    cv2.imshow("2",delta_frame)
    cv2.imshow("3",thresh_frame)
    cv2.imshow("5",frame)
    key=cv2.waitKey(1)
    if key==ord('q'):
        break
    print(status)
video.release()
cv2.destroyAllWindows