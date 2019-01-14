import socket
import numpy as np
import cv2
import sys
import time
UDP_IP = "192.168.1.178"
UDP_PORT  = int(sys.argv[1])
width = 320
height = 180
sock = socket.socket(socket.AF_INET,  # Internet
                     socket.SOCK_DGRAM)  # UDP
sock.bind((UDP_IP, UDP_PORT))
starttime = 0
while True:
    print('try to receive')
    end = time.time()
    realfps = 1 / (end - starttime)
    data, addr = sock.recvfrom(65507)  # buffer size is 1024 bytes
    print('received from '+ str(addr))
    data = np.array(bytearray(data))
    imgdecode = cv2.imdecode(data, 1)
    print('have received one frame')
    cv2.putText(imgdecode, "fps=%s" % (realfps), (10, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
    starttime = end
    cv2.imshow('live1', imgdecode)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
