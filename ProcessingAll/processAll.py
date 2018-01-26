from wrapperMain import *
from remove_letters import *
import os

if __name__ == "__main__":
    imgDir = '/home/apo/Facultate/Anul3/AI/-AI-proiectA1/Materiale Romana'
    pt.tesseract_cmd = '/usr/bin/tesseract'
    for image in os.listdir(imgDir):
        splitName = image.split(".")
        generateProcessedFiles(image, imgDir)
        remove_letters(image, splitName[0] + 'output.box')