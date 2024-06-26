import speech_recognition as sr
import pyttsx3
import webbrowser

# Initialize speech recognition and text-to-speech engines
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to recognize speech
def recognize_speech():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
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
    speak("Hello! I am your assistant. How can I help you today vivek sir ?")
    while True:
        # Listen for user input
        user_input = recognize_speech()

        if "exit" in user_input or "stop" in user_input:
            speak("Goodbye vivek your day go to beter!")
            break
        elif "open youtube" in user_input:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")
            
        elif "open google" in user_input:
            speak("Opening google")
            webbrowser.open("https://www.google.com")
            
        elif "how are you" in user_input:
            speak("I'm fine, thank you!") 
            
        elif "open porn" in user_input:
            speak("Opening porn")
            webbrowser.open("https://www.xhamster.com")        
            
               
        else:
            speak("I'm sorry, I didn't understand that.")

if __name__ == "__main__":
    main()
