from detection_functions import recognize_frame
from camera_functions import Camera
from network_cam import post_data
from tornado.ioloop import IOLoop
import tornado.web
import time
from constants import const


class ImageHandler(tornado.web.RequestHandler):
    def get(self):
        with open(const.detected_frame_path, 'rb') as f:
            data = f.read()
            self.write(data)
        self.finish()


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("templates/frame_template.html")


def make_app():
    return tornado.web.Application([
        (r'/', MainHandler),
        (r'/frame', ImageHandler)
    ])


def detection_job(cameraManager):
    cameraManager.capture_and_save(const.current_frame_path)
    people_count = recognize_frame()
    post_data(people_count, const.device_type, const.zone_id)
    time.sleep(1)
    detection_job(cameraManager)


if __name__ == "__main__":
    app = make_app()
    app.listen(5050)
    cameraManager = Camera()
    IOLoop.current().run_in_executor(None, detection_job, cameraManager)
    IOLoop.current().start()
