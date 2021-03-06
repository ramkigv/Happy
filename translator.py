import googletrans
import speech_recognition as sr
import pyaudio
import pyttsx3
import time
import gtts
import playsound
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile
root = tk.Tk()
listener=sr.Recognizer()
translator = googletrans.Translator()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

indian_lang={
    "english": "en-IN",
    "tamil" : "ta-IN",
    "telugu" : "te-IN",
    "malayalam" : "ml-IN",
    "marathi " : "mr-IN",
    "kannada" : "kn-IN",
    "hindi" : "hi-IN",
    "gujarati" : "gu-IN",
    "bengali" : "bn-IN",
    "urdu" : "ur-IN",
}
def take_voice(input,mins):
    try:
        with sr.Microphone() as source:
            listener.pause_threshold=1
            voice =listener.listen(source,timeout=mins,phrase_time_limit=mins)
            text = listener.recognize_google(voice,language=input)
            print(text)
            return text
    except:
        talk("repeat again")
        return take_voice(input,mins)

def take_command():
    try:
        with sr.Microphone() as source:
            listener.pause_threshold = 1
            voice = listener.listen(source,timeout=3,phrase_time_limit=3)
            command=listener.recognize_google(voice)
            command=command.lower()
            print(command)
            return command
    except:
        talk("cant hear you, say again")
        return take_command()

def talk(text):
    rate = 130
    engine.setProperty('rate', rate)
    engine.say(text)
    engine.runAndWait()

def translators():
    time.sleep(3)
    value=int(e.get())
    talk("Welcome, your translator is ready")
    talk("Can I know what is the input language")
    input_lan = take_command()
    talk("Fine, can I know what is the output language")
    output_lan = take_command()
    talk("OKAY")
    input_lang = indian_lang[input_lan]
    var = googletrans.LANGUAGES
    var = {value: key for key, value in var.items()}
    output_lang = var[output_lan]
    talk("Let the speech starts")
    text = take_voice(input_lang,value)
    translated = translator.translate(text, dest=output_lang)
    print(translated.text)
    converted_audio = gtts.gTTS(translated.text, lang=output_lang)
    converted_audio.save('translated.mp3')
    playsound.playsound('translated.mp3')



canvas=tk.Canvas(root,width=400,height=600)
canvas.grid(columnspan=7,rowspan=15)

#logo
logo=Image.open("logo.png")
logo = ImageTk.PhotoImage(logo)
logo_label= tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=3, row=0)

#timerequired
instruction=tk.Label(root,text="Enter how many seconds you want to translate",font=("Arial",12),fg="#FF1493")
instruction.grid(column=3,row=1)
e=Entry(root,width=10)
e.grid(column=3,row=2)



#button
speak_text=tk.StringVar()
speak_btn=tk.Button(root,textvariable = speak_text,command=lambda:translators(),font="Raleway",bg="#FF1493",fg="white",height=2,width=15)
speak_text.set("Translate")
speak_btn.grid(column=3,row=3)




root.mainloop()











