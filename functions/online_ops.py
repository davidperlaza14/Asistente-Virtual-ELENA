import requests
import wikipedia
import pywhatkit as kit
import datetime
from email.message import EmailMessage
import smtplib
from decouple import config


def find_my_ip():
    ip_address = requests.get('https://api.ipify.org?format=json').json()
    return ip_address['ip']

def search_on_wikipedia(query):
    results = wikipedia.summary(query, sentences=2)
    return results

def play_on_youtube(video):
    kit.playonyt(video)

def search_on_google(query):
    kit.search(query)

def send_whatsapp_message(number, message):
    now = datetime.datetime.now()
    time_hour = now.hour
    time_min = now.minute + 1
    kit.sendwhatmsg(f"+57{number}", message, time_hour, time_min)

def send_email(reciver_address, subject, message):
    try:
        email = EmailMessage()
        email['To'] = reciver_address
        email["Subject"] = subject
        email['From'] = EMAIL
        email.set_content(message)
        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        s.login(EMAIL, PASSWORD)
        s.sendz_message(email)
        s.close()
        return True
    except Exception as e:
        print(e)
        return False