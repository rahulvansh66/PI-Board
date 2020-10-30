import wikipedia
import re
import speech_recognition as sr
import pyttsx
from pygame import mixer
import commands as c
import os
import webbrowser
import win32com.client as wincl
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


speak = wincl.Dispatch("SAPI.SpVoice")
mixer.init()

cred = credentials.Certificate(".\\firebase project.json")
firebase_admin.initialize_app(cred, {"databaseURL": "firebase project link"})
root = db.reference()

while True:
     
    # Speech recognition using Google Speech Recognition
    try:
        flag = root.child("desktop/flag").get()
        n_ref = root.child('desktop')
        flag = int (flag)
        #print(flag)
        if(flag == 1):
        	mixer.music.load('chime1.mp3')
        	mixer.music.play()
        	n_ref.update({'flag' :""})
	        msg = root.child("desktop/input").get()
	        n_ref.update({'input' :""})
	        print("You said: " + msg )
	        msg = msg.lower()
	        if ("on led1" in msg) or ("on led 1" in msg):
		        GPIO.output(7,1)
		        n_ref = root.child('home')
		        n_ref.update({'led1' :"1" })
		    elif("on led2" in msg) or ("on led 2" in msg)::
		        GPIO.output(5,1)
		        n_ref = root.child('home')
		        n_ref.update({'led2' :"1" })
		    elif("off led1" in msg) or ("off led 1" in msg):
		        GPIO.output(7,0)
		        n_ref = root.child('home')
		        n_ref.update({'led1' :"0" })
		    elif("off led2" in msg) or ("off led 2" in msg):
		        GPIO.output(5,0)
		        n_ref = root.child('home')
		        n_ref.update({'led2' :"0" })
		    elif(msg == "close" or msg=="close connection"):
		        break
		    else:
		        print("Invalid input, please try again")
    except Exception as e:
    	x=5