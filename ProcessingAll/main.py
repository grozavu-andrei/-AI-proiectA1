from AI import procesare_continut
import os,sys
rootdir = '../TextIntermediar/'
targetdir="../Img+TextFinal/"

pathname = os.path.dirname(sys.argv[0])
print('path =', pathname)

for dirpath,_,filenames in os.walk(rootdir):
       for f in filenames:
           filepath=os.path.abspath(os.path.join(dirpath, f))
           print(filepath)
           procesare_continut.separare_chei(filepath,targetdir)