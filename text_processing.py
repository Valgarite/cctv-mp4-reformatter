import easyocr
import pandas as pd

def processOCR(imgURL: str):
    reader = easyocr.Reader(['en'])
    ocr_result = reader.readtext(imgURL, detail = 0)
    wanted_strings = ["camera", "02", "03"]
    found = any(word in ocr_result for word in wanted_strings)
    comparison = 3
    for word in ocr_result:
        print(word)
        check_result = is_date(word)
        if check_result[0] < comparison:
            best_result = str(check_result[0][1])
        print(is_date(word))
    return best_result

def is_date(date_string):
    try:
        return (0, str(pd.to_datetime(date_string, format='%m-%d-%Y')))
    except Exception:
        try:
            return (1, str(pd.to_datetime(date_string, format='%m-%Y')))
        except Exception:
            return (2, "no-date")