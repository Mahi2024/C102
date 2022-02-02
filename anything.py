import cv2

def take_snapshot():
    videoObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videoObject.read()
        cv2.imwrite("NewPicture1.jpg",frame)
        result=False
    videoObject.release()
    cv2.destroyAllWindows()
take_snapshot()