import cv2
def camera():
#initialising cv2
    videoCapture1=cv2.videoCapture(0)
    result=True
    while(result):
        #read the frames while camera is on
        ret,frame=videoCapture1.read()
        #cv2.imWrite, used to save an image to any storage device.
        cv2.imWrite("newPicture.jpg",frame)   
        result=False
    #release the camera
    videoCapture1.release()
    cv2.destroyAllWindows()
camera()           

