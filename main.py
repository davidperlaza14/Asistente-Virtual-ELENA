import requests
import pyttsx3
from decouple import config
from datetime import  datetime
import speech_recognition as sr
from random import choice
from utils import opening_text
from functions.online_ops import *
from functions.os_ops import *
from pprint import pprint


USERNAME = config('USER')
BOTNAME = config('BOTNAME')

def speak(text):
    engine = pyttsx3.init('espeak')
    engine.say(text)
    engine.runAndWait()

def greet_user():
    """Greets the user according to the time"""
    speak(f"Hello {USERNAME}, how are you today?")


# Text to Speech Conversion
# def speak(text):
#     """Used to speak whatever text is passed to it"""
#     engine.say(text)
#     engine.runAndWait()



from datetime import datetime

def greet_user():
    """Greets the user according to the time"""
    current_time = datetime.now()
    hour = current_time.hour
    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        speak(f"Good Morning {USERNAME}")
    elif (hour >= 12) and (hour < 16):
        speak(f"Good afternoon {USERNAME}")
    elif (hour >= 16) and (hour < 19):
        speak(f"Good Evening {USERNAME}")
    speak(f"I am {BOTNAME}. How may I assist you?")



# How to Take User Input
def take_user_input():
    """Takes user input, recognizes it using Speech Recognition module and converts it into text"""
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-US').lower()
        
        if 'hello' in query or 'how are you' in query or 'hi' in query:
            speak("I'm fine, thank you")
        
        if 'exit' not in query and 'stop' not in query:
            speak(choice(opening_text))
        else:
            hour = datetime.now().hour
            if 6 >= hour > 21:
                speak("Good night sir, take care!")
            else:
                speak('Have a good day sir!')
            exit()
    except Exception:
        speak('Sorry, I could not understand. Could you please say that again?')
        query = 'None'
    return query


if __name__ == '__main__':
    greet_user()
    while True:
        query = take_user_input().lower()
        
        if 'open note' in query:
            open_notepad()
        
        elif 'open command promprt' in query or 'open cmd' in query or 'open terminal' in query:
            open_terminal()
        
        elif 'open pomodoro' in query:
            open_pomodoro()
        
        elif 'open clocks' in query:
            open_clocks()
        
        elif 'open camera' in query:
            open_camera()
        
        elif 'open calculator' in query:
            open_calculator()
        
        elif 'open google' in query:
            open_google()
            
        elif 'open firefox' in query:
            open_firefox()
        
        elif 'ip address' in query:
            ip_address = find_my_ip()
            speak(f'Your IP Address is {ip_address}.\n For your convenience, I am printing it on the screen sir.')
            print(f'Your IP Address is {ip_address}')
        
        elif 'wikipedia' in query:
            speak('What do you want to search on Wikipedia, sir')
            search_query = take_user_input().lower()
            results = search_on_wikipedia(search_query)
            speak(f"According to Wikipedia, {results}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(results)
        
        elif 'youtube' in query:
            speak('What do you want to play on Youtube, sir?')
            video = take_user_input().lower()
            play_on_youtube(video)
        
        elif 'google' in query:
            speak('What do you want to search on Google,  sir?')
            query = take_user_input().lower()
            search_on_google(query)
        
        elif "send whatsapp message" in query:
            speak(
                'On what number should I send the message sir? Please enter in the console: ')
            number = input("Enter the number: ")
            speak("What is the message sir?")
            message = take_user_input().lower()
            send_whatsapp_message(number, message)
            speak("I've sent the message sir.")
        
        elif "send an email" in query:
            speak("On what email address do I send sir? Please enter in the console: ")
            receiver_address = input("Enter email address: ")
            speak("What should be the subject sir?")
            subject = take_user_input().capitalize()
            speak("What is the message sir?")
            message = take_user_input().capitalize()
            if send_email(receiver_address, subject, message):
                speak("I've sent the email sir.")
            else:
                speak("Something went wrong while I was sending the mail. Please check the error logs sir.")
        
        elif 'joke' in query:
            speak(f"Hope you this like one sir")
            joke = get_random_joke()
            speak(joke)
            speak("For your convenience, I am printing it on the screen sir.")
            pprint(joke)
            
        elif "advice" in query:
            speak(f"Here's an advice for you, sir")
            advice = get_random_advice()
            speak(advice)
            speak("For your convenience, I am printing it on the screen sir.")
            pprint(advice)
        
        elif "trending movies" in query:
            speak(f"Some of the trending movies are: {get_trending_movies()}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(*get_trending_movies(), sep='\n')
        
        elif 'news' in query:
            speak(f"I'm reading out the latest news headlines, sir")
            speak(get_latest_news())
            speak("For your convenience, I am printing it on the screen sir.")
            print(*get_latest_news(), sep='\n')
        
        elif 'weather' in query:
            ip_address = find_my_ip()
            city = requests.get(f"https://ipapi.co/{ip_address}/city/")
            speak(f"Getting weather report for your {city}")
            weather, temperature, feels_like = get_weather_report(city)
            speak(f"The current temperature is {temperature}, but it feels like {feels_like}")
            speak(f"Also, the weather report talks about {weather}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(f"Description: {weather}\nTemperature: {temperature}\nFeels like: {feels_like}")