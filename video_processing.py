import os
import cv2
import pandas as pd

from text_processing import NO_DATE, processOCR

def read_video(video: cv2.VideoCapture)->str:
    video.set(cv2.CAP_PROP_FPS, 1)
    frame_list = slice_frames(video=video, quant=20)
    success, image = video.read()
    scan_result = NO_DATE
    found_cam = 'other_cam'
    certainties = {'date': 0, 'time': 0}
    while(success):
        try:
            os.mkdir('temp')
        except:
            pass
        for each_frame in frame_list:
            each_frame = int(each_frame)
            video.set(cv2.CAP_PROP_POS_FRAMES, each_frame)
            success, image = video.read()
            imgURL = f'temp/{each_frame}.jpg'
            each_frame = str(each_frame)
            print(imgURL)
            try:
                cv2.imwrite(imgURL, image)
            except:
                pass
            scan_result = processOCR(imgURL)
            
            if(scan_result['best_date_certainty'] > certainties['date']):
                certainties['date'] = scan_result['best_date_certainty']
                date = scan_result['date']
            if(scan_result['best_time_certainty'] > certainties['time']):
                certainties['time'] = scan_result['best_time_certainty']
                clock = scan_result['time']
            if scan_result['camera'] == "02" or scan_result['camera'] == "03":
                found_cam = scan_result['camera']
            print(found_cam)
        video.release()
        break
    filename = f"camera{found_cam}-{date}_{clock}.mp4"
    return filename

def slice_frames(video: cv2.VideoCapture, quant: int = 30):
    videoLength = video.get(cv2.CAP_PROP_FRAME_COUNT)
    frames = []
    i=0
    while i<quant:
        frames.append(int(videoLength/quant * i))
        i+=1
    return frames