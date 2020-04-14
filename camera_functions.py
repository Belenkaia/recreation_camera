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
            # Throws "Out of resources" exception if initialized more than once
            self.camera = PiCamera()
        else:
            self.camera = cv2.VideoCapture(0)

    def capture_and_save_rasberrypi(self, save_path):
        self.camera.start_preview()
        self.camera.capture(save_path)
        self.camera.stop_preview()

    def capture_and_save_windows(self, save_path):
        retval, frame = self.camera.read()
        cv2.imwrite(save_path, frame)

    def capture_and_save(self, save_path):
        if self.isRasberryPI:
            self.capture_and_save_rasberrypi(save_path)
        else:
            self.capture_and_save_windows(save_path)
