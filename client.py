import socket
from threading import Thread
from tkinter import *
from tkinter import ttk
import ftplib
import os
import ntpath #This is used to extract filename from path

from tkinter import filedialog
from pathlib import Path


from playsound import playsound
import pygame
from pygame import mixer

PORT  = 8080
IP_ADDRESS = '127.0.0.1'
SERVER = None
BUFFER_SIZE = 4096


name = None
listbox =  None
textarea= None
labelchat = None
text_message = None




# Boilerplate Code
def acceptConnections():
    global SERVER
    global clients
    while True:
        client, addr = SERVER.accept()
        client, name = client.recv(4096).decode().lower()
        clients[client_name] = {
                "client"   : client,
                "address"  : addr,
                "connected_with"  : "",
                "file_name"  : "",
                "file_size"  : 4096
            }
        print(f"Connection established with {client_name} : {addr}")
        thread = Thread(target = handleClient, args=(client,client_name,))
        thread.start()

# Teacher Activity
def showClientsList():
    global listbox
    listbox.delete(0,"end")
    SERVER.send("show list".encode('ascii'))


# Prevoius class code
# Here we ended the last class
def connectToServer():
    global SERVER
    global name
    global sending_file

    cname = name.get()
    SERVER.send(cname.encode())


def openChatWindow():

    print("\n\t\t\t\tIP MESSENGER")

    #Client GUI starts here
    window=Tk()

    window.title('Messenger')
    window.geometry("500x350")

    global name
    global listbox
    global textarea
    global labelchat
    global text_message
    global filePathLabel

    namelabel = Label(window, text= "Enter Your Name", font = ("Calibri",10))
    namelabel.place(x=10, y=8)

    name = Entry(window,width =30,font = ("Calibri",10))
    name.place(x=120,y=8)
    name.focus()

    connectserver = Button(window,text="Connect to Chat Server",bd=1, font = ("Calibri",10), command = connectToServer)
    connectserver.place(x=350,y=6)

    separator = ttk.Separator(window, orient='horizontal')
    separator.place(x=0, y=35, relwidth=1, height=0.1)

    labelusers = Label(window, text= "Active Users", font = ("Calibri",10))
    labelusers.place(x=10, y=50)

    listbox = Listbox(window,height = 5,width = 67,activestyle = 'dotbox', font = ("Calibri",10))
    listbox.place(x=10, y=70)

    scrollbar1 = Scrollbar(listbox)
    scrollbar1.place(relheight = 1,relx = 1)
    scrollbar1.config(command = listbox.yview)

    # Student Activity 1
    playButton=Button(window,text="play",bd=1, font = ("Calibri",10), command= play)
    playButton.place(x=282,y=160)

    # Bolierplate Code
    Stop=Button(window,text="Stop",bd=1, font = ("Calibri",10), command= stop)
    Stop.place(x=350,y=160)

    # Teacher Activity
    refresh=Button(window,text="Refresh",bd=1, font = ("Calibri",10), command = showClientsList)
    refresh.place(x=435,y=160)

    labelchat = Label(window, text= "Chat Window", font = ("Calibri",10))
    labelchat.place(x=10, y=180)

    textarea = Text(window, width = 67,height = 6,font = ("Calibri",10))
    textarea.place(x=10,y=200)

    scrollbar2 = Scrollbar(textarea)
    scrollbar2.place(relheight = 1,relx = 1)
    scrollbar2.config(command = listbox.yview)

    attach=Button(window,text="Attach & Send",bd=1, font = ("Calibri",10))
    attach.place(x=10,y=305)

    text_message = Entry(window, width =43, font = ("Calibri",12))
    text_message.pack()
    text_message.place(x=98,y=306)

    send=Button(window,text="Send",bd=1, font = ("Calibri",10))
    send.place(x=450,y=305)

    filePathLabel = Label(window, text= "",fg= "blue", font = ("Calibri",8))
    filePathLabel.place(x=10, y=330)

    window.mainloop()


def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))


    # Boilerlate Code
    receive_thread = Thread(target=receiveMessage)               #receiving multiple messages
    receive_thread.start()

    openChatWindow()

setup()

def play():
    global song_selected 
    song_selected = listbox.get(ANCHOR)

    pygame
    mixer.init()
    mixer.music.load('shared_files/'+song_selected)
    mixer.music.play()
    if(song_selected!= ""):
        infolabel.configuire(text="Now Playing: " +song_selected)
    else:
        infolabel.configuire(text="")
