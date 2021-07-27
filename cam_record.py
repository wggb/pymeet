import cv2 as cv

def get_frame(cam_id = 0):
    ''' returns next camera frame '''
    camera = cv.VideoCapture(cam_id)
    while True:
        success, frame = camera.read()  # read the camera frame
        if not success: break
        
        for _ in range(3):
            frame = cv.pyrDown(frame)
        yield frame