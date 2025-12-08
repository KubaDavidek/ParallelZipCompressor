import os
import zipfile

'''
bere cesty k souborum z queue a kazdy soubor zabali do ZIP archivu
'''
def zip_worker(queue, output_folder):
    while True:
        file_path = queue.get()

        if file_path is None:
            break

        try:
            file_name = os.path.basename(file_path)
            zip_name = file_name + ".zip"
            zip_path = os.path.join(output_folder, zip_name)

            with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
                zf.write(file_path, arcname=file_name)

            print(f"Zabaleno: {file_name}")

        except Exception as e:
            print(f"Chyba pri zipovani: {file_path} ")