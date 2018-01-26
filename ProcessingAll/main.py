from procesare_continut import separare_chei
import os,sys
from wrapperMain import *
from remove_letters import *
import os
from generare import generare
rootdir = '../TextIntermediar/'
targetdir="../Img+TextFinal/"

#Process images using Tesseract
pt.tesseract_cmd = '/usr/bin/tesseract'
os.chdir('../MaterialeRomana')
for image in os.listdir('.'):
    splitName = image.split(".")
    if(len(splitName) > 1):
        if(splitName[1] == 'png' or splitName[1] == 'jpg'):
            print('Processing image ' + image)
            generateProcessedFiles(splitName)
            remove_letters(image, splitName[0] + 'output.box')

os.chdir('../Img+TextFinal')
for dirpath,_,filenames in os.walk(rootdir):
       for f in filenames:
           filepath=os.path.abspath(os.path.join(dirpath, f))
           separare_chei(filepath,targetdir)

os.chdir('../ProcessingAll')
generare(targetdir)