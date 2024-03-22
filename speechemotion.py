import tkinter as tk
from tkinter import filedialog
from tkinter import *
import tensorflow as tf

import numpy as np
import cv2
from tensorflow.keras.models import model_from_json
from PIL import Image,ImageTk
import numpy as np
import cv2
from keras.models import load_model
from keras.preprocessing.image import img_to_array

top = tk.Tk()
top.geometry('1920x800')
top.title('Real time Speech Emotion Detector')
top.configure(background='#CDCDCD')

label1 = Label(top, background='#CDCDCD', font = ('arial',15,'bold'))
sign_image = Label(top)
    
def speech():
    from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
    import speech_recognition as sr
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print('Clearing background noise...')
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print('Waiting for your message...')
        recordedaudio=recognizer.listen(source)
        print('Done recording..')
    try:
        print('Printing the message..')
        text=recognizer.recognize_google(recordedaudio, language='en-US')
        print('Your message: {}'.format(text))
    except Exception as ex:
        print(ex)

    Sentence=[str(text)]

    analyser=SentimentIntensityAnalyzer()
    for i in Sentence:
        v=analyser.polarity_scores(i)
        print(v)
        maxi = max(v, key=v.get)
        print(maxi)
        if(maxi == "pos"):
            texte="Positive"
        elif(maxi=="neg"):
            texte = "Negative"
        elif(maxi=="neu"):
            texte="Neutral"
        else:
            texte = "Compound"
        label1.configure(foreground = "#011638",text=texte)
    


upload = Button(top, text = "Analyse tone", command=speech,padx=2,pady=5)
upload.configure(background="#364156", foreground='white', font=('arial', 15, 'bold'))
upload.pack(side='bottom',pady=20)
sign_image.pack(side='bottom', expand='True')
label1.pack(side='bottom', expand='True')
heading =Label(top, text='Real time Speech Emotion Detector',pady=20, font=('arial', 25, 'bold'))
heading.configure(background='#CDCDCD', foreground="#364156")
heading.pack()
top.mainloop()
