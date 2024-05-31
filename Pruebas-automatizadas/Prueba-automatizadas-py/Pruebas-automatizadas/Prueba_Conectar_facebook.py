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
    # Abrir la página web i
    driver.get("https://www.instagram.com/")

    # Tomar una captura de pantalla después de abrir la página de facebok
    driver.save_screenshot(os.path.join(screenshot_dir, 'login_facebook.png'))

    # Esperar a que el botón de inicio de sesión esté presente en la página de facebook
    login_facebook = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[contains(@class, '_ab37')]")))
    login_facebook.click()
    

   

    # Esperar a que la página de inicio cargue completamente después de iniciar sesión (ajustar este tiempo de espera según sea necesario)
    time.sleep(10)

    # Tomar una captura de pantalla después de iniciar sesión correctamente
    driver.save_screenshot(os.path.join(screenshot_dir, 'facebook.png'))

    

except Exception as e:
    print("Ocurrió un error:", e)

# Agregar una pausa para que la página permanezca abierta durante 30 segundos después de completar la carga
time.sleep(30)

# Cerrar el navegador adecuadamente después de la pausa
driver.quit()
