# text to speech

# from gtts import gTTS
# import os
# text = "yendha ninte peru"
# output = gTTS(text= text, lang="ml", slow=False)
# output.save("output.mp3")
# os.system("start output.mp3")


# --------------file to speech----------------------
from  gtts import gTTS
import os
text=open("demo.txt","r").read()
language="en"
output=gTTS(text=text,lang=language,slow=False)
output.save("fileoutput.mp3")
os.system("start fileoutput.mp3")