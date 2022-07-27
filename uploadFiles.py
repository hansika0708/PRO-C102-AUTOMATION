import cv2
from cv2 import VideoCapture
import dropbox
import time 
import random 
start_time = time.time()
def take_snapshot():
    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame = videoCaptureObject.read()
        img_name = "img"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        result = False
    return img_name 
    print("Snapshot taken!!!")
    videoCaptureObject.release()
    cv2.destroyAllWindows()
def upload_file(img_name):
    access_token = 'sl.BML47m_EVAdrG5qU2b6NoZshCYF1IdJ9p0r6RuKDyT4F4ml5c5BOJDCyRC4bnXK8mLu_vCdFbjMpR35c-wGgifGgzldOmwzrMJBOKSeseP_1RJ5P61G8-gYFVHKR9rEClLgsjeA'
    file = img_name
    file_from = file 
    file_to = "/NewFolder1/"+img_name 
    dbx= dropbox.Dropbox(access_token)
    with open (file_from , "rb") as f:
        dbx.files_upload(f.read(),file_to,mode = dropbox.files.WriteMode.overwrite)
        print("file uploaded!!!")
def main():
    while(True):
        if((time.time()-start_time)>= 3):
            name = take_snapshot()
            upload_file(name)
main()
