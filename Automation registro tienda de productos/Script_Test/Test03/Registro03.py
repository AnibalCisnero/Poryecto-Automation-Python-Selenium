#Caso de Prueba: Verificar la presencia de los botón "Sign up" y “Close“ en el formulario de registro.

import unittest
from HtmlTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestRegistro(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_close_sigUp(self):
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

        #Capturar el texto de los botones boton close y sign up
        texto_button_Close = self.driver.find_element(By.XPATH,'//*[@id="signInModal"]/div/div/div[3]/button[1]').text
        texto_button_SigUp = self.driver.find_element(By.XPATH,'//*[@id="signInModal"]/div/div/div[3]/button[2]').text

        #Comparar el texto capturaro con el texto esperado
        self.assertEqual(texto_button_Close, "Close", "El nombre del campo de usuario no coincide")
        self.assertEqual(texto_button_SigUp, "Sign up", "El nombre del campo de contraseña no coincide")


    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
        # Abrimos el archivo de salida
    archivo_salida = open('reporte Formulario de Registro (03).html', 'w')

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


