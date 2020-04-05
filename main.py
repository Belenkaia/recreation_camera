from detection_functions import capture_and_recognize
from network_cam import post_data
from tornado.ioloop import IOLoop, PeriodicCallback
import tornado.web
import time
from constants import const


class ImageHandler(tornado.web.RequestHandler):
    def get(self):
        with open(const.current_frame_path, 'rb') as f:
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


async def loop_job():
    await capture_and_recognize()
    # await post_data(people_count, const.device_type, const.zone_id)
    time.sleep(2)
    await loop_job()


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    IOLoop.current().spawn_callback(loop_job)
    IOLoop.current().start()
