from procesare_continut import separare_chei
import os,sys
from wrapperMain import *
from remove_letters import *
import os
from generare import generare
rootdir = '../TextIntermediar/'
targetdir="../Img+TextFinal/"

def processImages(dir):
    #Process images using Tesseract
    pt.tesseract_cmd = '/usr/bin/tesseract'
    os.chdir(dir)
    for image in os.listdir('.'):
        splitName = image.split(".")
        if(len(splitName) > 1):
            if(splitName[1] == 'png' or splitName[1] == 'jpg'):
                print('Processing image ' + image)
                generateProcessedFiles(splitName)
                remove_letters(image, splitName[0] + 'output.box')

def separateKeys():
    os.chdir('../Img+TextFinal')
    for dirpath,_,filenames in os.walk(rootdir):
           for f in filenames:
               filepath=os.path.abspath(os.path.join(dirpath, f))
               separare_chei(filepath,targetdir)

if __name__ == "__main__":
    choice = 0
    while choice!=3:
        print('-'*40)
        choice = int(input("1)Process images\n2)Generate question\n3)Exit\nChoice:"))
        if choice==1:
            processImages('../MaterialeRomana')
            separateKeys()
        elif choice==2:
            os.chdir('../ProcessingAll')
            generare(targetdir)