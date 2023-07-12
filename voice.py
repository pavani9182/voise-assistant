
import pyttsx3 
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes

def sptext():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
         print('Listening...')
         recognizer.adjust_for_ambient_noise(source)
         audio=recognizer.listen(source)
         try:
              print("recognizing...")
              data=recognizer.recognize_google(audio)
              print(data)
              return data    
         except sr.UnknownValueError:
              print("can't hear you...")

def speechtxt(x):
     engine= pyttsx3.init()
     voices = engine.getProperty('voices')
     engine.setProperty('voice', voices[1].id)
     rate= engine.getProperty('rate')
     engine.setProperty('rate',120)
     engine.say(x)
     engine.runAndWait()

if __name__ == '__main__':
     
  while True:
    
    data1=sptext().lower()

    if "your name" in data1:
         name="my name is alexa"
         speechtxt(name)
    elif "time now" in data1:
         time=datetime.datetime.now().strftime("%I%M%p")
         speechtxt(time)
    elif "old" in data1:
         age="I am sixteen year old"
         speechtxt(age)
    elif "youtube" in data1:
         webbrowser.open("https://www.youtube.com/")
    elif "netflix" in data1:
         webbrowser.open("https://www.netflix.com/")
    elif "google" in data1:
         webbrowser.open("https://www.google.com/")
    elif "joke" in data1:
         joke_1=pyjokes.get_joke(language="en",category="neutral")
         print(joke_1)
         speechtxt(joke_1)
    elif "exit" in data1:
         speechtxt("Thank you")
         break

         
