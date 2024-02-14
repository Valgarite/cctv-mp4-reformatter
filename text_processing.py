import easyocr
import pandas as pd

NO_DATE = "no-date.mp4"
NO_TIME = "no-time"

reader = easyocr.Reader(['en'])

def processOCR(imgURL: str):
    ocr_result = reader.readtext(imgURL)
    print(ocr_result)
    best_date_certainty, best_time_certainty = 0 , 0
    camera_number = None
    previous_word = None
    found_cam = 'other_cam'
    for result in ocr_result:
        word, certainty = result[1], result[2]
        if previous_word == 'Camera':
            camera_number = word
        previous_word = word
        check_date = is_date(word)
        check_time = is_time(word)
        if check_date != NO_DATE:
            date_certainty = certainty
        elif check_time != NO_TIME:
            time_certainty = certainty
        
        if check_date != NO_DATE and date_certainty >= best_date_certainty:
            best_date = check_date
            best_date_certainty = date_certainty
            print("date: ", best_date, best_date_certainty)
            
        if check_time != NO_TIME and time_certainty >= best_time_certainty:
            best_time = check_time
            best_time_certainty = time_certainty
            print("time: ", best_time, best_time_certainty)
    if camera_number==2 or camera_number == 3:
        found_cam = camera_number
    return f'Cam{found_cam}D{best_date}T{best_time}'

def is_date(date_string: str) -> str:
    try:
        return str(pd.to_datetime(date_string, format='%m-%d-%Y').strftime('%Y-%m-%d'))
    except Exception:
        return NO_DATE

def is_time(time_string: str) -> str:
    try:
        print(time_string)
        return str(pd.to_datetime(time_string, format='%H:%M:%S').strftime('%H_%M_%S'))
    except Exception:
        return NO_TIME