from filechooser import FileChooser
from bandsorter import BandSorter
import os

filechooser = FileChooser()
print("Choix du fichier de cellules :")
filenameCells = filechooser.choosingFile("input")
bandsorter = BandSorter(filenameCells)
bandsorter.only4G()

