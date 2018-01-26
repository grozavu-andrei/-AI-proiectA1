import csv
import cv2
from pytesseract import pytesseract as pt
from PIL import Image
import sys


# Path-ul catre Tesseract pe Ubuntu. Modifica linia asta daca folosesti Win
pt.tesseract_cmd = '/usr/bin/tesseract'

def generateProcessedFiles(splittedName):
    # Get string from Image
    fullName = splittedName[0] + '.' +  splittedName[1]
    imgText = pt.image_to_string(Image.open(fullName), lang='ron')

    with open('../TextIntermediar/' + splittedName[0] + "text.txt", 'w') as f:
        f.write(imgText)

    # Get bounding boxes
    pt.run_tesseract(fullName, splittedName[0] + 'output', lang='ron', boxes=True, config="hocr")

    #Remove non-alphanumeric characters
    with open(splittedName[0] + 'output.box', 'r+') as f:
        buf = ''
        for line in f:
            if line[0].isalnum() or line[0]=='(' or line[0] == ')':
                buf += line
        f.seek(0)
        f.write(buf)

    # To read the coordinates
    boxes = []
    with open(splittedName[0] + 'output.box', 'r') as f:
        reader = csv.reader(f, delimiter = ' ')
        for row in reader:
            if(len(row)==6):
                boxes.append(row)

    # Draw the bounding box
    # img = cv2.imread(fullName)
    # h, w, _ = img.shape
    # for b in boxes:
    #     img = cv2.rectangle(img,(int(b[1]),h-int(b[2])),(int(b[3]),h-int(b[4])),(255,0,0),2)

    # img = Image.fromarray(img)
    # img.save(splittedName[0] + "-out." + splittedName[1])

if __name__ == "__main__":
    splitName = sys.argv[1].split(".")
    pt.tesseract_cmd = '/usr/bin/tesseract'
    generateProcessedFiles()