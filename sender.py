from os import write
import cv2 as cv
from threading import Thread

from net import connection
from cam_record import get_frame

camera_id = 1

def encode_frame(frame):
    cv.imwrite("frame.jpg", frame)
    ret, buffer = cv.imencode('.jpg', frame)
    frame = buffer.tobytes()
    # with open("enc_frame.jpg", "wb") as writer:
    #     writer.write(frame)
    return frame

def init(con : connection):
    def loop(con : connection):
        for frame in get_frame(camera_id):
            data = encode_frame(frame)
            con.send(data, encode=False)
    Thread(target=loop, args=(con,), daemon=False).start()
