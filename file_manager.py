import os
import shutil

def mover_video(ruta_org: str, output_folder: str):
    output_folder = os.path.join("output", output_folder)
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    filename = os.path.basename(ruta_org)
    output_file = os.path.join(output_folder, filename)
    # shutil.move(ruta_org, output_file)
    print(f"Se movió el archivo {filename} a {output_folder}")