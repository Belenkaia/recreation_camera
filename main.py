from detection_functions import capture_and_recognize
from network_cam import post_data
from tornado.ioloop import IOLoop, PeriodicCallback
import tornado.web
import time
import threading
from constants import const


class ImageHandler(tornado.web.RequestHandler):
    def get(self):
        with open(const.detected_frame_path, 'rb') as f:
            data = f.read()
            self.write(data)
        self.finish()

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(r'<img src="/frame">')


def make_app():
    return tornado.web.Application([
        (r'/', MainHandler),
        (r'/frame', ImageHandler)
    ])


def loop_job():
    people_count = capture_and_recognize()
    post_data(people_count, const.device_type, const.zone_id)
    time.sleep(1)
    loop_job()


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    x = threading.Thread(target=loop_job)
    x.start()
    IOLoop.current().start()
