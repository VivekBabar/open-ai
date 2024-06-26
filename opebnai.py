import os
import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import requests
import random

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

# Category: System Control
def shutdown_computer():
    speak("Shutting down the computer")
    os.system("shutdown /s /t 1")

def restart_computer():
    speak("Restarting the computer")
    os.system("shutdown /r /t 1")

def lock_computer():
    speak("Locking the computer")
    os.system("rundll32.exe user32.dll,LockWorkStation")

# Category: Web Search
def search_google(query):
    try:
        webbrowser.open(f"https://www.google.com/search?q={query}")
        speak(f"Searching Google for: {query}")
    except Exception as e:
        speak(f"Error searching Google: {e}")

def open_youtube():
    try:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube")
    except Exception as e:
        speak(f"Error opening YouTube: {e}")

# Category: Entertainment
def tell_joke():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "What do you get when you cross a snowman and a vampire? Frostbite."
    ]
    joke = random.choice(jokes)
    speak(joke)

def play_music():
    speak("Playing music")
    webbrowser.open("https://music.youtube.com")

# Category: Information Retrieval
def tell_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M")
    speak(f"The current time is {current_time}")

def tell_date():
    today = datetime.date.today()
    speak(f"Today's date is {today}")

def get_weather(city):
    api_key = "your_openweather_api_key"  # Replace with your OpenWeather API key
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(base_url)
        data = response.json()
        if data["cod"] != "404":
            main = data["main"]
            weather_desc = data["weather"][0]["description"]
            temperature = main["temp"]
            speak(f"The weather in {city} is currently {weather_desc} with a temperature of {temperature} degrees Celsius.")
        else:
            speak("City not found.")
    except Exception as e:
        speak(f"Error getting weather information: {e}")

def get_news():
    api_key = "your_newsapi_api_key"  # Replace with your News API key
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
    try:
        response = requests.get(url)
        news_data = response.json()
        articles = news_data["articles"]
        speak("Here are the latest news headlines:")
        for article in articles[:5]:  # Read out the first 5 headlines
            speak(article["title"])
    except Exception as e:
        speak(f"Error getting news: {e}")

# Category: Productivity Tools
def set_timer(duration):
    speak(f"Setting a timer for {duration} seconds")
    os.system(f"timeout /t {duration}")

def add_reminder(reminder):
    speak(f"Reminder set: {reminder}")

# Category: Smart Home Control
def control_lights(action):
    speak(f"{action} the lights")

# Category: Communication
def send_email(recipient, subject, body):
    speak(f"Sending email to {recipient}")
    # Placeholder for email sending functionality

def send_sms(number, message):
    speak(f"Sending SMS to {number}")
    # Placeholder for SMS sending functionality

# Category: Social Media
def check_facebook_notifications():
    speak("Checking Facebook notifications")
    # Placeholder for Facebook notifications checking

# Category: Finance
def get_stock_price(ticker):
    speak(f"Getting stock price for {ticker}")
    # Placeholder for stock price retrieval

def convert_currency(amount, from_currency, to_currency):
    speak(f"Converting {amount} {from_currency} to {to_currency}")
    # Placeholder for currency conversion

# Category: Health & Fitness
def start_workout(workout_type):
    speak(f"Starting {workout_type} workout")
    # Placeholder for workout starting functionality

def get_nutrition_info(food):
    speak(f"Getting nutrition information for {food}")
    # Placeholder for nutrition information retrieval

# Category: Shopping
def add_to_cart(item):
    speak(f"Adding {item} to the cart")
    # Placeholder for adding item to shopping cart

def checkout():
    speak("Checking out")
    # Placeholder for checkout functionality

# Category: Education
def get_definition(word):
    speak(f"Getting definition of {word}")
    # Placeholder for word definition retrieval

def translate_text(text, target_language):
    speak(f"Translating text to {target_language}")
    # Placeholder for text translation

# Category: Reminders
def set_alarm(time):
    speak(f"Setting an alarm for {time}")
    # Placeholder for alarm setting

def create_event(event_details):
    speak(f"Creating event: {event_details}")
    # Placeholder for event creation

# Function to handle unsupported commands
def unsupported_command():
    speak("Sorry, I didn't understand that command.")

# Main function to map commands to functions
def main():
    # Mapping commands to functions
    commands = {
        "shutdown computer": shutdown_computer,
        "restart computer": restart_computer,
        "lock computer": lock_computer,
        "search google for": search_google,
        "open youtube": open_youtube,
        "tell a joke": tell_joke,
        "play music": play_music,
        "what time is it": tell_time,
        "what is the date": tell_date,
        "weather in": get_weather,
        "news": get_news,
        "set a timer for": set_timer,
        "add reminder": add_reminder,
        "turn on lights": lambda: control_lights("Turning on"),
        "turn off lights": lambda: control_lights("Turning off"),
        "send email to": send_email,
        "send sms to": send_sms,
        "check facebook notifications": check_facebook_notifications,
        "stock price of": get_stock_price,
        "convert currency": convert_currency,
        "start workout": start_workout,
        "nutrition info for": get_nutrition_info,
        "add to cart": add_to_cart,
        "checkout": checkout,
        "define": get_definition,
        "translate": translate_text,
        "set alarm for": set_alarm,
        "create event": create_event
    }

    speak("Hello! I am your assistant. How can I help you today?")
    while True:
        user_input = recognize_speech()

        if "exit" in user_input or "stop" in user_input:
            speak("Goodbye!")
            break

        # Find the command in the dictionary and execute it
        command_found = False
        for command in commands:
            if command in user_input:
                command_found = True
                if "search google for" in user_input:
                    query = user_input.replace("search google for", "").strip()
                    commands[command](query)
                elif "weather in" in user_input:
                    city = user_input.replace("weather in", "").strip()
                    commands[command](city)
                elif "set a timer for" in user_input:
                    duration = int(user_input.replace("set a timer for", "").strip())
                    commands[command](duration)
                elif "send email to" in user_input:
                    parts = user_input.replace("send email to", "").strip().split(" subject ")
                    recipient = parts[0].strip()
                    subject, body = parts[1].split(" body ")
                    commands[command](recipient.strip(), subject.strip(), body.strip())
                elif "send sms to" in user_input:
                    parts = user_input.replace("send sms to", "").strip().split(" message ")
                    number = parts[0].strip()
                    message = parts[1].strip()
                    commands[command](number, message)
                elif "stock price of" in user_input:
                    ticker = user_input.replace("stock price of", "").strip()
                    commands[command](ticker)
                elif "define" in user_input:
                    word = user_input.replace("define", "").strip()
                    commands[command](word)
                elif "translate" in user_input:
                    parts = user_input.replace("translate", "").strip().split(" to ")
                    text = parts[0].strip()
                    target_language = parts[1].strip()
                    commands[command](text, target_language)
                elif "set alarm for" in user_input:
                    time = user_input.replace("set alarm for", "").strip()
                    commands[command](time)
                elif "create event" in user_input:
                    event_details = user_input.replace("create event", "").strip()
                    commands[command](event_details)
                else:
                    commands[command]()
                break

        if not command_found:
            unsupported_command()

if __name__ == "__main__":
    main()

