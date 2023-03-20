#Caso de Prueba: Registro exitoso
import unittest
from HtmlTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestRegistro(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_Registro_exitoso(self):
        #Habro la pagina a probar
        self.driver.get("https://www.demoblaze.com/index.html")
        time.sleep(10)
        #Hacer click en el boton sig up
        self.driver.find_element(By.ID,'signin2').click()
        time.sleep(10)
       
        # Verificar que el formulario de registro aparezca en la página
        formulario = self.driver.find_element(By.XPATH, "//*[@id='signInModal']/div/div")
        self.assertTrue(formulario.is_displayed())
        time.sleep(10)

        #Ingresar un usuario que no existe para registrame
        self.driver.find_element(By.ID,'sign-username').send_keys('Marzo2023')
        time.sleep(10)

        #Ingresar una contraseña no registrada
        self.driver.find_element(By.ID,'sign-password').send_keys('9815')
        time.sleep(10)

        #Hacer click en boton sig up
        self.driver.find_element(By.XPATH,'//*[@id="signInModal"]/div/div/div[3]/button[2]').click()
        time.sleep(10)

        #Capturo el alert 
        alert = self.driver.switch_to.alert
        #Capturo el mensaje del alert de registro existoso
        alert_text = alert.text
        #mensaje esperado
        texto_alert_esperado = "Sign up successful."
        #Comparar el mensaje capturado con el mensaje esperado
        assert texto_alert_esperado == alert_text, f"Texto del alert esperado: {texto_alert_esperado}. Texto de alert real: {alert_text}"
        #Aceptar el alert
        alert.accept()

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
        # Abrimos el archivo de salida
    archivo_salida = open('reporte Formulario de Registro (07).html', 'w')

    # Creamos un objeto runner de HTMLTestRunner
    runner = HTMLTestRunner(
        stream=archivo_salida,
        verbosity=2,
    )

    # Ejecutamos la suite de pruebas
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRegistro)
    runner.run(suite)

    # Cerramos el archivo de salida
    archivo_salida.close()