from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

# Configurar el directorio para almacenar las capturas de pantalla
screenshot_dir = 'screenshots'
if not os.path.exists(screenshot_dir):
    os.makedirs(screenshot_dir)

# Configurar el driver de Selenium
driver = webdriver.Chrome()

try:
    # Abrir la página web de Instagram
    driver.get("https://www.instagram.com/")

    # Tomar una captura de pantalla después de abrir la página
    driver.save_screenshot(os.path.join(screenshot_dir, 'paso_1.png'))

    # Esperar a que el campo de nombre de usuario esté presente en la página
    username_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))

    # Introducir el nombre de usuario en el campo de entrada de nombre de usuario
    username = ""
    username_field.send_keys(username)

    # Esperar a que el campo de contraseña esté presente en la página
    password_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "password")))

    # Introducir la contraseña en el campo de entrada de contraseña
    contrasena = ""
    password_field.send_keys(contrasena)

    # Enviar la tecla "Enter" para iniciar sesión
    password_field.send_keys(Keys.ENTER)

    # Tomar una captura de pantalla después de iniciar sesión correctamente
    driver.save_screenshot(os.path.join(screenshot_dir, 'inicio_sesion.png'))

    # Esperar a que aparezcan las publicaciones en el feed de inicio (ajustar este tiempo de espera según sea necesario)
    time.sleep(5)

    # ver historias
    ver = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[contains(@class, 'x6s0dn4')][1]")))
    ver.click()
    time.sleep(5)
  
    # Tomar una captura de pantalla después de ver la historia
    driver.save_screenshot(os.path.join(screenshot_dir, 'Historias.png'))

except Exception as e:
    print("Ocurrió un error:", e)

# Agregar una pausa para que la página permanezca abierta durante 30 segundos después de completar la carga
time.sleep(30)

# Cerrar el navegador adecuadamente después de la pausa
driver.quit()
