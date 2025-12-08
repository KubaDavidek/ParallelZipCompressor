import os
import zipfile


'''
cte soubory z queue a nacte jejich data do outpu_queue
'''
def zip_worker(queue, output_queue, input_folder):


    while True:
        file_path = queue.get()

        if file_path is None:
            output_queue.put(None)
            break

        try:
            with open(file_path, "rb") as f:
                data = f.read()

            relative_path = os.path.relpath(file_path, input_folder)
            output_queue.put((relative_path, data))

        except:
            pass



def zip_writer(output_queue, lock, zip_path, worker_count):
            finished_workers = 0

            with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
                while True:
                    item = output_queue.get()

                    if item is None:
                        finished_workers += 1
                        if finished_workers == worker_count:
                            break
                        continue

                    file_path, data = item

                    with lock:
                        zipf.writestr(file_path, data)
                        print("zabaleno:", file_path)
