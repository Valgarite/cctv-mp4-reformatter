import os
import cv2
import pandas as pd

from text_processing import processOCR

def read_video(video: cv2.VideoCapture):
    video.set(cv2.CAP_PROP_FPS, 1)
    frame_list = slice_frames(video=video, quant=30)
    success, image = video.read()
    scan_result = "no-data"
    while(success):
        try:
            os.mkdir('temp')
        except:
            pass
        for each_frame in frame_list:
            try:
                each_frame = int(each_frame)
                video.set(cv2.CAP_PROP_POS_FRAMES, each_frame)
                success, image = video.read()
                imgURL = f'temp/{each_frame}.jpg'
                each_frame = str(each_frame)
                print(imgURL)
                cv2.imwrite(imgURL, image)
                scan_result = processOCR(imgURL)
                os.remove(imgURL)
            except:
                print(Exception)
                pass
        video.release()
        break
    return scan_result

def slice_frames(video: cv2.VideoCapture, quant: int = 30):
    videoLength = video.get(cv2.CAP_PROP_FRAME_COUNT)
    frames = []
    i=0
    while i<quant:
        frames.append(int(videoLength/quant * i))
        i+=1
    return frames