from wrapperMain import *
from remove_letters import *
import os

if __name__ == "__main__":
    pt.tesseract_cmd = '/usr/bin/tesseract'
    os.chdir('../MaterialeRomana')
    for image in os.listdir('.'):
        splitName = image.split(".")
        if(len(splitName) > 1):
            if(splitName[1] == 'png' or splitName[1] == 'jpg'):
                print('Processing image ' + image)
                generateProcessedFiles(splitName)
                remove_letters(image, splitName[0] + 'output.box')