from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube
import os
import re
import moviepy.editor as mp

# import socket

folder_name=''
# socket.getaddrinfo('localhost', 25)
def openloction():
    global folder_name
    folder_name=filedialog.askdirectory()
    if(len(folder_name)>1):
        plabel.config(text=folder_name,fg="green")
    else:
        plabel.config(text="Please specify the location",fg="red")

def downvideo():
    global folder_name
    url=urlentry.get()
    choice=ytchoices.get()
    
    if(len(url)>1):
        errolable.config(text='')
        yt=YouTube(url)
        
        if(choice==choices[0]):
            select=yt.streams.filter(progressive=True).get_by_resolution("240p")
        elif(choice==choices[1]):
            select=yt.streams.filter(progressive=True).get_by_resolution("360p")
        elif(choice==choices[2]):
            select=yt.streams.filter(progressive=True).get_by_resolution("720p")
    else:
         errolable.config(text="Paste Link Again",fg="red")

    select.download(folder_name)
    errolable.config(text="Download Complete !!!")

def downaudio():
    url=urlentry.get()
    
    if(len(url)>1):
        errolable.config(text='')
        yt=YouTube(url)
        select=yt.streams.filter(only_audio=True).first()
    else:
            errolable.config(text="Paste Link Again",fg="red")
    
    select.download(folder_name)
    errolable.config(text="Download Complete !!!")
    


root=Tk()
root.title("yt Download")
root.geometry("500x300")
root.resizable(False,False)
root.columnconfigure(0,weight=1)


#Title
l1=Label(root,text="YT Downloader",font="none 14")  
l1.grid()

#enter url lable
l1=Label(root,text="Paste The Link Here :",font="none 14")  
l1.place(relx=0.1,rely=0.2)

# url entry box
entryvar=StringVar()
urlentry= Entry(root)
urlentry.place(relx=0.5,rely=0.22,relwidth=0.4)

# error lable
errolable= Label(root,text=" ",fg="red",font="none 10")
errolable.place(relx=0.6,rely=0.29)

#path
pbtn=Button(root,text="File Path",border=1,bg="#A52A2A",fg="white",command=openloction)
pbtn.place(relx=0.25,rely=0.4,relwidth=0.5)

# path error
plabel=Label(root,text="Select File Path",fg="red",font="none 10")
plabel.place(relx=0.4,rely=0.5)

# select video quality
vq=Label(root,text="Select Video Quality",font="none 15")
vq.place(relx=0.1,rely=0.6)

# download video button
dv=Button(root,text="Download video",border=1,bg="#A52A2A",fg="white",command=downvideo)
dv.place(relx=0.1,rely=0.78,relwidth=0.3)

#combobox
choices=["240p","360p","720p"]
ytchoices=ttk.Combobox(root,values=choices)
ytchoices.place(relx=0.5,rely=0.6,relwidth=0.3)

# download audio button
da=Button(root,text="Download mp3",border=1,bg="#A52A2A",fg="white",command=downaudio)
da.place(relx=0.6,rely=0.78,relwidth=0.3)

root.mainloop()

