from tkinter import *
import pyttsx3

#window
root=Tk()
root.title("Text to speech")
root.iconbitmap(r"logo.ico")
root.resizable(0,0)

#Creating canvas & background
can=Canvas(root,width=600,height=400,bg="#ACDB57")
can.pack(fill="both",expand=True)

#Header
l1=Label(root,text="Text To Speech",font="Arial 28 bold",bg="#ACDB57",bd=2)
ls=can.create_window(300,30,window=l1)

#Text Box
e1=Text(root,width=50,height=12,bg="#F1F8A2",font="Arial 15 ")
es=can.create_window(300,200,window=e1)


#Botton
#Start button
def start():
	speaker=pyttsx3.init()
	speaker.setProperty('voice',"english_rp+f4")
	
	if not e1.get("1.0","end-1c"):
		speaker.say("Please write somthing")
		speaker.runAndWait()
	else:
		text=e1.get("1.0","end-1c")
		speaker.say(text)
		speaker.runAndWait()
b1=Button(root,text="Start",width=5,font="Arial 12 bold",command=start)
b1s=can.create_window(300,370,window=b1)

#Stop button
b2=Button(root,text="Stop",width=5,font="Arial 12 bold")
b2s=can.create_window(230,370,window=b2)

#Repeat Button
def repeat():
	start()
b3=Button(root,text="Repeat",width=5,font="Arial 12 bold",command=repeat)
b3s=can.create_window(370,370,window=b3)

#Clear button
def clear():
	e1.delete(1.0,END)

b3=Button(root,text="Clear",width=5,font="Arial 12 bold",command=clear)
b3s=can.create_window(550,370,window=b3)



root.mainloop()
