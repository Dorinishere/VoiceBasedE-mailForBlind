from Google import Create_Service
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pyglet
import os, time
import socket
from gtts import gTTS
import pyglet
import os, time
import speech_recognition as sr
import reademail



print ("-"*60)
print ("Project:Voice based Email for blind")
print ("-"*60)

#project name
ts = gTTS(text="Project: Voice based Email for blind", lang='en', slow=False)
tsname=("path/voice_based_email_mysite_audio.mp3")
ts.save(tsname)
music = pyglet.media.load(tsname, streaming = False)
music.play()

time.sleep(music.duration)
os.remove(tsname)

#login from os
login = os.getlogin
print ("You are logged In from : "+login())

#choices
print ("1. Compose a mail.")
ts = gTTS(text="option 1. Composed a mail.", lang='en',slow=False)
tsname=("path/voice_based_email_mysite_audio.mp3")
ts.save(tsname)

music = pyglet.media.load(tsname, streaming = False)
music.play()

time.sleep(music.duration)
os.remove(tsname)

print ("2. Check your inbox")
ts = gTTS(text="option 2. Check your inbox", lang='en',slow=False)
tsname=("hello.mp3")
ts.save(tsname)

music = pyglet.media.load(tsname, streaming = False)
music.play()

time.sleep(music.duration)
os.remove(tsname)
#this is for input choices
#ts = gTTS(text="Your choice ", lang='en')
#tsname=("path/hello.mp3")
#ts.save(tsname)

#music = pyglet.media.load(tsname, streaming = False)
#music.play()

#time.sleep(music.duration)
#os.remove(tsname)
r = sr.Recognizer()
with sr.Microphone() as source:
        print("choice:")
        ts = gTTS(text="choice", lang='en',slow=False)
        tsname=("path/hello.mp3")
        ts.save(tsname)

        music = pyglet.media.load(tsname, streaming = False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
        audio = r.listen(source)
            # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
        try:
                # using google speech recognition
                text1 = r.recognize_google(audio)
                

                #print('Converting audio transcripts into text ...')
                print(text1)
                ########condition of if else
                if(text1=='compose a mail'):
                    CLIENT_SECRET_FILE = 'client_secret.json'
                    API_NAME = 'gmail'
                    API_VERSION = 'v1'
                    SCOPES = ['https://mail.google.com/']

                    service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

                    r = sr.Recognizer()
                    with sr.Microphone() as source:
                        print("Speak your email message:")
                        ts = gTTS(text="Speak your email message", lang='en',slow=False)
                        tsname=("path/hello.mp3")
                        ts.save(tsname)

                        music = pyglet.media.load(tsname, streaming = False)
                        music.play()

                        time.sleep(music.duration)
                        os.remove(tsname)
                        audio = r.listen(source)
                            # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
                        try:
                                # using google speech recognition
                                text = r.recognize_google(audio)
                                #print('Converting audio transcripts into text ...')
                                print(text)
                                
                        except:
                            print('Sorry....run again...')
                    emailMsg = text
                    mimeMessage = MIMEMultipart()
                    mimeMessage['to'] = 'h.2002.uji@gmail.com'
                    r = sr.Recognizer()
                    with sr.Microphone() as source:
                            print("Speak your email subject:")
                            ts = gTTS(text="Speak your email subject", lang='en',slow=False)
                            tsname=("path/hello.mp3")
                            ts.save(tsname)

                            music = pyglet.media.load(tsname, streaming = False)
                            music.play()

                            time.sleep(music.duration)
                            os.remove(tsname)
                            audio = r.listen(source)
                            # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
                            try:
                                # using google speech recognition
                                text1 = r.recognize_google(audio)
                                #print('Converting audio transcripts into text ...')
                                print(text1)
                            except:
                                print('Sorry....run again...')
                    mimeMessage['subject'] = text1
                    mimeMessage.attach(MIMEText(emailMsg, 'plain'))
                    raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()

                    message = service.users().messages().send(userId='h.2002.uji@gmail.com', body={'raw': raw_string}).execute()
                    print(message)
        except:
                print('Sorry....run again...')
 ## reading email 
SERVICE2 = reademail.authenticate_gmail()
reademail.check_mails(SERVICE2)

                   


