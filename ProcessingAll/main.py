from procesare_continut import separare_chei
import os,sys
rootdir = '../TextIntermediar/'
targetdir="../Img+TextFinal/"

for dirpath,_,filenames in os.walk(rootdir):
       for f in filenames:
           filepath=os.path.abspath(os.path.join(dirpath, f))
           separare_chei(filepath,targetdir)