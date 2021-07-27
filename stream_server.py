import threading
from flask import Flask, render_template, Response
import receiver

app = Flask(__name__)


def fetch_frame():
    while True:
        frame = receiver.get()
        if frame is None:
            continue
        # with open("stream.jpg", 'wb') as writer:
        #     writer.write(frame)
        yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    #Video streaming route. Put this in the src attribute of an img tag
    return Response(fetch_frame(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


def run_cam_server():
    app.run(debug=True, host="0.0.0.0", port=80)    