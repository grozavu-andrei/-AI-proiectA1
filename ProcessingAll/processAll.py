from wrapperMain import *
from remove_letters import *

if __name__ == "__main__":
    splitName = sys.argv[1].split(".")
    print(splitName)
    pt.tesseract_cmd = '/usr/bin/tesseract'
    generateProcessedFiles(splitName)
    remove_letters(sys.argv[1], splitName[0] + 'output.box')