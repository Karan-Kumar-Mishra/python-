import pyttsx3  # Text-to-speech library
import speech_recognition as sr  # Speech recognition library
import datetime
import wikipedia
import webbrowser
import os


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def greet():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am Jarvis. How can I assist you?")


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")
    except Exception as e:
        print("Sorry, I couldn't understand. Can you please repeat that?")
        return None
    return query


def process(query):
    if query:
        query = query.lower()
        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia...")
            print(results)
            speak(results)
        elif "open youtube" in query:
            webbrowser.open("https://www.youtube.com")
        elif "open google" in query:
            webbrowser.open("https://www.google.com")
        elif "play music" in query:
            music_dir = "C:/Path/To/Your/Music/Folder"
            songs = os.listdir(music_dir)
            if songs:
                os.startfile(os.path.join(music_dir, songs[0]))
        elif "what time is it" in query:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The current time is {current_time}")
        else:
            speak("I'm sorry, I can't perform that task.")


if __name__ == "__main__":
    greet()
    while True:
        query = listen()
        process(query)
