import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# Configuración del navegador
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

# URL de la página a extraer
url = 'https://es.wikipedia.org/wiki/Anexo:Pa%C3%ADses_de_%C3%81frica'

# Navegar hasta la página
driver.get(url)

# Esperar a que se carguen los elementos multimedia
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, 'img')))

# Extraer las imágenes y guardarlas en la carpeta images
image_count = 0
for img in driver.find_elements(By.TAG_NAME, 'img'):
    src = img.get_attribute('src')
    if src and 'http' in src and 'nasa_logo' not in src:
        response = requests.get(src)
        with open(f'images/image{image_count}.jpg', 'wb') as f:
            f.write(response.content)
        image_count += 1
        if image_count >= 100:
            break

# Cerrar el navegador
driver.quit()
