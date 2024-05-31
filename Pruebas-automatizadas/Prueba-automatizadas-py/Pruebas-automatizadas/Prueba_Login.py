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
    # Abrir la página web
    driver.get("https://www.instagram.com/")

    # Tomar una captura de pantalla después de abrir la página
    driver.save_screenshot(os.path.join(screenshot_dir, 'login_1.png'))

    # Esperar a que el botón de inicio de sesión esté presente en la página
    login_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[contains(@class, 'x9f619')]")))
    login_button.click()

    # Esperar a que el campo de correo electrónico esté presente en la página
    email_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))

    # Introducir el correo electrónico en el campo de entrada de correo electrónico
    email =  ""
    email_field.send_keys(email)

    # Esperar a que el campo de contraseña esté presente en la página
    password_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "password")))

    # Introducir la contraseña en el campo de entrada de contraseña
    contrasena = ""
    password_field.send_keys(contrasena)

    # Enviar la tecla "Enter" para iniciar sesión
    password_field.send_keys(Keys.ENTER)

    # Esperar a que la página de inicio cargue completamente después de iniciar sesión (ajustar este tiempo de espera según sea necesario)
    time.sleep(5)

    # Tomar una captura de pantalla después de iniciar sesión correctamente
    driver.save_screenshot(os.path.join(screenshot_dir, 'inicio_sesion_Correcto.png'))

    # Esperar a que aparezcan las notificaciones de Instagram (ajustar este tiempo de espera según sea necesario)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[contains(@class, 'x1lliihq')]")))

    # Encontrar el elemento de notificaciones de Instagram y hacer clic en él
    notifications_button = driver.find_element(By.XPATH, "//*[contains(@class, 'x1lliihq')]")
    notifications_button.click()

    # Tomar una captura de pantalla después de hacer clic en las notificaciones
    driver.save_screenshot(os.path.join(screenshot_dir, 'Finalizacion.png'))

except Exception as e:
    print("Ocurrió un error:", e)

# Agregar una pausa para que la página permanezca abierta durante 30 segundos después de completar la carga
time.sleep(30)

# Cerrar el navegador adecuadamente después de la pausa
driver.quit()
