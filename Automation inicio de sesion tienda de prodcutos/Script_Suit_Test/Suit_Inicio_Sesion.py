import unittest
import logging
from HtmlTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


#configuramos el logger básico para que registre los mensajes en un archivo de registro (en este caso, 'test.log')
#solo se registrarán mensajes con un nivel de ERROR o superior.
logging.basicConfig(filename='test.log', level=logging.ERROR)

class Suit_inicioSesion(unittest.TestCase):
     def setUp(self):
        self.driver = webdriver.Chrome()

     
     def test_IncisoSesionExitoso(self):
      try:
        self.driver.get("https://www.demoblaze.com/index.html")
        time.sleep(10)
    
        self.driver.maximize_window()

        self.driver.find_element(By.ID,'login2').click()
        time.sleep(10)

        self.driver.find_element(By.ID,'loginusername').send_keys("Anibal98")
        time.sleep(20)
        
        self.driver.find_element(By.ID,'loginpassword').send_keys(1234)
        time.sleep(10)

        self.driver.find_element(By.XPATH,"//*[@id='logInModal']/div/div/div[3]/button[2]").click()
        time.sleep(20)
        self.driver.close()
        time.sleep(20)
        pass
      #En resumen, esta línea se encarga de registrar cualquier excepción que se produzca
      #durante la ejecución de la prueba, lo que facilita el proceso de depuración y solución de problemas.
      except Exception as e:
               logging.exception("Error en la prueba 'test_IncisoSesionExitoso'")
    
     def test_CredencialesInvalidas(self):
      try:
        self.driver.get("https://www.demoblaze.com/index.html")
        time.sleep(10)

        self.driver.maximize_window()
        
        self.driver.find_element(By.ID,'login2').click()
        time.sleep(10)

        self.driver.find_element(By.ID,'loginusername').send_keys("Anibal")
        time.sleep(10)
        
        self.driver.find_element(By.ID,'loginpassword').send_keys(12)
        time.sleep(10)

        self.driver.find_element(By.XPATH,"//*[@id='logInModal']/div/div/div[3]/button[2]").click()
        time.sleep(10)
        
        alert = self.driver.switch_to.alert

        alert_text = alert.text
        
        texto_alert_esperado = "Wrong password."
        
        assert texto_alert_esperado == alert_text, f"Texto del alert esperado: {texto_alert_esperado}. Texto de alert real: {alert_text}"
        
        alert.dismiss()
        time.sleep(10)
        self.driver.close()
        time.sleep(20)
        pass
      #En resumen, esta línea se encarga de registrar cualquier excepción que se produzca
      #durante la ejecución de la prueba, lo que facilita el proceso de depuración y solución de problemas.
      except Exception as e:
               logging.exception("Error en la prueba ' test_CredencialesInvalidas'")


     def test_NombreUsuarioVacio(self):
      try:
        self.driver.get("https://www.demoblaze.com/index.html")
        time.sleep(10)

        self.driver.maximize_window()

        self.driver.find_element(By.ID,'login2').click()
        time.sleep(10)
        
        self.driver.find_element(By.ID,'loginpassword').send_keys(1234)
        
        self.driver.find_element(By.XPATH,"//*[@id='logInModal']/div/div/div[3]/button[2]").click()
        time.sleep(10)

        alert = self.driver.switch_to.alert
        alert_text = alert.text
        texto_alert_esperado = "Please fill out Username and Password."
        assert texto_alert_esperado == alert_text, f"Texto del alert esperado: {texto_alert_esperado}. Texto de alert real: {alert_text}"
        alert.dismiss()
        time.sleep(10)
        self.driver.close()
        time.sleep(20)
        pass
      #En resumen, esta línea se encarga de registrar cualquier excepción que se produzca
      #durante la ejecución de la prueba, lo que facilita el proceso de depuración y solución de problemas.
      except Exception as e:
               logging.exception("Error en la prueba 'test_NombreUsuarioVacio'")


     def test_ContraseñaVacia(self):
      try:
        self.driver.get("https://www.demoblaze.com/index.html")
        time.sleep(10)

        self.driver.maximize_window()
        
        self.driver.find_element(By.ID,'login2').click()
        time.sleep(10)

        self.driver.find_element(By.ID,'loginusername').send_keys("Anibal98")
        
        self.driver.find_element(By.XPATH,"//*[@id='logInModal']/div/div/div[3]/button[2]").click()
        time.sleep(10)

        alert = self.driver.switch_to.alert
        alert_text = alert.text
        texto_alert_esperado = "Please fill out Username and Password."
        assert texto_alert_esperado == alert_text, f"Texto del alert esperado: {texto_alert_esperado}. Texto de alert real: {alert_text}"
        alert.dismiss()
        time.sleep(10)
        self.driver.close()
        time.sleep(20)
        pass
      #En resumen, esta línea se encarga de registrar cualquier excepción que se produzca
      #durante la ejecución de la prueba, lo que facilita el proceso de depuración y solución de problemas.
      except Exception as e:
               logging.exception("Error en la prueba 'test_ContraseñaVacia'")

     
     def test_UsuarioNoExistente(self):
      try:
        self.driver.get("https://www.demoblaze.com/index.html")
        time.sleep(10)

        self.driver.maximize_window()

        self.driver.find_element(By.ID,'login2').click()
        time.sleep(10)

        self.driver.find_element(By.ID,'loginusername').send_keys("ANibal")

        self.driver.find_element(By.ID,'loginpassword').send_keys("ABcd")

        self.driver.find_element(By.XPATH,"//*[@id='logInModal']/div/div/div[3]/button[2]").click()
        time.sleep(10)

        alert = self.driver.switch_to.alert
        alert_text = alert.text
        texto_alert_esperado = "User does not exist."
        assert texto_alert_esperado == alert_text, f"Texto del alert esperado: {texto_alert_esperado}. Texto de alert real: {alert_text}"
        alert.dismiss()
        time.sleep(10)
        self.driver.close()
        time.sleep(20)
        pass
      #En resumen, esta línea se encarga de registrar cualquier excepción que se produzca
      #durante la ejecución de la prueba, lo que facilita el proceso de depuración y solución de problemas.
      except Exception as e:
               logging.exception("Error en la prueba 'test_UsuarioNoExistente'")


     def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    #Abrimos el archivo de salida con la funcion open() lo utilizamos para abrir un archivo en modo de escritura
    archivo_salida = open('Reporte de la Suit de Pruebas Inicio de Sesión.html ', 'w')

    #Creamos un objeto runner de HTMLTestRunner
    runner = HTMLTestRunner(
        stream=archivo_salida, #Para que el informe se guarde en el archivo que generamos en la varibale archivo_salida
        verbosity=2, #El parámetro verbosity se establece en 2, lo que significa que se mostrarán detalles adicionales en el informe.
    )

    #Ejecutamos la suite de pruebas
    suite = unittest.TestLoader().loadTestsFromTestCase(Suit_inicioSesion)
    runner.run(suite)

    #Cerramos el archivo de salida
    archivo_salida.close()


