from main import *
import datetime

# greets according to the current time
def greetMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour<=12:
        speak("Good Morning, Navneeth")
    elif hour >12 and hour<=16:
        speak("Good Evening, Navneeth")
    elif hour >16 and hour <=18:
        speak("Good Evening, Navneeth")
    else:
        speak("Good Evening, Navneeth")
    
    speak("How can I help you ?")


