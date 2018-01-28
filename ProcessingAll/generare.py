import os
import random
#from PIL import Image


def random_line(fisier, no=1):
    line = []
    while (no >= 1):
        one_line = random.choice(open(fisier).readlines())
        line.append(one_line.rstrip())
        no = no - 1
    return line


def generare(dir):
    filename = random.choice(os.listdir(dir))
    while (filename[-4:] != ".txt" and filename!="intrebari.txt"):
        filename = random.choice(os.listdir(dir))
    sentence = random_line(os.path.realpath('intrebari.txt'))
    os.chdir(dir)
    no = sentence[0].split()[0]
    sentence = sentence[0].split(' ', 1)[1]
    words = random_line(filename, int(no))
    for i in range(0, int(no)):
        sentence = sentence.replace("_", words[i], 1)

    print(sentence)
    cap_file = filename.replace(".txt", "")
    jpg = cap_file + ".jpg"
    png = cap_file + ".png"
    if (os.path.isfile(jpg)):
        #image = Image.open(jpg)
        # image.show()
        os.system("ristretto " + jpg)
        print(jpg)
    elif (os.path.isfile(png)):
        #image = Image.open(png)
        # image.show()
        print(png)
        os.system("ristretto " + png)
    else:
        print("Nu exista o imagine corespunzatoare")

# generare("intrebari")