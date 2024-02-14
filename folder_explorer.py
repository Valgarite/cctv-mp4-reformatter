import os

import cv2
from file_manager import mover_video
from video_processing import read_video

def search_loop(root_folder_url: str):
    test_list = ['camera', '03', "01"]
    for root, dirs, files in os.walk(root_folder_url):
        # print(root, dirs, files, sep=" ")
        for file in files:
            if file.endswith(".mp4") or file.endswith(".MP4"):
                ruta_completa = os.path.join(root, file)
                # ruta_completa = "prueba\\y2mate.com - FPV Drone Flight through Beautiful Iceland Canyon_v240P.mp4"
                print(ruta_completa)
                video = cv2.VideoCapture(ruta_completa)
                vid_scan_result = read_video(video)
                
                print("mover")
                target_folder = vid_scan_result[1][0]
                mover_video()
                