import requests
from bs4 import BeautifulSoup
import pickle

# Obtener el contenido de la página
url = 'https://www.nasa.gov/'
response = requests.get(url)
content = response.content

# Parsear el contenido con BeautifulSoup
soup = BeautifulSoup(content, 'html.parser')

# Obtener el título de la página
title = soup.title.string

# Guardar el título en un archivo con pickle
with open('nasa_title.pickle', 'wb') as f:
    pickle.dump(title, f)

# Cargar el título desde el archivo
with open('nasa_title.pickle', 'rb') as f:
    loaded_title = pickle.load(f)

# Imprimir el título cargado desde el archivo
print('Título cargado desde el archivo:', loaded_title)
