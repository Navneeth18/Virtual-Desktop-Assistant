import os
import pyttsx3
import speech_recognition as sr
import requests
from bs4 import BeautifulSoup
import datetime
from playsound import playsound
import pyautogui
import webbrowser

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 210)

# speaker/output voice function
def speak(text):
    engine.say(text)
    engine.runAndWait()

# microphone/input voice function
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        text = r.listen(source,0,4)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(text, language='en-in')
        print(f"you said: {query}\n")
    except Exception as e:
        print("can you please say that again")
        return "none"
    return query

# playing audio
def playInitializeSound():
    music_dir = "assets\\audio\\start-sound1.mp3"
    playsound(music_dir)

def playAssistantSound():
    music_dir = "assets\\audio\\jarvis-audio.mp3"
    playsound(music_dir)




# main function
if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            playInitializeSound()
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()

                # the program runs but it wont respond, it is in sleep mode, to activate it say "wake up".
                if "go to sleep" in query:
                    speak("Ok Sir, You can call me anytime")
                    playAssistantSound()
                    break
                
                # simple conversation
                elif "hello" in query:
                    speak("Hello Sir, how are You ?")
                elif "i am fine" in query:
                    speak("that's great sir")
                elif "how are you" in query:
                    speak("Perfect, Sir")
                elif "thank You" in query:
                    speak("you are Welcome, Sir")
                
                # youtube controls 
                elif "pause video" in query:
                    pyautogui.press("k")
                elif "play video" in query:
                    pyautogui.press("k")
                elif "mute video" in query:
                    pyautogui.press("m")
                    speak("video muted")
                elif "full screen" in query:
                    pyautogui.press("f")
                elif "small screen" in query:
                    pyautogui.press("f")
                
                # screenshot "it takes ss and saves the file in the current directory as 'ss.jpg', next time when we take ss current ss is deleated "
                elif "screenshot" in query:
                    im = pyautogui.screenshot()
                    im.save("ss.jpg")

                # taking photos through camera
                elif "click my photo" in query:
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(2)
                    speak("SMILE")
                    pyautogui.press("enter")

                
                # accessing eduprime(student portal) of college(VNR VJIET)
                elif "college website" in query:
                    web = "https://automation.vnrvjiet.ac.in/eduprime3"
                    webbrowser.open(web)
                    pyautogui.press("enter") #incase we have saved passwords it will hit "enter" and page opens automatically
                    
                # opening desktop applications by searching on windows search
                elif "open" in query:
                    query = query.replace("open","")
                    query = query.replace("jarvis","")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.sleep(2)
                    pyautogui.press("enter")
                
                # closing the current workspace
                elif "clear" in query:
                    query = query.replace("jarvis","")
                    pyautogui.hotkey("alt","f4")
                    speak("done, sir")

                # opening websites and desktop applications
                elif "open" in query:
                    from DictApp import openAppWeb
                    openAppWeb(query)
                    playAssistantSound()

                # for closing all tabs of the active window
                elif "close all tabs" in query:
                    pyautogui.hotkey("alt","f4")
                    speak("all tabs closed")
                
                # for closing the active websites and desktop applications
                elif "close" in query:
                    from DictApp import closeappweb
                    closeappweb(query)
                    playAssistantSound()

                # searching on google
                elif "google" in query:
                    from SearchNow import searchGoogle
                    playAssistantSound()
                    searchGoogle(query)
                    
                    
                # search and play onyoutube
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    playAssistantSound()
                    searchYoutube(query)


                # WhatsApp automation - send messages directly through voice commands by entering the reciever's mobile number
                elif "whatsapp" in query:
                    print("In whatsApp...")
                    from Whatsapp import send_whatsapp_message
                    send_whatsapp_message()

                # tells the temperature // to use say- 'what's the temperature in {any city}'
                elif "temperature" in query:
                    query = query.replace("jarvis","")
                    query = query.replace("what is the","")
                    query = query.replace("what's the","")
                    url = f"https://www.google.com/search?q={query}"
                    req = requests.get(url) 
                    data = BeautifulSoup(req.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    playAssistantSound()
                    speak(f"current {query} is {temp}")   

                # tells the current time in 24hour format
                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"sir, the time is {strTime}")
                
                
                # voice commands for exit or terminating the program
                elif "finally sleep" in query:
                    speak("shutting down, sir")
                    playInitializeSound()
                    exit()
                elif "turn off" in query: 
                    speak("shutting down, sir")
                    playInitializeSound()
                    exit()
                elif "end program" in query:
                    speak("shutting down, sir")
                    playInitializeSound()
                    exit()
                elif "exit" in query:
                    speak("shutting down, sir")
                    playInitializeSound()
                    exit()



                
                





