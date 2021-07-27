from collections import deque
from enum import Flag
from os import read
from threading import Thread
import cv2 as cv

from net import connection

frames = deque()

def get():
    if (len(frames)>0):
        return frames.popleft()
    else:
        return None

def save(frame):
    # import cv2 as cv
    # with open("rec.jpg", 'wb') as writer:
    #     writer.write(frame)
    frames.append(frame)

def init(con : connection):
    def loop(con : connection):
        while True:
            frame = con.recv(decode=False)
            save(frame)
    Thread(target=loop, args=(con,), daemon=False).start()

