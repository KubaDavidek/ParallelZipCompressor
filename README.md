Tento projekt ke školní program v PYTHON jazyce, který paralelně prochází složku a nalezené soubory a zabalí do výsledného zipu.

Ukázka řešení producer-consumer problému

Struktura projektu:

scanner.py - prochází složku a posílá cesty k souborům do fronty.
zipper.py 
(worker) - paralelně čtou obsah souborů.
(writer) - zapisuje data do finálního ZIP archivu.

