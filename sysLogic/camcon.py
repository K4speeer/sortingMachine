from picamera2 import Picamera2
import time


cam = Picamera2()

cam.start()
time.sleep(1)
cam.capture_file('test.jpg')

cam.close()
