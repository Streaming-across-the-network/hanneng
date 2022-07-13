import socket
import os
import tkinter as tk

file = "MonaServer.exe"

path = os.path.abspath(file)

os.startfile(path)

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

#print("Your Computer Name: "+hostname+ "\nYour current IP Address is: "+IPAddr)

message = "This is the following rtmp URL for the GoPro app: \n rtmp://"+IPAddr+"/live/1"

def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("!")
    label = tk.Label(popup, text=msg, font= ("Courier", 30))
    label.pack(side="top", fill="x", pady=10)
    B1 = tk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()
    
popupmsg(message)
    
#print("The following RTMP adress u should use: \n rtmp://"+IPAddr+"/live/1")
