import cv2

def fraccionar_vid(video: cv2.VideoCapture, partes: int):
    fcount = video.get(cv2.CAP_PROP_FRAME_COUNT)
    frames = []
    i=0
    while i<=partes:
        frames.append(fcount/partes * i)
        i+=1
    return frames