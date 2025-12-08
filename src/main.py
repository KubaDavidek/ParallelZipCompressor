import os
import multiprocessing

from src.scanner import scan_folder
from src.zipper import zip_worker
from conf.config import INPUT_FOLDER, OUTPUT_FOLDER

def main():
    print("Main started")
    if not os.path.exists(INPUT_FOLDER):
        print("Zadana slozka neexistuje")
        return

    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    queue = multiprocessing.Queue()
    cpu_count = multiprocessing.cpu_count()

    producer = multiprocessing.Process(target=scan_folder, args=(INPUT_FOLDER, queue))
    producer.start()

    workers = []

    for i in range(cpu_count):
        p = multiprocessing.Process(target=zip_worker, args=(queue, OUTPUT_FOLDER))
        p.start()
        workers.append(p)

    producer.join()

    for worker in workers:
        worker.join()

    print("Zipovani dokonceno")

if __name__ == "__main__":
    main()

