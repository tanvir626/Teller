from tkinter import *
#window
root=Tk()
root.title("Text to speech")
root.iconbitmap(r"logo.ico")
root.geometry("600x400")
root.configure(background="#ACDB57")

#Header
l1=Label(root,text="Text To Speech",font="Arial 28 bold",bg="#ACDB57",bd=2)
l1.pack(pady=10)

#box
e1=Text(root,width=50,height=12,bg="#F1F8A2",font="Arial 15 ")
e1.pack()

pb=Button(root,text="Pause")
pb.grid()
plb=Button(root,text="Play")
plb.pack()
rb=Button(root,text="Repeat")
rb.pack()

root.mainloop()
