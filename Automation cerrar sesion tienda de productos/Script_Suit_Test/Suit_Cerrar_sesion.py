import unittest
import logging
from HtmlTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import text_to_be_present_in_element
from selenium.webdriver.common.by import By
import time

#configuramos el logger básico para que registre los mensajes en un archivo de registro (en este caso, 'test.log')
#solo se registrarán mensajes con un nivel de ERROR o superior.
logging.basicConfig(filename='test.log', level=logging.ERROR)

class Suit_CerrarSesion(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_Verificar_laPrecencia_Logout(self):
       try:
        self.driver.get("https://www.demoblaze.com/index.html")
        time.sleep(20)
        self.driver.maximize_window()
        acceso = self.driver.find_element(By.ID,'login2')
        acceso.click()
        time.sleep(10)
        campo_usuario = self.driver.find_element(By.ID,'loginusername')
        campo_usuario.send_keys("Anibal98")
        cammpo_contraseña = self.driver.find_element(By.ID,'loginpassword')
        cammpo_contraseña.send_keys(1234)
        login_button = self.driver.find_element(By.XPATH,"//*[@id='logInModal']/div/div/div[3]/button[2]")
        login_button.click()
        time.sleep(30)
        element = WebDriverWait(self.driver, 10).until(
             EC.presence_of_element_located((By.ID, "logout2"))
             )
        element.screenshot(r"C:\Users\54373\Desktop\Automatizacion con Python con Selenium\captura cerrar sesion.png")
        self.driver.quit()
        time.sleep(10)
        pass
      #En resumen, esta línea se encarga de registrar cualquier excepción que se produzca
      #durante la ejecución de la prueba, lo que facilita el proceso de depuración y solución de problemas.
       except Exception as e:
               logging.exception("Error en la prueba 'test_Verificar_laPrecencia_Logout")

    def test_user_redirected_to_login_page_after_logout(self):
      try:
        self.driver.get("https://www.demoblaze.com/index.html")
        time.sleep(20)
        self.driver.maximize_window()
        acceso = self.driver.find_element(By.ID,'login2')
        acceso.click()
        time.sleep(10)
        #Campo usuario ingreso los datos
        self.driver.find_element(By.ID,'loginusername').send_keys("Anibal98")
        #Campo Password ingreso los datos
        self.driver.find_element(By.ID,'loginpassword').send_keys(1234)
        #Click en el boton login
        self.driver.find_element(By.XPATH,"//*[@id='logInModal']/div/div/div[3]/button[2]").click()
        time.sleep(10)
        #Clicke en cerrar seison
        self.driver.find_element(By.ID,'logout2').click()
        # Comprobar que se redirige a la página de inicio de sesión
        WebDriverWait(self.driver, 10).until(EC.url_matches("https://www.demoblaze.com/index.html"))
        self.driver.quit()
        pass
      #En resumen, esta línea se encarga de registrar cualquier excepción que se produzca
      #durante la ejecución de la prueba, lo que facilita el proceso de depuración y solución de problemas.
      except Exception as e:
               logging.exception("Error en la prueba 'test_user_redirected_to_login_page_after_logout")

    def test_cerrar_sesion_al_cerrar_pestaña(self):
      try:
        self.driver.get("https://www.demoblaze.com/index.html")
        # Haz clic en el botón de inicio de sesión
        login_button = self.driver.find_element(By.ID,"login2")
        login_button.click()

# Espera a que se muestre el cuadro de diálogo de inicio de sesión
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "logInModal")))

# Ingresa el nombre de usuario y la contraseña
        username_field = self.driver.find_element(By.ID,"loginusername")
        password_field = self.driver.find_element(By.ID,"loginpassword")
        username_field.send_keys("Anibal98")
        password_field.send_keys(1234)
        time.sleep(10)

# Haz clic en el botón de inicio de sesión en el cuadro de diálogo
        login_button = self.driver.find_element(By.XPATH,"//div[@id='logInModal']//button[text()='Log in']")
        login_button.click()
        time.sleep(10)

        # Obtener la sesión actual
        current_session_id = self.driver.session_id
        time.sleep(5)

        # Cerrar la sesión al cerrar la ventana
        self.driver.execute_script("window.onbeforeunload = function() { navigator.sendBeacon('/session/close', ''); };")
        time.sleep(5)
        # Abrir una nueva ventana
        self.driver.execute_script("window.open('https://www.demoblaze.com/index.html', 'new_window')")
        time.sleep(5)

        # Cambiar a la nueva ventana
        self.driver.switch_to.window("new_window")
        time.sleep(5)

# Verificar que la sesión anterior se cerró
        try:
                WebDriverWait(self.driver, 10).until(self.staleness_of(self.driver.find_element(By.ID, "nameofuser")))
        except:
                print("La sesión no se cerró al cerrar la ventana")
        self.driver.quit()
        pass
      #En resumen, esta línea se encarga de registrar cualquier excepción que se produzca
      #durante la ejecución de la prueba, lo que facilita el proceso de depuración y solución de problemas.
      except Exception as e:
               logging.exception("Error en la prueba 'test_cerrar_sesion_al_cerrar_pestaña")
         

    def test_redireccion(self):
      try:
        self.driver.get("https://www.demoblaze.com/index.html")
        time.sleep(10)
         # Haz clic en el botón de inicio de sesión
        login_button = self.driver.find_element(By.ID,"login2")
        login_button.click()

# Espera a que se muestre el cuadro de diálogo de inicio de sesión
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "logInModal")))

# Ingresa el nombre de usuario y la contraseña
        username_field = self.driver.find_element(By.ID,"loginusername")
        password_field = self.driver.find_element(By.ID,"loginpassword")
        username_field.send_keys("Anibal98")
        password_field.send_keys(1234)
        time.sleep(10)

# Haz clic en el botón de inicio de sesión en el cuadro de diálogo
        login_button = self.driver.find_element(By.XPATH,"//div[@id='logInModal']//button[text()='Log in']")
        login_button.click()
        time.sleep(10)
        
        # Cierra el navegador y vuelve a abrir la página
        self.driver.quit()
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.demoblaze.com/index.html")
        time.sleep(10)
        
        # Verifica que se redirige a la página de inicio de sesión
        login_modal = self.driver.find_element(By.ID, "login2")
        assert login_modal.is_displayed(), "No se redirige a la página de inicio de sesión"
        time.sleep(10)
        pass
      #En resumen, esta línea se encarga de registrar cualquier excepción que se produzca
      #durante la ejecución de la prueba, lo que facilita el proceso de depuración y solución de problemas.
      except Exception as e:
               logging.exception("Error en la prueba 'test_redireccion")
      
    def tearDown(self):
            self.driver.quit()

if __name__ == '__main__':
    #Abrimos el archivo de salida con la funcion open() lo utilizamos para abrir un archivo en modo de escritura
    archivo_salida = open('Reporte de la Suit de Prueba Cerrar Sesión.html', 'w')

    #Creamos un objeto runner de HTMLTestRunner
    runner = HTMLTestRunner(
        stream=archivo_salida, #Para que el informe se guarde en el archivo que generamos en la varibale archivo_salida
        verbosity=2, #El parámetro verbosity se establece en 2, lo que significa que se mostrarán detalles adicionales en el informe.
    )

    #Ejecutamos la suite de pruebas
    suite = unittest.TestLoader().loadTestsFromTestCase(Suit_CerrarSesion)
    runner.run(suite)

    #Cerramos el archivo de salida
    archivo_salida.close()
