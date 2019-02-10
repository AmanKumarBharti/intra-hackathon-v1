#!/usr/bin/env python3
"""Script for Tkinter GUI chat client."""
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter
from tkinter import *



def receive():
    """Handles receiving of messages."""
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8")
            msg_list.insert(tkinter.END, msg)
        except OSError:  # Possibly client has left the chat.
            break


def send(event=None):  # event is passed by binders.
    """Handles sending of messages."""
    msg = my_msg.get()
    my_msg.set("")  # Clears input field.
    client_socket.send(bytes(msg, "utf8"))
    if msg == "{quit}":
        client_socket.close()
        top.quit()


def on_closing(event=None):
    """This function is to be called when the window is closed."""
   
    send()

top = tkinter.Tk()
top.title("IIIT-NR CHAT")



messages_frame = tkinter.Frame(height="500",width="1000")
my_msg = tkinter.StringVar()  # For the messages to be sent.
my_msg.set("Type your Name  here.")
my_msg.set("Type your messages")

scrollbar = tkinter.Scrollbar(messages_frame)  # To navigate through past messages.
# Following will contain the messages.
msg_list = tkinter.Listbox(messages_frame, height=35, width=1000, yscrollcommand=scrollbar.set,fg="green",bg="black")
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()
messages_frame.pack()
master=Tk()
entry_field = tkinter.Entry(top, textvariable=my_msg,width="400")
entry_field.bind("<Return>", send)
entry_field.pack()
send_button = tkinter.Button(top, text="Send", command=send,fg="white",bg="green",activebackground="yellow",width=30)
send_button.pack(side="right")
exit_button= tkinter.Button(top,text="Exit",command=exit,fg="white",bg="red",activebackground="yellow",width=30)
exit_button.pack(side="right")
null_button=tkinter.Button(top,bg="#757575",width="300",activebackground="#757575",text="DEVLOPED BY TEAM MORNING STAR")
null_button.pack(side="right")

top.protocol("WM_DELETE_WINDOW", on_closing)

#----Now comes the sockets part----
HOST = input('Enter host: ')
PORT = input('Enter port: ')
if not PORT:
    PORT = 33000
else:
    PORT = int(PORT)

BUFSIZ = 1024
ADDR = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

receive_thread = Thread(target=receive)
receive_thread.start()
tkinter.mainloop()  # Starts GUI execution.
