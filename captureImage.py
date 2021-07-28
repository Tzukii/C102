import cv2
import dropbox
import time
import random

start_time = time.time()

def take_snapshot():
    number = random.randint(0,100)
    #initializing cv2
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        #read the frames while the camera is on
        ret,frame = videoCaptureObject.read()
        #cv2.imwrite() method is used to save an image to any storage device
        img_name = "img"+str(number)+".png"
        cv2.imwrite(img_name, frame)
        start_time = time.time
        result = False
    return img_name
    print("snapshot taken")
    # releases the camera
    videoCaptureObject.release()
    #closes all the window that might be opened while this process
    cv2.destroyAllWindows()

def upload_file(img_name):
    access_token ="sl.A1cQLnBXkHWyG-2SjzzPN0yIvBD2VSxNnDBcxyHfI505BbzA6fyok9XgXsXyJKzTng0BOb17uMpRO1k8lc4hfkK93L_hADo73ThfU_VvQyWg5aMO7985inkt6jVd2e5bIASXmGrXmD77"
    file = img_name
    fileFrom = file
    fileTo = "/captureImage_Shivam"+(img_name)
    dbx=dropbox.Dropbox(access_token)

    with open(fileFrom, 'rb') as f:
        dbx.files_upload(f.read(), fileTo,mode=dropbox.files.WriteMode.overwrite)
        print("file uploaded")

    
def main():
    while(True):
        if((time.time()-start_time)>=5):
            name=take_snapshot()
            upload_file(name)


main()
    