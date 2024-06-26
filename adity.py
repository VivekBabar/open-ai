import speech_recognition as sr
import pyttsx3
import subprocess

# Initialize speech recognition and text-to-speech engines
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to recognize speech
def recognize_speech():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        # Recognize speech using Google Speech Recognition for English
        text = recognizer.recognize_google(audio, language='en-US')
        print(f"You said: {text}")
        return text.lower()
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""

# Function to speak out text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Main function to run the assistant
def main():
    speak("Hello! I am your assistant. How can I help you today?")
    while True:
        # Listen for user input
        user_input = recognize_speech()

        if "exit" in user_input or "stop" in user_input:
            speak("Goodbye!")
            break
        elif "jarvis" in user_input:
            if "open chrome" in user_input:
                speak("Opening Google Chrome")
                subprocess.Popen(["C:/Program Files/Google/Chrome/Application/chrome.exe"])
            elif "open notepad" in user_input:
                speak("Opening Notepad")
                subprocess.Popen(["notepad.exe"])
            else:
                speak("I'm sorry, I didn't understand that.")
        else:
            speak("I'm sorry, I didn't catch the keyword 'Jarvis'. Could you repeat?")

if __name__ == "__main__":
    main()
