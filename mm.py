from pydub import AudioSegment
from pathlib import Path
import os
import glob
from mutagen import File
from mutagen.flac import Picture, FLAC
from tkinter import *
import tkinter as tk
from tkinter import filedialog
import os
import sys
import shutil

def fcat(flist) : 
	audioSegs=[AudioSegment.from_file(i) for i in sorted(flist)]
	a=audioSegs[0]
	for i in audioSegs[1:] :
		a += (i)
	a.export("a.flac", format="flac")
	return (AudioSegment.from_file("a.flac"))
flist=os.listdir('.')
flist1=[Path(i) for i in flist]
print (flist1)
flist2 =[i for i in flist1 if Path(i).suffix== '.flac']
a=fcat(flist2)
print (len(a))

def trackN(d,i) :
	if d/i < 60*5*1000 :return i
	else: return trackN(d,i+1)

def trackLenList(total) :
	tnum=trackN(total,1) 
	time=total/tnum
	pivotList= [round(time*i+10000) for i in range(tnum)] + [total]
	pivotList[0]=0
	return(pivotList)
def pivotTuples (d): 
	tuples=trackLenList(d)
	return(list(zip(tuples,tuples[1:])))
a=AudioSegment.from_file("a.flac")
aLen=len(a)
pTuples=pivotTuples(aLen)
print (pTuples)
tlen=(len(pTuples))
print(tlen)
dived=[a[f:l] for (f,l) in pTuples]
strList=[str(round(i/1000)) for i in trackLenList(aLen)] 
print(strList)
for i in range (tlen): dived[i].export("t"+strList[i]+".flac",format="flac")

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


dir = filedialog.askdirectory() 
print(dir)
fl=os.listdir('.')
ts = [i for i in fl if i[0]=='t']
tfs=[Path(i) for i in ts]
tflacs=[i for i in tfs if Path(i).suffix== '.flac']
print (tflacs)
for i in tflacs: shutil.move(i,dir)
shutil.move("a.jpg",dir)
shutil.move("a.flac","/home/i/.local/share/Trash/files/a.flac")
fl=os.listdir('.')
print (fl)
fs=[Path(i) for i in fl]
f2g=[i for i in fs if Path(i).suffix== '.flac']
print (f2g)
for i in f2g: shutil.move(i,"/home/i/.local/share/Trash/files/i")
