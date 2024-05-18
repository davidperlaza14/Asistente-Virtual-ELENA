import requests
import wikipedia
import smtplib
import pywhatkit as kit
import datetime
from email.message import EmailMessage
import smtplib
from decouple import config


EMAIL = config("EMAIL")
PASSWORD = config("PASSWORD")
OPENWEATHER_APP_ID = config("OPENWEATHER_APP_ID")
NEWS_API_KEY = config("NEWS_API_KEY")
TMDB_API_KEY = config("TMDB_API_KEY")

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


def send_email(receiver_address, subject, message):
    try:
        email = EmailMessage()
        email['To'] = receiver_address
        email["Subject"] = subject
        email['From'] = EMAIL
        email.set_content(message)
        
        # Conexión al servidor SMTP de Gmail
        with smtplib.SMTP("smtp.gmail.com", 587) as s:
            s.starttls()  # Habilita el cifrado TLS
            s.login(EMAIL, PASSWORD)  # Inicia sesión en la cuenta de Gmail
            s.send_message(email)  # Envía el correo electrónico
        
        return True
    except Exception as e:
        print(e)
        return False


def get_latest_news():
    news_headlines = []
    res = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}&category=general").json()
    articles = res["articles"]
    for article in articles:
        news_headlines.append(article["title"])
    return news_headlines[:5]
    
#     try:
        
#         # Realiza la solicitud a la API de noticias
#         response = requests.get(url)
        
#         # Verifica si la solicitud fue exitosa
#         if response.status_code == 200:
#             data = response.json()
#             articles = data.get("articles", [])
            
#             # Extrae los títulos de los artículos
#             for article in articles:
#                 title = article.get("title")
#                 if title:
#                     news_headlines.append(title)
            
#             return news_headlines[:5]
        
#         if response.status_code == 426:
#             print("Error en la solicitud HTTP: 426")
#             print("Mensaje de la API:", data.get("message"))
#             print("No se pudieron obtener las últimas noticias. Por favor, ajusta la fecha de la solicitud.")
#             return None

#         else:
#             print("Error en la solicitud HTTP:", response.status_code)
#             print("Contenido de la respuesta:", response.content)  # Imprime el contenido de la respuesta para obtener más información
#             return None
#     except Exception as e:
#         print("Error:", e)
#         return None


def get_weather_report(city):
    res = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_APP_ID}").json()
    
    # Extrae la información del clima del diccionario "main"
    weather = res["weather"][0]["main"]
    
    # Temperatura en grados Celsius (kelvin - 273.15)
    temperature = f"{res['main']['temp'] - 273.15}℃"
    
    # Sensación térmica en grados Celsius (kelvin - 273.15)
    feels_like = f"{res['main']['feels_like'] - 273.15}℃"
    
    return weather, temperature, feels_like


def get_trending_movies():
    trending_movies = []
    res = requests.get(f"https://api.themoviedb.org/3/movie/550?api_key={TMDB_API_KEY}").json()
    results = res.get("results", [])
    for movie in results:
        title = movie.get("original_title")
        if title:
            trending_movies.append(title)

    return trending_movies[:5]

def get_random_joke():
    headers = {
        'Accept': 'application/json'
    }
    res =  requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    return res["joke"]


def get_random_advice():
    res = requests.get("https://api.adviceslip.com/advice").json()
    return res['slip']['advice']