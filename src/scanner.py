import os

'''
fce projde zadany folder, najde soubory, vezme jejich cestu a a vlozi ji do "queue"
'''
def scan_folder(folder, queue):

    for root, dirs, files in os.walk(folder):
        for name in files:
            # path = cesta k souboru, vlozi se do queue
            path = os.path.join(root, name)
            queue.put(path)


        cpu_count = os.cpu_count()

        # posleme "None" pro kaydz worker, aby vedeli, ze uz neni dalsi prace a ukonci se
        for i in range(cpu_count):
            queue.put(None)

