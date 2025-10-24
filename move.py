from tkinter import *
import tkinter as tk
from tkinter import filedialog
import os
import sys
import shutil
from pathlib import Path

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
