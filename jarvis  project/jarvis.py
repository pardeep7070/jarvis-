import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser

engine = pyttsx3.init()

# Speak Function
def speak(text):
    print("heydeep:", text)
    engine.say(text)
    engine.runAndWait()

# Listen Function
def listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        command = r.recognize_google(audio)
        print("You:", command)
        return command.lower()

    except:
        return ""

# Wish User
def wish():
    hour = datetime.datetime.now().hour

    if hour < 12:
        speak("Good Morning")
    elif hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("I am deep. How can I help you?")

wish()

while True:

    command = listen()

    if "hello" in command:
        speak("Hello, how are you?")

    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak("Current time is " + time)

    elif "google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "exit" in command or "bye" in command:
        speak("Goodbye")
        break 
