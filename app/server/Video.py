from collections import deque

import cv2
import argparse
import sys, os

from app.client.pyqt5.OL_3D_Plot import OL_3D_Plot

class Video:
    def __init__(self, id):
        try:

            # INITIALIZE DATA STRUCTURES FOR VIDEO
            self.id = id
            ap = argparse.ArgumentParser()
            ap.add_argument("-b", "--buffer", type=int, default=128, help="max buffer size")
            self.args = vars(ap.parse_args())
            self.frame = None
            self.counter = 0
            self.newDeque = deque(maxlen=self.args["buffer"])
            self.red =    {'x': [], 'y': [], 'z': [], 'text': []}
            self.green =  {'x': [], 'y': [], 'z': [], 'text': []}
            self.blue =   {'x': [], 'y': [], 'z': [], 'text': []}
            self.yellow = {'x': [], 'y': [], 'z': [], 'text': []}

            self.red_xyz_pts =    {'x': None, 'y': None, 'z': None, 'pts': self.newDeque, 'text': None}
            self.green_xyz_pts =  {'x': None, 'y': None, 'z': None, 'pts': self.newDeque, 'text': None}
            self.blue_xyz_pts =   {'x': None, 'y': None, 'z': None, 'pts': self.newDeque, 'text': None}
            self.yellow_xyz_pts = {'x': None, 'y': None, 'z': None, 'pts': self.newDeque, 'text': None}

            self.isDetected = {"red": False, "green": False, "blue": False, "yellow": False}
            #self.time =

            print("Creating v" + self.id + " ... defined data structures")

            # 3D PLOTS FOR THIS VIDEO
            self.plot = OL_3D_Plot(self)


        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            print (e)
    def setVidSource(self, vidSource):
        if (vidSource == '0' or vidSource == '1' or vidSource == '2' or vidSource == '3'):
            self.vidSource = int(vidSource)
        else:
            self.vidSource = vidSource

        self.vidCap = cv2.VideoCapture(self.vidSource)
        self.vidCap.set(cv2.CAP_PROP_FRAME_WIDTH, 400)
        self.vidCap.set(cv2.CAP_PROP_FRAME_HEIGHT, 300)

        # Find OpenCV version to set FPS
        (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
        if int(major_ver) < 3:
            self.fps = self.vidCap.get(cv2.cv.CV_CAP_PROP_FPS)
            print("Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(self.fps))
        else:
            self.fps = self.vidCap.get(cv2.CAP_PROP_FPS)
            print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(self.fps))
        print("Creating ... v" + self.id + " made video capture")

    def clear(self, color):
        if(color == "all"):
            print(" Clearing " + self.id + " all")
            self.red = {'x': [], 'y': [], 'z': [], 'text': []}
            self.green = {'x': [], 'y': [], 'z': [], 'text': []}
            self.blue = {'x': [], 'y': [], 'z': [], 'text': []}
            self.yellow = {'x': [], 'y': [], 'z': [], 'text': []}

            self.red_xyz_pts = {'x': None, 'y': None, 'z': None, 'pts': self.newDeque, 'text': None}
            self.green_xyz_pts = {'x': None, 'y': None, 'z': None, 'pts': self.newDeque, 'text': None}
            self.blue_xyz_pts = {'x': None, 'y': None, 'z': None, 'pts': self.newDeque, 'text': None}
            self.yellow_xyz_pts = {'x': None, 'y': None, 'z': None, 'pts': self.newDeque, 'text': None}
            self.counter = 0

        elif(color == "red"):

            print(" Clearing " + self.id + " red")
            self.red = {'x': [], 'y': [], 'z': [], 'text': []}
            self.red_xyz_pts = {'x': None, 'y': None, 'z': None, 'pts': self.newDeque, 'text': None}

        elif (color == "green"):

            print(" Clearing " + self.id + " green")
            self.green = {'x': [], 'y': [], 'z': [], 'text': []}
            self.green_xyz_pts = {'x': None, 'y': None, 'z': None, 'pts': self.newDeque, 'text': None}

        elif (color == "blue"):

            print(" Clearing " + self.id + "blue")
            self.blue = {'x': [], 'y': [], 'z': [], 'text': []}
            self.blue_xyz_pts = {'x': None, 'y': None, 'z': None, 'pts': self.newDeque, 'text': None}

        elif (color == "yellow"):

            print(" Clearing " + self.id + " yellow")
            self.yellow = {'x': [], 'y': [], 'z': [], 'text': []}
            self.yellow_xyz_pts = {'x': None, 'y': None, 'z': None, 'pts': self.newDeque, 'text': None}

        print(" EXITING Clearing " + self.id)
        return