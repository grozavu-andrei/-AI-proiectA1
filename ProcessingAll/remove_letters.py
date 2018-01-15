import os
from sys import argv
from PIL import Image

def takeArguments():
	try:
		if len(argv)<3:
			raise Exception("Insufficient number of arguments ! [picture.jpg] [coordonates.box]")
		else:
			file1 = argv[1]
			if not os.path.isfile(file1):
				raise Exception("File 1 doesn't exist!")
			file2 = argv[2]
			if not os.path.isfile(file2):
				raise Exception("File 2 doesn't exist!")
			return (file1,file2)
	except Exception as e:
		print(str(e))
		sys.exit()

def remove_letters(img, coordonatesFile):
	oldImage = Image.open(img)
	oldPixelMap = oldImage.load()

	newImage = Image.new(oldImage.mode, oldImage.size)
	newPixelMap = newImage.load()

	for i in range(oldImage.size[0]):
		for j in range(oldImage.size[1]):
			newPixelMap[i,j] = oldPixelMap[i,j]

	try:
		f = open(coordonatesFile)
	except Exception as e:
		print(str(e))
		sys.exit()

	lines = f.readlines()
	#remove whitespace characters like `\n` at the end of each line
	lines = [x.strip() for x in lines] 
	print(len(lines))
	for k in range(len(lines)-1):
		coordonates = lines[k].split(' ')
		print(k)
		if len(coordonates) > 4: 
			x = oldImage.size[1] - int(coordonates[4])
			y = oldImage.size[1] - int(coordonates[2])
			for i in range(int(coordonates[1])-5,int(coordonates[3])+6):
				for j in range(x-5,y+6):
					newPixelMap[i,j] = (255,255,255,0)

	newImage.save(img.split('.')[0] + "output.jpg")
	newImage.close()
	return newImage



if __name__=="__main__" :
	(image, coordonates) = takeArguments()
	remove_letters(image,coordonates)