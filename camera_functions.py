import os
import platform
from time import sleep
if platform.system() != 'Windows':
    from picamera import PiCamera
else:
    import cv2

class Camera:
    def __init__(self):
        self.isRasberryPI = platform.system() == 'Linux'
        if self.isRasberryPI:
            self.camera = PiCamera()
        else:
            self.camera = cv2.VideoCapture(0)

    def capture_rasberrypi(self, save_path, delay_s):
        self.camera.start_preview()
        sleep(delay_s)
        self.camera.capture(save_path)
        self.camera.stop_preview()

    def capture_windows(self, save_path, delay_s):
        if os.path.isfile(save_path):
            os.remove(save_path)
        retval, frame = self.camera.read()
        cv2.imwrite(save_path, frame)
        sleep(delay_s)

    def capture_with_delay(self, save_path, delay_s):
        if self.isRasberryPI:
            self.capture_rasberrypi(save_path, delay_s)
        else:
            self.capture_windows(save_path, delay_s)