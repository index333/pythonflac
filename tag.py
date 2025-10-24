import glob
import os
from mutagen import File
from mutagen.flac import Picture, FLAC
l = glob.glob('./*.flac')
print(l)
def addP (fname,jname):
    image = Picture()
    image.type = 3
    mime = 'image/jpeg'
    audio = File(fname)
    image.desc = 'front cover'
    with open(jname, 'rb') as pic:
        image.data = pic.read()
        audio.add_picture(image)
        audio.save()
for f in l:
    addP (f,'a.jpg')
