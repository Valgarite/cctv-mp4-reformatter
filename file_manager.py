import os
import shutil

def mover_video(ruta_org: str, output_folder_name: str, new_filename: str):
    no_date_folder = "output/no_date_found"
    output_folder_name = os.path.join("output", output_folder_name)
    filename = os.path.basename(ruta_org)
    if(new_filename=="no-date.mp4"):
        if not os.path.exists(no_date_folder):
            os.makedirs(no_date_folder)
        no_change_in_filename = os.path.basename(ruta_org)
        output_file = os.path.join(no_date_folder, no_change_in_filename)
    else:
        if not os.path.exists(output_folder_name):
            os.makedirs(output_folder_name)
        output_file = os.path.join(output_folder_name, new_filename)
    pre, ext = os.path.splitext(output_file)
    shutil.move(ruta_org, pre + ".mp4")
    print(f"Se movió el archivo {filename} a {output_folder_name}")