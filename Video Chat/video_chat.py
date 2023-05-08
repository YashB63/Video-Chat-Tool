from vidstream import *
import tkinter as tk
import socket
import threading
import requests


local_ip_address = socket.gethostbyname(socket.gethostname())
#public_ip_address = requests.get('https://api.ipify.org').text
#server = StreamingServer('Your IP Address', 9999)

server = StreamingServer(local_ip_address, 9999)
reciever = AudioReceiver(local_ip_address, 8888)


def start_listening():
    th1 = threading.Thread(target=server.start_server)
    th2 = threading.Thread(target=reciever.start_server)
    th1.start()
    th2.start()


def start_camera_stream():
    camera_client = CameraClient(text_target_ip.get(1.0,'end-1c'), 7777)
    th3 = threading.Thread(target=camera_client.start_stream)
    th3.start()


def start_screen_sharing():
    screen_client = ScreenShareClient(text_target_ip.get(1.0,'end-1c'), 7777)
    th4 = threading.Thread(target=screen_client.start_stream)
    th4.start()


def start_audio_stream():
    audio_Sender = AudioSender(text_target_ip.get(1.0,'end-1c'), 6666)
    th5 = threading.Thread(target=audio_Sender.start_stream)
    th5.start()



#---------------------------------GUI------------------------------

window = tk.Tk()
window.title("Yash Calls v1 Nitro")
window.geometry('300x200')

label_target_ip = tk.Label(window, text="Target Ip:")
label_target_ip.pack()

text_target_ip = tk.Text(window, height=1)
text_target_ip.pack()

btn_listen = tk.Button(window, text="Start Listening", width=50, command=start_listening)
btn_listen.pack(anchor=tk.CENTER, expand=True)

btn_camera = tk.Button(window, text="Start Camera Stream", width=50, command=start_camera_stream)
btn_camera.pack(anchor=tk.CENTER, expand=True)

btn_screen = tk.Button(window, text="Start Screenshare", width=50, command=start_screen_sharing)
btn_screen.pack(anchor=tk.CENTER, expand=True)

btn_audio = tk.Button(window, text="Start Audio Stream", width=50, command=start_audio_stream)
btn_audio.pack(anchor=tk.CENTER, expand=True)

window.mainloop()



