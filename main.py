import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import wikipedia
import pywhatkit as kit
import os
import sys
import cv2
import smtplib
import pyjokes
import requests
import Desktop_file
import subprocess
import musicLibrary
import MyAlarm
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


recognizer = sr.Recognizer()
ttsx = pyttsx3.init()

def speak(text):
    ttsx.say(text)
    ttsx.runAndWait()

def wish():
     hour = int(datetime.datetime.now().hour)
     if hour >= 0 and hour < 12:
          speak("Good Morning!")
          print("Good Morning!")

     elif hour >= 12 and hour < 18:
          speak("Good Afternoon!")
          print("Good Afternoon!")      
     else:
          speak("Good Evening!")
          print("Good Evening!")
def takecommand():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print(f"User said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        print("Could not understand audio")
        return ""
    except sr.RequestError:
        print("Could not request results")
        return ""

newsapi = "5b857d0eead467c9bd1231d8f3efc24"  
def sendEmail(to, content):

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("hellochirag3@gmail.com", "Chirag#1970")
    server.sendmail("hellochirag3@gmail.com", to, content)
    server.close()
    


def processCommand(c):
    if "open google" in c.lower():
        speak("Opening Google")
        print("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "open youtube" in c.lower():
        speak("Opening Youtube")
        webbrowser.open("https://www.youtube.com")  
    elif "open facebook" in c.lower():
        speak("Opening Facebook")       
        webbrowser.open("https://www.facebook.com") 
    elif "open whatsapp" in c.lower():
        speak("Opening Whatsapp")       
        webbrowser.open("https://web.whatsapp.com/")
    elif "open instagram" in c.lower():
        speak("Opening Instagram")       
        webbrowser.open("https://www.instagram.com/")
    elif "open twitter" in c.lower():
        speak("Opening Twitter")       
        webbrowser.open("https://twitter.com/")
    elif "open linkedin" in c.lower():
        speak("Opening Linkedin")       
        webbrowser.open("https://www.linkedin.com/")  
    elif "alram" in c.lower:
        speak("Sir please tell me the time to set the alarm to 5:30 am")
        tt = takecommand()
        tt = tt.replace("set alarm to", "")
        tt = tt.replace(".", "")
        tt = tt.upper()

        MyAlarm

    
    elif "search google" in c.lower():
        print(command)
        speak (command)
        r = c.lower().split(" ")[2]
        r = " ".join(c.lower().split(" ")[2:])
        print(r)
        webbrowser.open(f"https://www.google.com/search?q={r}")    

# search wikipedia
    elif "search wikipedia" in c.lower():
        print(command)
        speak (command)
        r = c.lower().split(" ")[2]
        r = " ".join(c.lower().split(" ")[2:])
        print(r)
        result = wikipedia.summary(r,sentences=3)
        print (result)
        speak (result)

    elif "play song on youtube" in c.lower():
        kit.playonyt("Namo Namah Shivay")

    elif "play music" in c.lower():
        music_dir = "C:\\Users\\HP\\Music"
        songs = os.listdir(music_dir)
        os.startfile(os.path.join(music_dir, songs[0]))
        for song in songs:
            if song.endswith(".mp3"):
                os.startfile(os.path.join(music_dir, song))

    elif c.lower().startswith("play"):

        print(command)
        song = c.lower().split(" ")[1]
        print(command)
        link = musicLibrary.music[song]
        webbrowser.open(link)

    elif "file" in c.lower():
        print(c)
        r = c.lower().split(" ")[1]
        # r = " ".join(c.lower().split(" ")[2:])
        print(r)

        if r in Desktop_file.file:
            link = Desktop_file.file[r]
            print(f"Opening {link}")
            speak(f"Opening {r}")
            try:
                subprocess.Popen([link], shell=True)
            except Exception as e:
                print(f"Failed to open {link}: {e}")
                speak(f"Failed to open {r}")
        else:
            speak(f"File {r} not found in the desktop file library")

#     elif "open notepad" in c.lower():
#         speak("Opening Notepad")
#         npath = "C:\\Users\\HP\\OneDrive\\Desktop\\notepad.exe"
        
#         os.startfile("npath")

# non testing cases
    # elif "open command prompt" in c.lower():
    #     speak("Opening Command Prompt")
    #     os.system("start cmd")


#     elif "open camera" in c.lower():
#         speak("Opening Camera")
#         # os.system("start microsoft.windows.camera:")
#         cap = cv2.VideoCapture(0)
#         if not cap.isOpened():
#             speak("Camera is not available")
#             print("Camera is not available")
#         else:
#             speak("Camera is opened")
#             print("Camera is opened")
#             while True:
#                 ret, frame = cap.read()
#                 cv2.imshow('Camera', frame)


#                 # if cv2.waitKey(1) & 0xFF == ord('q'):
#                 #     break
#                 k = cv2.waitKey(50)

#                 if k == 27:  # Press 'Esc' to exit
#                     break
#         cap.release()
#         cv2.destroyAllWindows()


#     elif "send message on whatsapp" in c.lower():
#         kit.sendwhatmsg("+917027968174", "Hello", 2, 25)
        
#     elif "no thanks" in c.lower():
#         speak("Okay, have a nice day!")
#         sys.exit()

#     elif "close notepad" in c.lower():
#         speak("Closing Notepad")
#     #     os.system("taskkill /f /im notepad.exe")
#     # elif "set alarm" in c.lower():
#         # speak("Please tell me the time to set the alarm")
#         # with sr.Microphone() as source:
#         #     audio = recognizer.listen(source)
#         #     time = recognizer.recognize_google(audio)
#         #     print(f"Alarm set for {time}")
#         #     speak(f"Alarm set for {time}")
#         # nn = int(datetime.datetime.now().hour)
#         # if nn == 22:
#         #     music_dir = "C:\\Users\\HP\\Music"
#         #     songs = os.listdir(music_dir)
#         #     os.startfile(os.path.join(music_dir, songs[0]))
#         # speak("Alarm set for 10 PM")

#     elif "tell me a joke" in c.lower():
#         joke = pyjokes.get_joke()
#         speak(joke)
    
#     elif "shut down" in c.lower():
#         os.system("shutdown /s /t 5")
    
#     elif "restart" in c.lower():
#         os.system("shutdown /r /t 5")
    
#     elif "sleep" in c.lower():
#         os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

#     elif c.lower().startswith("news"):

#         print("Getting News")
#         r = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=e5b857d0eead467c9bd1231d8f3efc24")

#         if r.status_code == 200:
#             data = r.json()
#             articles = data.get('articles', [])
#             for article in articles[:10]:  # Limit to the first 5 articles
#                 print(article['title'])
#                 speak(article['title'])
#                 speak("Moving to the next news")
#         else:
#             speak("Sorry, I couldn't fetch the news at the moment.")

#     elif "can you calculate" in c.lower():
#         speak("Sure, please tell me the calculation you want to perform")
#         r = sr.Recognizer()
#         with sr.Microphone() as source:
#             print("Listening for calculation...")
#             r.adjust_for_ambient_noise(source)
#             audio = r.listen(source)
#         my_string = r.recognize_google(audio)
#         print(f"You said: {my_string}")
#         def get_operator_fn(op):
#             return {
#                 '+' : operator.add,
#                 '-' : operator.sub,
#                 'x' : operator.mul,
#                 '/' : operator.truediv
#             }[op]
#         def eval_binary_expr(op1, oper, op2):
#             op1, op2 = int(op1), int(op2)
#             return get_operator_fn(oper)(op1, op2)
#         speak("Your result is: ")
#         speak(eval_binary_expr(*(my_string.split())))
#         speak("Here is the result of your calculation")



           
    # elif "email to chirag" in c.lower():
    #     speak("Sir, what should I say?")
    #     c.lower() = takecommand().lower()
    #     if "send email" in c.lower():
    #         email_content = "hellochirag3@gmail.com"
    #         password = "Chirag#1970"
    #         to = "chiragns2002@gmail.com"

    #         speak("What is the subject of the email?")
    #         subject = takecommand().lower()
    #         speak("What is the content of the email?")
    #         content = takecommand().lower()
    #         speak ("Enter the file path to attach the file")
    #         file_path = input("Enter the file path to attach the file: ")
    #         speak("Sending email")

    #         msg = MIMEMultipart()
    #         msg['From'] = email_content
    #         msg['To'] = to
    #         msg['Subject'] = subject
    #         msg.attach(MIMEText(content, 'plain'))
    #         filename = os.path.basename(file_path)
    #         attachment = open(file_path, "rb")
    #         part = MIMEBase('application', 'octet-stream')
    #         part.set_payload(attachment.read())
    #         encoders.encode_base64(part)
    #         part.add_header('Content-Disposition', f'attachment; filename={filename}')
    #         msg.attach(part)

    #         server = smtplib.SMTP('smtp.gmail.com', 587)
    #         server.ehlo()
    #         server.starttls()
    #         server.login("hellochirag3@gmail.com", "Chirag#1970")
    #         server.sendmail("hellochirag3@gmail.com", to, content)
    #         server.close()

    #     else:
    #         email_content = "hellochirag3@gmail.com"
    #         password = "Chirag#1970"
    #         to = "chiragns2002@gmail.com"

    #         server = smtplib.SMTP('smtp.gmail.com', 587)
    #         server.ehlo()
    #         server.starttls()
    #         server.login("hellochirag3@gmail.com", "Chirag#1970")
    #         server.sendmail("hellochirag3@gmail.com", to, content)
    #         server.close()
    #     try:
    #         speak("What should I say?")
    #         content = takecommand().lower()
    #         to = "chiragns2002@gmail.com"
    #         sendEmail(to, content)
    #     except Exception as e:
    #         print(e)
    #         speak("Sorry, I am not able to send this email")




# main function
if __name__ == "__main__":  

    print("Program Started")
    wish()

    speak("Initializing Shivaa like as Jarvis......")
    print("Initializing Shivaa like as Jarvis.......")

    while True:
    # Listen for the wake word "Jarvis"
        r = sr.Recognizer()
        print ("recognizing....")

        try:
            with sr.Microphone() as source:
                print("Listening......")
                audio = r.listen(source, timeout=5, phrase_time_limit=5)

            word = r.recognize_google(audio)

            if (word.lower() == "shiva"):                   
                    speak("Yes, I am here. How can I help you?")

                    with sr.Microphone() as source:
                        print("Shiva Active........")
                        audio = r.listen(source)
                        command = r.recognize_google(audio)
                        processCommand(command)

                  
        except Exception as e:
            print("Error;{0} " .format(e))
            print("Please try again, I didn't understand that.")
