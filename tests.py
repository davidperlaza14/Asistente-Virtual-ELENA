import pyttsx3
import requests
import wikipedia
import pywhatkit as kit
from email.message import EmailMessage
import smtplib
from decouple import config



# Inicializa el motor de síntesis de voz
# engine = pyttsx3.init()

# Obtén la lista de voces disponibles
# voices = engine.getProperty('voices')

# Enumera las voces disponibles
# print("Voces disponibles")
# for i, voice in enumerate(voices, start=1):
#     print(f"Voz {i}: {voice.name}")


# Reproduce una muestra de audio con cada voz disponible
# for i, voice in enumerate(voices, start=1):
#     print(f"Reproduciendo muestra de audio con Voz {i}: {voice.name}")
#     engine.setProperty('voice', voice.id)
#     engine.say("Hola, esta es una muestra de audio utilizando la voz" + voice.name)
#     engine.runAndWait()




# Busca una voz femenina en inglés
# for voice in voices:
#     if 'female' in voice.name.lower() and 'english' in voice.name.lower():
#     # Establece la voz femenina encontrada
#         engine.setProperty('voice', voice.id)
#         break



# Reproduce una muestra de audio con la voz femenina seleccionada
# engine.say("Hello, this is a sample of speech using a female English voice.")
# engine.runAndWait()







# import subprocess as sp

# paths = {
#     'notepad': "/usr/bin/gedit",
#     'google': "/usr/bin/gnome-www-browser",
#     'calculator': "/usr/bin/gnome-calculator",
#     'terminal': "/usr/bin/gnome-terminal",
#     'pomodoro': "/usr/bin/gnome-pomodoro",
#     'clocks': "/usr/bin/gnome-clocks",
#     'camera': "cheese",
#     'firefox': "/usr/bin/firefox"
# }

# def open_app(app_name):
#     # Verifica si la aplicación está en el diccionario de rutas
#     if app_name in paths:
#         # Obtiene la ruta de la aplicación del diccionario
#         app_path = paths[app_name]
#         # Abre la aplicación utilizando el comando subprocess.run
#         sp.run(app_path)
#     else:
#         print(f"No se encontró la aplicación {app_name} en el diccionario.")

# # Ejemplo de uso
# open_app('firefox')




# =============================================
# =============================================


"""Para interactuar con API usando Python, generalmente utilizamos la biblioteca requests, que nos permite realizar solicitudes HTTP de manera sencilla. Aquí te muestro cómo puedes implementar una función de búsqueda en Wikipedia y otra función para reproducir vídeos en YouTube."""
# import requests

# def search_wikipedia(query):
#     # URL base de la API de Wikipedia
#     base_url = "https://en.wikipedia.org/w/api.php"
    
#     # Parámetros de la solicitud
#     params = {
#         "action": "query",
#         "format": "json",
#         "list": "search",
#         "srsearch": query
#     }

#     # Realizar la solicitud GET a la API de Wikipedia
#     response = requests.get(base_url, params=params)
    
#     # Verificar el estado de la respuesta
#     if response.status_code == 200:
#         # Convertir la respuesta a JSON
#         data = response.json()
#         # Obtener los títulos de los artículos encontrados
#         for item in data['query']['search']:
#             print(item['title'])
#     else:
#         print("Error al realizar la solicitud a la API de Wikipedia")

# Ejemplo de uso
# search_wikipedia("Sexo")


# import requests

# def get_public_ip():
#     try:
#         response = requests.get("https://api.ipify.org?format=json")
#         if response.status_code == 200:
#             return response.json()
#         else:
#             print("Error al obtener la dirección IP pública")
#             return None
#     except Exception as e:
#         print("Error:", e)
#         return None

# Ejemplo de uso
# public_ip = get_public_ip()
# if public_ip:
#     print("Tu dirección IP pública es:", public_ip)





# Importa la función desde tu archivo
# from functions.online_ops import search_on_wikipedia

# Define el término de búsqueda
# search_query = "Green Colors"

# Llama a la función con el término de búsqueda
# result = search_on_wikipedia(search_query)

# Imprime los resultados
# print(result)



from functions.online_ops import *

# video_name = "Despacito"
# play_on_youtube(video_name)

# buscar en Google.
name = "Marie Curie"
search_on_google(name)




# send_whatsapp_message("314145902348693023513", "Hola amor, te envie este mensaje desde mi propia inteligencia artificial.")

