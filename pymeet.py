from threading import Thread

import win
from net import connection
import receiver
import sender
import stream_server

def init():
    receiver.init(con)
    sender.init(con)

if __name__ == "__main__":
    con = connection()
    Thread(target=init, daemon= False).start()
    stream_server.run_cam_server()
    # win.init_window()