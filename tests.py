from functions.online_ops import *
from functions.os_ops import *
from main import *

"""Test de todas las funciones."""

# notepad
# open_notepad()

# google
# open_google()

# calculator
# open_calculator()

# terminal
# open_terminal()

# pomodoro
# open_pomodoro()

# clocks
# open_clocks()

# camera
# open_camera()

# firefox
# open_firefox()

# ip_address
# print(find_my_ip())

# wikipedia
# print(search_on_wikipedia("Chemestry"))

# youtube
# play_on_youtube("Feliz navida 1")

# search_on_google
# search_on_google("Mari Curie")

# send whatsapp message
# send_whatsapp_message()

# Importa la función


# Define los detalles del correo electrónico
# receiver_address = "@gmail.com"
# subject = "Prueba de correo electrónico"
# message = "Hola, esto es una prueba de correo electrónico desde Python."

# # Llama a la función para enviar el correo electrónico
# enviado_exitosamente = send_email(receiver_address, subject, message)

# # Verifica si el correo electrónico se envió correctamente
# if enviado_exitosamente:
#     print("El correo electrónico se envió correctamente.")
# else:
#     print("Hubo un error al enviar el correo electrónico.")

# from functions.online_ops import get_latest_news
# latest_news = get_latest_news()
# if latest_news:
#     for headline in latest_news:
#         print(headline)
# else:
#     print("No se pudieron obtener las ultimas noticias.")

# print(get_weather_report("New York"))



# =======================================

# trending_movies  = get_trending_movies()

# if trending_movies:
#     print("Las películas de tendencia son:")
#     for movie in trending_movies:
#         print(movie)
# else:
#     print("o se pudieron obtener las películas de tendencia.")



# ==========================================
# print(get_random_joke())


# ===========================================
# print(get_random_advice())

import pyttsx3
from decouple import config

# USERNAME = config('USER')
# BOTNAME = config('BOTNAME')

# def speak(text):
#     engine = pyttsx3.init('espeak')
#     engine.say(text)
#     engine.runAndWait()

# def greet_user():
#     """Greets the user according to the time"""
#     speak(f"Hello {USERNAME}, how are you today?")

# greet_user()