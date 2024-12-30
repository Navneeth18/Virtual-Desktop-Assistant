from main import *
import pywhatkit
import webbrowser

query = takeCommand().lower()

# opens browser and search on google
def searchGoogle(query):
    if "google" in query:
        import wikipedia as googleScrap
        query = query.replace("jarvis","")
        query = query.replace("google","")
        speak("This is what I found on google")

        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query,1)
            speak(result)
        except:
            speak("No Output available")

# opens youtube on browser and search
def searchYoutube(query):
    if "youtube" in query:
        speak("This is what I found on youtube")
        # speak("This is what I found")
        query = query.replace("open","")
        query = query.replace("youtube","")
        query = query.replace("jarvis","")
        query = query.replace("search","")
        web = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("Done, Sir")

