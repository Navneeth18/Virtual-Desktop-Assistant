import os
import pyautogui
import webbrowser
from main import *
from time import sleep


# list of applications
dictapp = {
    "commandprompt": "cmd",
    "paint": "paint",
    "vscode": "code",
    "word": "winword",
    "excel": "excel",
    "powerpoint": "powerpnt",
    "notepad": "notepad",
    "chrome": "chrome",  # Assuming you use Chrome
    "brave": "brave",
    "fileexplorer": "explorer",
    "taskmanager": "taskmgr",
    "calculator": "calculator",
    "snippingtool": "snippingtool",
    "mspaint": "mspaint",
    "msconfig": "msconfig",
    "firefox": "firefox",
    "teams": "teams",
    "outlook": "outlook",
    "spotify": "spotify",
    "steam": "steam",
    "taskview": "taskview",
    "settings": "ms-settings",
}

# opens websites and applications
def openAppWeb(query):
    speak("launching, sir")
    if ".com" in query or " .co.in" in query or ".org" in query or ".net" in query:
        query = query.replace("open","")
        query = query.replace("jarvis","")
        query = query.replace("launch","")
        query = query.replace(" ","")
        webbrowser.open(f"https://www.{query}")
    else:
        query = query.replace("open","")
        keys = list(dictapp.keys())
        for app in keys: 
            if app in query:
                os.system(f"start {dictapp[app]}")
            
                
# closes websites and applications
def closeappweb(query):
    speak("Closing sir")
    if "one tab" in query or "1 tab" in query:
        pyautogui.hotkey("ctrl","w")
    elif "2 tabs" in query or "two tabs" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("All tabs closed") 
    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"taskkill /f /im {dictapp[app]}.exe")
