from picamera import PiCamera
import datetime
import time

class Camera():
    def Snap(self, targetPath):
        camera = PiCamera()
        camera.resolution = (1024, 768)
        camera.start_preview()
        #Camera warm up time
        time.sleep(2)
        camera.capture(targetPath)
