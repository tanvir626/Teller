from tkinter import *
#

#window
root=Tk()
root.title("Text to speech")
root.iconbitmap(r"logo.ico")
root.resizable(0,0)


can=Canvas(root,width=600,height=400,bg="#ACDB57")
can.pack(fill="both",expand=True)

l1=Label(root,text="Text To Speech",font="Arial 28 bold",bg="#ACDB57",bd=2)
ls=can.create_window(300,30,window=l1)

e1=Text(root,width=50,height=12,bg="#F1F8A2",font="Arial 15 ")
es=can.create_window(300,200,window=e1)

b1=Button(root,text="Start",width=5,font="Arial 12 bold")
b1s=can.create_window(300,370,window=b1)

b2=Button(root,text="Stop",width=5,font="Arial 12 bold")
b2s=can.create_window(230,370,window=b2)

b3=Button(root,text="Repeat",width=5,font="Arial 12 bold")
b3s=can.create_window(370,370,window=b3)

l1=Label(root,text="Text To Speech",font="Arial 28 bold",bg="#ACDB57",bd=2)
ls=can.create_window(300,30,window=l1)


root.mainloop()
