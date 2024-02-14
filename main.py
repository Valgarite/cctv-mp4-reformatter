import os
import shutil
import cv2
from text_processing import processOCR
from folder_explorer import search_loop
from img_extract import fraccionar_vid

if __name__ == "__main__":
    ruta_principal = r'C:\\Users\\La Maraña (Reborn)\\Desktop\\Útiles\\videos\\videodemo'
    search_loop(ruta_principal)