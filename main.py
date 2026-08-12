import sounddevice as sd
import soundfile as sf
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os

# Text to speech
engine = pyttsx3.init()


def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()


def listen():
    duration = 5
    sample_rate = 44100

    print("Listening...")

    # Record voice using sounddevice
    recording = sd.rec(
        int(duration * sample_rate),
        samplerate=sample_rate,
        channels=1,
        dtype="float32"
    )

    sd.wait()

    # Save recording
    sf.write("voice.wav", recording, sample_rate)

    # Recognize voice
    recognizer = sr.Recognizer()

    with sr.AudioFile("voice.wav") as source:
        audio = recognizer.record(source)

    try:
        command = recognizer.recognize_google(audio)

        print("You:", command)

        return command.lower()

    except sr.UnknownValueError:
        speak("Sorry, I could not understand you.")
        return ""

    except sr.RequestError:
        speak("Please check your internet connection.")
        return ""


def run_assistant():

    speak("Hello! I am your voice assistant.")
    speak("How can I help you?")

    while True:

        command = listen()

        if command == "":
            continue

        # Greeting
        if "hello" in command or "hi" in command:
            speak("Hello! How are you?")

        # How are you
        elif "how are you" in command:
            speak("I am fine. Thank you for asking.")

        # Time
        elif "time" in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak("The current time is " + current_time)

        # Date
        elif "date" in command:
            current_date = datetime.datetime.now().strftime("%d %B %Y")
            speak("Today's date is " + current_date)

        # Google
        elif "open google" in command:
            speak("Opening Google.")
            webbrowser.open("https://www.google.com")

        # YouTube
        elif "open youtube" in command:
            speak("Opening YouTube.")
            webbrowser.open("https://www.youtube.com")

        # Search
        elif "search" in command:

            speak("What should I search for?")

            search = listen()

            if search != "":
                speak("Searching for " + search)

                url = "https://www.google.com/search?q=" + search
                webbrowser.open(url)

        # Play music
        elif "play music" in command or "play song" in command:

            speak("Opening YouTube Music.")
            webbrowser.open("https://music.youtube.com")

        # Calculator
        elif "open calculator" in command:

            speak("Opening calculator.")

            os.system("calc")

        # Notepad
        elif "open notepad" in command:

            speak("Opening notepad.")

            os.system("notepad")

        # Exit
        elif "exit" in command or "quit" in command or "goodbye" in command:

            speak("Goodbye! See you later.")
            break

        else:
            speak("Sorry, I don't know that command yet.")


run_assistant()