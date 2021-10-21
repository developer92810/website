import os

os.system("wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-386.zip")
os.system("unzip ngrok-stable-linux-386.zip")
os.system("./ngrok authtoken 1zpLme3OYe7GbtqDyKWLkZK366U_2Twq1S6VRU9HW21SwUbUp")
os.system("./ngrok http file:////app/site")
