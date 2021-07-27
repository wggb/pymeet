import os
from re import TEMPLATE
from threading import Thread
import webview


def init_window():
    WIDTH = 1000
    HEIGHT = 1000
    BASE_DIR = os.path.dirname(os.path.realpath(__file__))
    TEMPLATE = 'index.html'
    url = os.path.join(BASE_DIR, "templates/"+TEMPLATE)
    api = None
    win = None

    win = webview.create_window(
        "webview",
        url="http://localhost/",
        js_api=api,
        frameless=True,
        width=WIDTH,
        height=HEIGHT,
        resizable=False,
        transparent=True,
        on_top=True
    )

    if os.name == "nt":
        win.frameless = False

    webview.start(debug=True)
