# import socket
#
# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
#
# sock.bind((UDP_IP, UDP_PORT))


import numpy as np
import socket
from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
import time
import sys
from threading import *

SEND_TO = '192.168.1.178'

width = 320
height = 180

#	initialize	the	camera	and	grab	a	reference	to	the	raw	camera	capture
camera = PiCamera()
camera.vflip = True
camera.hflip = True
# camera.brightness	=	60
camera.resolution = (width, height)
camera.framerate = 10
rawCapture = PiRGBArray(camera, size=(width, height))
#	allow	the	camera	to	warmup
time.sleep(0.1)

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

class videoprocess(Thread):
    """Thread chargé simplement d'afficher une lettre dans la console."""

    def __init__(self, fps, id, ipclient, portclient):
        Thread.__init__(self)
        self.image = np.zeros((20, 20, 3), np.uint8)
        self.fps = fps
        self.id = id
        self.ipclient = ipclient
        self.portclient = portclient
        self.end = 0
        self.starttime = 0
        print('thread=live at fps=' + str(fps))


    def setimage(self, image):
        self.image = image

    def run(self):
        """Code à exécuter pendant l'exécution du thread."""
        print('run thread=' + str(self.id))  # ne pas décommenter cette ligne
        attente = 1 / float(self.fps)
        while(True):
            self.end = time.time()
            realfps = 1/(self.end - self.starttime)
            print(str(self.id) +' : ' +str(realfps))
            result, imgencode = cv2.imencode('.jpg', self.image, [cv2.IMWRITE_JPEG_QUALITY, 50])
            # cv2.putText(self.image, "%dfps=%s" % (self.id,realfps), (10, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))

            server.sendto(imgencode, (self.ipclient, self.portclient))
            time.sleep(attente)
            self.starttime = self.end


list_thread = []

num_thread = int(sys.argv[1])
set_fps = sys.argv[2].split(',')

for i in range(0,num_thread):
    thread = videoprocess( int(set_fps[i]), i, SEND_TO, 5000 + i)
    list_thread.append(thread)

for t in list_thread:
    t.start()

# thread_2 = videoprocess( 20, 2, SEND_TO, 5004)
# thread_3 = videoprocess( 40, 3, SEND_TO, 5005)
#
# thread_1.start()
# thread_2.start()
# thread_3.start()

print('now starting to send frames...')
#	capture	frames	from	the	camera
for frame in camera.capture_continuous(rawCapture, format="bgr",
                                       use_video_port=True):


    image = frame.array
    image.flags.writeable = True
    rawCapture.truncate(0)

    for t in list_thread:
        t.setimage(image)

camera.close()
server.close()
for t in list_thread:
    t.join()
cv2.destroyAllWindows()
