from pydub import AudioSegment
from pathlib import Path
import os
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
