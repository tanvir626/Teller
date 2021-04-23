import pyttsx3
f=open("a.txt","r")
a=f.read().replace('\n',' ')
speaker=pyttsx3.init()
speaker.setProperty('voice',"english_rp+f4")
speaker.say(a)
speaker.runAndWait()