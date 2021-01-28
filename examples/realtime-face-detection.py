# -*- coding: utf-8 -*-

from twitchrealtimehandler import TwitchImageGrabber
import time
import face_recognition
import cv2
import numpy as np
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--twitch-url', type=str, help='url of the stream')
    parser.add_argument('--quality', type=str, default="480p", help='quality of the stream')
    parser.add_argument('--fps', type=int, default=5, help='fps')
    opt = parser.parse_args()

    img_grabber = TwitchImageGrabber(twitch_url=opt.twitch_url,
                                     quality=opt.quality,
                                     rate=opt.fps,
                                     blocking=True)
    previous_time = time.time()
    i = 0
    while True:
        img = img_grabber.grab()
        if img is not None:
            t = time.time()
            face_locations = face_recognition.face_locations(img)
            print(f"inference time: {time.time()-t}")

            for face in face_locations:
                # Extract the ROI of the face from the grayscale image, resize it to a fixed 28x28 pixels, and then prepare
                # the ROI for classification via the CNN
                top, right, bottom, left = face
                img = cv2.rectangle(img,
                                    (left, top),
                                    (right, bottom),
                                    (0, 0, 255), 2)
            cv2.imshow("frame", img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            print(time.time()-previous_time)
            previous_time = time.time()
            cv2.imwrite("imgs/img{}.jpg".format(str(i).zfill(5)), cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
            i += 1
    cv2.destroyAllWindows()
    img_grabber.terminate()
