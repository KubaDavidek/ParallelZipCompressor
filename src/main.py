import os
import multiprocessing

from src.scanner import scan_folder
from src.zipper import zip_worker, zip_writer
from conf.config import INPUT_FOLDER, OUTPUT_FOLDER, FINAL_ZIP_NAME


def main():

    if not os.path.exists(INPUT_FOLDER):
        print("Zadaná složka neexistuje")
        return

    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    cpu_count = multiprocessing.cpu_count()

    queue = multiprocessing.Queue()
    output_queue = multiprocessing.Queue()
    lock = multiprocessing.Lock()

    final_zip_path = os.path.join(OUTPUT_FOLDER, FINAL_ZIP_NAME)

    producer = multiprocessing.Process(
        target=scan_folder,
        args=(INPUT_FOLDER, queue, cpu_count)
    )

    workers = []
    for i in range(cpu_count):
        p = multiprocessing.Process(target=zip_worker,args=(queue, output_queue, INPUT_FOLDER))
        workers.append(p)

    writer = multiprocessing.Process(target=zip_writer,args=(output_queue, lock, final_zip_path, cpu_count))

    producer.start()
    for w in workers:
        w.start()
    writer.start()

    producer.join()
    for w in workers:
        w.join()
    writer.join()

    print("ZIPOVÁNÍ DOKONČENO")


if __name__ == "__main__":
    main()
