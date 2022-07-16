import socket
import os
import tkinter as tk
import subprocess
import glob


file = "/trunk/configure"
#Option 1
# code = subprocess.run(["/trunk/configure.sh"], shell = True)
# print(code)

#Option 2
subprocess.call("/srs/trunk/configure.sh")


#exit_code = subprocess.call('./practice.sh')
# path = glob.glob(file + "/**/*.txt", recursive = True)
# print(path)

# path1 = os.path.abspath(file)
# print(path1)
# os.startfile(path1)
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

#print("Your Computer Name: "+hostname+ "\nYour current IP Address is: "+IPAddr)

message = "This is the following rtmp URL for the GoPro app: \n rtmp://"+IPAddr+"/live/livestream \n\n\n This is the following HLS URL: \n http://"+IPAddr+"/live/livestream.m3u8 "
            

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