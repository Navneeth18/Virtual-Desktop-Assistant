import pywhatkit as kit
import speech_recognition as sr
import pyttsx3

import webbrowser
from time import sleep
import os
import pyautogui

'''
This script automates sending WhatsApp messages using voice commands. 
It captures the user's input through speech recognition and sends the message instantly via pywhatkit.
After sending the message, the message and timestamps are recorded in the 'pyWhatKit_DB.txt' file.
'''

# Initialize text-to-speech engine
engine1 = pyttsx3.init()
engine1.setProperty('rate', 150)

# speech output function
def speak1(text):
    engine1.say(text)
    engine1.runAndWait()

# speech input function
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening from whatsapp...")
        try:
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio)
            return command.lower()
        except sr.UnknownValueError:
            speak1("Sorry, I didn't understand that. Could you please repeat?")
            return None

# Main function for automation
def send_whatsapp_message():
    speak1("To whom should I send the WhatsApp message? Please enter the phone number.")
    phone_number = input("enter number: ")
    if phone_number:
        speak1("What message would you like to send?")
        print("message...")
        message = listen()
        if message:
            try:
                
                # schedule the message
                kit.sendwhatmsg_instantly(f"+91{phone_number}",message)
                speak1("Message scheduled successfully! waiting for it to send.")
                # waits for 1 sec till the website loads
                sleep(1)
                pyautogui.press("enter") # in case it dont send message it only type and wait this line will press "enter" and send message
                speak1("Message sent successfully!")

                
            except ValueError:
                speak1("Invalid time format. Please provide valid numbers for the hour and minute.")
        else:
            speak1("No message received.")
    else:
        speak1("No phone number received.")

