import speech_recognition as sr
import smtplib
# import pyaudio
# import platform
# import sys
from bs4 import BeautifulSoup
import email
import imaplib
from gtts import gTTS
import pyglet
import os, time
global translation11,translation1
from translate import Translator

import speech_recognition as sr
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

#fetch project name
tts = gTTS(text="Voice Email system for blind People", lang='en')
ttsname=("name.mp3") 
tts.save(ttsname)

music = pyglet.media.load(ttsname, streaming = False)
music.play()

time.sleep(music.duration)
os.remove(ttsname)

#login from os
# login = os.getlogin
print ("Voice Email system for blind People")

#choices
print ("1. compose Your mail")
tts = gTTS(text="option 1. compose Your mail.", lang='en')
ttsname=("hello.mp3") #Example: path -> C:\Users\sayak\Desktop> just change with your desktop directory. Don't use my directory.
tts.save(ttsname)

music = pyglet.media.load(ttsname, streaming = False)
music.play()

time.sleep(music.duration)
os.remove(ttsname)

print ("2. Check your inbox")
tts = gTTS(text="option 2. Check your inbox", lang='en')
ttsname=("second.mp3")
tts.save(ttsname)

music = pyglet.media.load(ttsname, streaming = False)
music.play()

time.sleep(music.duration)
os.remove(ttsname)

print ("3. Delete your Mail")
tts = gTTS(text="option 3. Delete your Mail", lang='en')
ttsname=("second.mp3")
tts.save(ttsname)

music = pyglet.media.load(ttsname, streaming = False)
music.play()

time.sleep(music.duration)
os.remove(ttsname)

#this is for input choices
tts = gTTS(text="Please Speak Your Choice ", lang='en')
ttsname=("hello.mp3") #Example: path -> C:\Users\sayak\Desktop> just change with your desktop directory. Don't use my directory.
tts.save(ttsname)

music = pyglet.media.load(ttsname, streaming = False)
music.play()

time.sleep(music.duration)
os.remove(ttsname)




try:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        global translation11,translation1
        print ("Your choice is:")
        audio = r.record(source, duration=10)
        print("Recognizing...")
        # convert speech to text
        text=r.recognize_google(audio)
        print ("You said your choice as: "+text)
        tts = gTTS(text="You said your choice as: "+text, lang='en')
        ttsname=("hello2.mp3") #Example: path -> C:\Users\sayak\Desktop> just change with your desktop directory. Don't use my directory.
        tts.save(ttsname)

        music = pyglet.media.load(ttsname, streaming = False)
        music.play()
    
        time.sleep(music.duration)
        os.remove(ttsname)
    if text == '1' or text == 'One' or text == 'one' or text=='11':
            
            tts = gTTS(text="Please Enter Subject ", lang='en')
            ttsname=("hello.mp3") #Example: path -> C:\Users\sayak\Desktop> just change with your desktop directory. Don't use my directory.
            tts.save(ttsname)

            music = pyglet.media.load(ttsname, streaming = False)
            music.play()

            time.sleep(music.duration)
            os.remove(ttsname)
            
            r = sr.Recognizer()
            with sr.Microphone() as source:
               # global translation11,translation1
                print ("Your Subject:")
                audio = r.record(source, duration=10)
                print("Recognizing...")
                # convert speech to text
                text1=r.recognize_google(audio)
                print ("Please enter Subject: "+text1)
                tts = gTTS(text="Your Subject is: "+text1, lang='en')
                ttsname=("hello2.mp3") #Example: path -> C:\Users\sayak\Desktop> just change with your desktop directory. Don't use my directory.
                tts.save(ttsname)

                music = pyglet.media.load(ttsname, streaming = False)
                music.play()

                time.sleep(music.duration)
                os.remove(ttsname)
                
            status, messages = (None,f'SUBJECT "{text1}"')
##########################################################################################################################

            
            
####################################################################################################################################         

        
            global translation11,translation1
            TTS = gTTS(text='Please said  body of mail ')
            TTS.save("voice.mp3")
            os.system("voice.mp3")
        
            r = sr.Recognizer()
            print("Please talk")
            with sr.Microphone() as source:
             # read the audio data from the default microphone
                audio_data = r.record(source, duration=10)
                print("Recognizing...")
                # convert speech to text
                bd = r.recognize_google(audio_data)
                print("Body of mail is:"+bd)
                translator= Translator(from_lang="English",to_lang="English")
                translation1 = translator.translate(bd)
                print(translation1)
                TTS = gTTS(text=translation1)
                TTS.save("voice.mp3")
                os.system("voice.mp3")
        
            
            with sr.Microphone() as source:    
                print ("Receiver Mail ID :")
                TTS = gTTS(text='Please said  Receiver Mail id ')
                TTS.save("voice.mp3")
                os.system("voice.mp3")
                r = sr.Recognizer()
                print("Please talk")
                with sr.Microphone() as source:
               # read the audio data from the default microphone
                  audio_data = r.record(source, duration=10)
                print("Recognizing...")
                # convert speech to text
                text = r.recognize_google(audio_data)
                text = str(text+'@gmail.com')
                text = text.lower()
                text = text.replace(" ","")
                print("Mail ID is is:"+text)
                translator= Translator(from_lang="English",to_lang="English")
                translation1 = translator.translate(text)
                print(translation1)
                TTS = gTTS(text=translation1)
                TTS.save("voice.mp3")
                os.system("voice.mp3")
                From = 'voicemailsystem4@gmail.com'
                SUBJECT = text1   
                TEXT = bd
                
            # FILE = attachment
            tts = gTTS(text="You Want to attched File", lang='en')
            ttsname=("second.mp3")
            tts.save(ttsname)
            #Attachhed file 
            #choices
            print ("1. Yes")
            tts = gTTS(text="option 1.Yes.", lang='en')
            ttsname=("hello.mp3") #Example: path -> C:\Users\sayak\Desktop> just change with your desktop directory. Don't use my directory.
            tts.save(ttsname)

            music = pyglet.media.load(ttsname, streaming = False)
            music.play()

            time.sleep(music.duration)
            os.remove(ttsname)

            print ("2. No")
            tts = gTTS(text="option 2. No", lang='en')
            ttsname=("second.mp3")
            tts.save(ttsname)

            music = pyglet.media.load(ttsname, streaming = False)
            music.play()

            time.sleep(music.duration)
            os.remove(ttsname)
                
            r = sr.Recognizer()
            with sr.Microphone() as source:
               # global translation11,translation1
                print ("Enter Your Choice Yes/No:")
                audio = r.record(source, duration=10)
                print("Recognizing...")
                # convert speech to text
                text1=r.recognize_google(audio)
                print ("You said your choice as: "+text1)
                tts = gTTS(text="You said your choice as: "+text1, lang='en')
                ttsname=("hello2.mp3") #Example: path -> C:\Users\sayak\Desktop> just change with your desktop directory. Don't use my directory.
                tts.save(ttsname)

                music = pyglet.media.load(ttsname, streaming = False)
                music.play()
            
                time.sleep(music.duration)
                os.remove(ttsname)
            if text1 == 'Yes' or text1 == 'yes':
                            
                
                        def listen():
                            recognizer = sr.Recognizer()
            
                            with sr.Microphone() as source:
                                 
                                tts = gTTS(text="Please say the file name you want to send.", lang='en')
                                ttsname=("hello.mp3") #Example: path -> C:\Users\sayak\Desktop> just change with your desktop directory. Don't use my directory.
                                tts.save(ttsname)
            
                                music = pyglet.media.load(ttsname, streaming = False)
                                music.play()
            
                                time.sleep(music.duration)
                                os.remove(ttsname)
                                
                                r = sr.Recognizer()
                                with sr.Microphone() as source:
                                   # global translation11,translation1
                                    print ("Please say the file name you want to send:")
                                    audio = r.record(source, duration=10)
                                    print("Recognizing...")
                                    
                                    # convert speech to text
                                    attachment=r.recognize_google(audio)
                                    print ("Your File Name is: "+attachment)
                                    tts = gTTS(text="Your File Name is: "+attachment, lang='en')
                                    ttsname=("hello2.mp3") #Example: path -> C:\Users\sayak\Desktop> just change with your desktop directory. Don't use my directory.
                                    tts.save(ttsname)
            
                                    music = pyglet.media.load(ttsname, streaming = False)
                                    music.play()
            
                                    time.sleep(music.duration)
                                    os.remove(ttsname)
                                    
                               
                            try:
                                print("Recognizing...")
                                file_name = recognizer.recognize_google(audio)
                                print(f"File name recognized: {file_name}")
                                return file_name
                            except sr.UnknownValueError:
                                print("Could not understand the audio.")
                                return None
                            except sr.RequestError as e:
                                print(f"Error: {e}")
                                return None
            
                        def send_email(subject, body, recipient_email, file_path):
                            sender_email = 'voicemailsystem4@gmail.com'  # Replace with your email address
                            sender_password = 'Voice@123'  # Replace with your email password
            
                            msg = MIMEMultipart()
                            msg['From'] = sender_email
                            msg['To'] = recipient_email
                            msg['Subject'] = subject
                            text = body
                            
                            # Attach text message
                            msg.attach(MIMEText(text, "plain"))
            
                            # Attach selected file
                            attachment = open(file_path, 'rb')
                            part = MIMEBase('application', 'octet-stream')
                            part.set_payload(attachment.read())
                            encoders.encode_base64(part)
                            part.add_header('Content-Disposition' ,f'attachment; filename= {file_path}')
                            msg.attach(part)
            
                            # Connect to SMTP server and send email
                            server = smtplib.SMTP('smtp.gmail.com', 587)
                            server.starttls()
                            server.login(sender_email, sender_password)
                            server.sendmail(sender_email, recipient_email, msg.as_string())
                            server.quit()
            
                        # Listen for the file name via voice command
                        file_name = listen()
            
                        if file_name:
                            message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
                            file_path = f'D:/voice email system for blind people/{file_name}'+'.pdf'  # Update with your file path
                            email_subject = SUBJECT
                            email_body = TEXT
                            recipient = text  # Replace with recipient's email
            
                            send_email(email_subject, email_body, recipient, file_path)
                            
                            tts = gTTS(text="File Attached Successfully", lang='en')
                            ttsname=("hello.mp3") 
                            tts.save(ttsname)
            
                            music = pyglet.media.load(ttsname, streaming = False)
                            music.play()
            
                            time.sleep(music.duration)
                            os.remove(ttsname)
                           #send_email.close() 
                            
                           
                              
                        else:
                            print("No file name recognized. Please try again.")
            else:
                print("send mail")
                message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
                mail = smtplib.SMTP('smtp.gmail.com',587)    #host and port area
                mail.ehlo()  #Hostname to send for this command defaults to the FQDN of the local host.
                mail.starttls() #security connection
                mail.login('voicemailsystem4@gmail.com','ynck ruvf bosm zopc') #login part
                mail.sendmail(From,text,message) #send part
                print ("Congrates! Your mail has send. ")
                tts = gTTS(text="Congrates! Your mail has send ", lang='en')
                ttsname=("send.mp3") #Example: path -> C:\Users\sayak\Desktop> just change with your desktop directory. Don't use my directory.
                tts.save(ttsname)
                music = pyglet.media.load(ttsname, streaming = False)
                music.play()
                time.sleep(music.duration)
                os.remove(ttsname)
                mail.close()   
        
#########################################################################################################################
        
    if text == '2' or text == 'tu' or text == 'two' or text == 'Tu' or text == 'to' or text == 'To' or text=='22':
        mail = imaplib.IMAP4_SSL('imap.gmail.com',993) #this is host and port area.... ssl security
        #unm = ('srcdocs190@gmail.com')  #username
        #psw = ('3847@V!nodmrun@l')  #password
        mail.login('voicemailsystem4@gmail.com','ynck ruvf bosm zopc')  #login
        stat, total = mail.select('Inbox')  #total number of mails in inbox
        print ("Number of mails in your inbox :"+str(total))
        tts = gTTS(text="Total mails are :"+str(total), lang='en') #voice out
        ttsname=("total.mp3") #Example: path -> C:\Users\sayak\Desktop> just change with your desktop directory. Don't use my directory.
        tts.save(ttsname)
        music = pyglet.media.load(ttsname, streaming = False)
        music.play()
        time.sleep(music.duration)
        os.remove(ttsname)
        
        #unseen mails
        unseen = mail.search(None, 'UnSeen') # unseen count
        print ("Number of UnSeen mails :"+str(unseen))
        tts = gTTS(text="Your Unseen mail :"+str(unseen), lang='en')
        ttsname=("unseen.mp3") #Example: path -> C:\Users\sayak\Desktop> just change with your desktop directory. Don't use my directory.
        tts.save(ttsname)
        # music = pyglet.media.load(ttsname, streaming = False)
        # music.play()
        # time.sleep(music.duration)
        os.remove(ttsname)
        
        #search mails
        result, data = mail.uid('search',None, "ALL")
        inbox_item_list = data[0].split()
        new = inbox_item_list[-1]
        old = inbox_item_list[0]
        result2, email_data = mail.uid('fetch', new, '(RFC822)') #fetch
        print("email_data",email_data)
        print(result2)
        raw_email = email_data[0][1].decode("utf-8") #decode
        email_message = email.message_from_string(raw_email)
        print ("From: "+email_message['From'])
        print ("Subject: "+str(email_message['Subject']))
        tts = gTTS(text="From: "+email_message['From']+" And Your subject: "+str(email_message['Subject']), lang='en')
        ttsname=("mail.mp3") #Example: path -> C:\Users\sayak\Desktop> just change with your desktop directory. Don't use my directory.
        tts.save(ttsname)
        music = pyglet.media.load(ttsname, streaming = False)
        music.play()
        time.sleep(music.duration)
        os.remove(ttsname)
        
        #Body part of mails
        stat, total1 = mail.select('Inbox')
        stat, data1 = mail.fetch(total1[0], "(UID BODY[TEXT])")
        msg = data1[0][1]
        soup = BeautifulSoup(msg, "html.parser")
        txt = soup.get_text()
        print ("Body :"+txt)
        tts = gTTS(text="Body: "+txt, lang='en')
        ttsname=("body.mp3") #Example: path -> C:\Users\sayak\Desktop> just change with your desktop directory. Don't use my directory.
        tts.save(ttsname)
        music = pyglet.media.load(ttsname, streaming = False)
        music.play()
        time.sleep(music.duration)
        os.remove(ttsname)
        mail.close()
        mail.logout()
        
    if text == '3' or text == 'three' or text == '33':
        
        import imaplib
        import email
        from email.header import decode_header


        
        # account credentials
        username = "voicemailsystem4@gmail.com"
        password = "Voice@123"

        # create an IMAP4 class with SSL 
        imap = imaplib.IMAP4_SSL("imap.gmail.com")
        # authenticate
        #imap.login(username, password)
        imap.login('voicemailsystem4@gmail.com','ynck ruvf bosm zopc')
        # select the mailbox I want to delete in
      
        imap.select("INBOX")
       
        #this is for input choices
        tts = gTTS(text="Please Speak Your Subject ", lang='en')
        ttsname=("hello.mp3") #Example: path -> C:\Users\sayak\Desktop> just change with your desktop directory. Don't use my directory.
        tts.save(ttsname)

        music = pyglet.media.load(ttsname, streaming = False)
        music.play()

        time.sleep(music.duration)
        os.remove(ttsname)
        
        r = sr.Recognizer()
        with sr.Microphone() as source:
           # global translation11,translation1
            print ("Your Subject:")
            audio = r.record(source, duration=10)
            print("Recognizing...")
            # convert speech to text
            text=r.recognize_google(audio)
            print ("You said your Subject: "+text)
            tts = gTTS(text="You said your Subject: "+text, lang='en')
            ttsname=("hello2.mp3") #Example: path -> C:\Users\sayak\Desktop> just change with your desktop directory. Don't use my directory.
            tts.save(ttsname)

            music = pyglet.media.load(ttsname, streaming = False)
            music.play()

            time.sleep(music.duration)
            os.remove(ttsname)
            
        status, messages = imap.search(None,f'SUBJECT "{text}"')
        # to get mails after a specific date
        # status, messages = imap.search(None, 'SINCE "01-JAN-2020"')
        # to get mails before a specific date
        # status, messages = imap.search(None, 'BEFORE "01-JAN-2020"')
        # convert messages to a list of email IDs
        messages = messages[0].split()
        for mail in messages:
            _, msg = imap.fetch(mail, "(RFC822)")
            # you can delete the for loop for performance if you have a long list of emails
            # because it is only for printing the SUBJECT of target email to delete
            for response in msg:
                if isinstance(response, tuple):
                    msg = email.message_from_bytes(response[1])
                    # decode the email subject
                    subject = decode_header(msg["Subject"])[0][0]
                    if isinstance(subject, bytes):
                        # if it's a bytes type, decode to str
                        subject = subject.decode()
                    print("Deleting", subject)
            # mark the mail as deleted
            imap.store(mail, "+FLAGS", "\\Deleted")
            tts = gTTS(text="Delete Your mail successfully", lang='en')
            ttsname=("hello.mp3") 
            tts.save(ttsname)

            music = pyglet.media.load(ttsname, streaming = False)
            music.play()

            time.sleep(music.duration)
            os.remove(ttsname)
      
        imap.expunge()
        # close the mailbox
        imap.close()
        # logout from the account
        imap.logout()


except sr.UnknownValueError: 
    print("Google Speech Recognition could not understand audio.")
     
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e)) 

#choices details
