from pydub import AudioSegment
from pydub.playback import play
from pathlib import Path
import os
import mutagen
from io import BytesIO
from PIL import Image

def fplay (flist):
    for i in flist:    
        print (Path.readlink(i)) 
        audio = mutagen.File(i)
        if 'audio/mp3' in audio.mime:
            images = [audio[i] for i in audio if "APIC" in i]
        elif 'audio/flac' in audio.mime:
            images = audio.pictures

        for imgb in images:
            img = Image.open(BytesIO(imgb.data))
            img.show()


        a=AudioSegment.from_file(i)
        aa =  a.fade_in(5000)
        ab = aa.fade_out(5000)
        play(ab)
        
flist=os.listdir('.')
flist1=[Path(i) for i in sorted(flist)]
flist2 =[i for i in flist1 if Path(i).suffix== '.flac']
fplay(flist2)
