'''
from picamera import PiCamera
import datetime
import time

class PiCam():
    __camera = PiCamera()
    __imgPath = "/home/pi/image.jpg"
    __camera.resolution = (1024, 768)

    def Snap(self):
        self.__camera.start_preview()
        #Camera warm up time
        time.sleep(2)
        self.__camera.capture(self.__imgPath)
        '''
