from pydub import AudioSegment
from pathlib import Path
import os
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
