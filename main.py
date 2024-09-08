import pyttsx3
import pyaudio
import speech_recognition as sr
import datetime
import webbrowser
import random
import smtplib
import sys
import os
import pyautogui
import wmi
import psutil
import ctypes
import re
import wolframalpha
from datetime import datetime

# Information Print
INFO = '''
                *=======================================*
                |.....LISHA ARTIFICIAL INTELLIGENCE.....|
                +---------------------------------------+
                |        #NAME: L-I-S-H-A               |
                |        #OWNER: Aradhana Kushwaha      |
                |        #DATE: 8/9/2024                |
                *=======================================* 
            ''' 
print(INFO)            

# Initialize TTS Engine
engine = pyttsx3.init('sapi5')
client = wolframalpha.Client('V5T2P6-3VAKKLLVXU')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    print('lisha: ' + audio)
    engine.say(audio)
    engine.runAndWait()

    
def greet_user():
    """Greets the user according to the time"""

    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        speak(f"Good Morning ")
    elif (hour >= 12) and (hour < 16):
        speak(f"Good afternoon")
    elif (hour >= 16) and (hour < 19):
        speak(f"Good Evening")
    speak(f"Hello Aradhana Mam I am Lisha.  How may I assist you?")

def takeCommand():
    """Listens to user commands via the microphone and converts speech to text."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)  # Adjust for ambient noise
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that. Could you please repeat?")
        return "none"
    except sr.RequestError as e:
        speak(f"Sorry, my speech service is down; {e}")
        return "none"
    except Exception as e:
        print(f"Error: {e}")
        speak("Say that again, please.")
        return "none"
    return query.lower()

def sendEmail(to, content):
    """Sends an email to a specified address with the provided content."""
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('ak1234@gmail.com', 'paa1234')
        server.sendmail('ak1234@gmail.com', to, content)
        server.close()
        speak("Email has been sent!")
    except Exception as e:
        print(e)
        speak("Sorry, I was not able to send the email.")

if __name__ == "__main__":
    greet_user()  # Greet the user at the start
    while True:
        query = takeCommand()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            try:
                import wikipedia
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except ImportError:
                speak("Wikipedia module is not available.")

        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")
        
        elif 'open google' in query:
            speak('Okay')
            webbrowser.open("www.google.co.in")

        elif 'the time' in query:
            strTime = datetime.now().strftime("%H:%M:%S")
            speak(f"mam, the time is {strTime}")

        elif 'open gmail' in query:
            speak('Okay')
            webbrowser.open('www.gmail.com')

        elif 'open facebook' in query:
            speak('Okay')
            webbrowser.open('www.facebook.com')

        elif 'open whatsapp' in query:
            speak('Okay')
            webbrowser.open('www.whatsapp.com')

        elif 'open instragram' in query:
            speak('Okay')
            webbrowser.open('https://www.instagram.com')

        elif "what's up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))

        elif 'tell me about yourself' in query:
            speak('I am your digital assistant Lisha.')

        elif 'hello' in query:
            speak('Hello mam')
          
        elif 'love you' in query:
            speak('Love you too, mam')

        elif 'do you have a boyfriend' in query:
            speak('Yes mam')

        elif 'are you in a relationship' in query:
            speak('No mam, I am single')

        elif 'will you marry me' in query:
            speak('No sorry! I am digital assistant of aradhana mam')

        elif 'how old are you' in query:
            speak(' I am artificial intelligent ')

        elif 'who is your favourite actor' in query:
            speak('My favourite actor is Shahrukh khaan')

        elif 'what is your favourite food' in query:
            speak('My favourite food is internet')

        elif 'what is your favourite movie' in query:
            speak('My favourite movie is 3 Idiots')

        elif 'joke for me' in query:
            speak('Ha ha ha ha ha ha ha ha very funny')   

        elif 'screenshot' in query:
            speak('Okay, mam. Let me take a screenshot.')
            pic = pyautogui.screenshot()
            pic.save('C:/Users/USER/Desktop/screenshot.png')
            speak('Screenshot saved on your desktop.')

        elif 'brightness' in query:
            if 'decrease brightness' in query:
                dec = wmi.WMI(namespace='wmi')
                methods = dec.WmiMonitorBrightnessMethods()[0]
                methods.WmiSetBrightness(10, 0)
            
            elif 'increase brightness' in query:
                inc = wmi.WMI(namespace='wmi')
                methods = inc.WmiMonitorBrightnessMethods()[0]
                methods.WmiSetBrightness(100, 0)

        elif 'search' in query:
            webbrowser.open(query)

        elif 'lock my' in query:
            speak('Okay, mam.')
            ctypes.windll.user32.LockWorkStation()

        elif 'current weather in' in query:
            reg_ex = re.search('current weather in (.*)', query)
            if reg_ex:
                city = reg_ex.group(1)
                # Replace this with your weather function call
                speak(f'The current weather in {city} is...')  # Example placeholder

        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            speak('Okay. Bye mam, have a good day.')
            sys.exit()

        elif 'email to aradhana' in query:
            try:
                speak("What should I say?")
                content = takeCommand() 
                to = "aradhanakushwaha280@gmail.com"    
                sendEmail(to, content)
            except Exception as e:
                print(e)
                speak("Sorry, I was not able to send the email.")    

        elif 'bye' in query:
            speak('Bye mam, have a good day.')
            sys.exit()

        elif 'thanks' in query:
            speak('You are welcome, Aradhana mam')

        else:
            speak('Searching...')
            try:
                res = client.query(query)
                results = next(res.results).text
                speak('According to my database:')
                speak(results)
            except Exception as e:
                print(e)
                speak("I could not find an answer. Searching Google...")
                webbrowser.open('www.google.com')
