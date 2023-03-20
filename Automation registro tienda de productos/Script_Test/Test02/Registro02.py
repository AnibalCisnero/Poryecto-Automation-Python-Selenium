#Caso de Prueba: Validar que el usuario puede ingresar su nombre de usuario y contraseña deseados en los campos correspondientes.

import unittest
from HtmlTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestRegistro(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_captura_text_registro(self):
        self.driver.get("https://www.demoblaze.com/index.html")
        time.sleep(10)
        #Hago click en el boton Registro
        self.driver.find_element(By.ID,'signin2').click()
        time.sleep(10)

        # Verificar que el formulario de registro aparezca en la página
        formulario = self.driver.find_element(By.XPATH, "//*[@id='signInModal']/div/div")
        self.assertTrue(formulario.is_displayed())
        time.sleep(10)
        
        campo_usuario = self.driver.find_element(By.ID, 'sign-username')
        time.sleep(10)
        campo_usuario.send_keys('Anibal')
        texto_capturado_usuario = campo_usuario.get_attribute('value')

        campo_password = self.driver.find_element(By.ID, 'sign-password')
        time.sleep(10)
        campo_password.send_keys('1234')
        texto_capturado_password = campo_password.get_attribute('value')
        
        #Realizamos la compararcion del texto capturado con el esperado
        self.assertEquals (texto_capturado_usuario, 'Anibal',  "El usuario capturado no coincide con el Usuario ingresado")
        self.assertEquals (texto_capturado_password, '1234',  "La Pasword capturada no coincide con la Pasword ingresado")



    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
      # Abrimos el archivo de salida
    archivo_salida = open('reporte Formulario de Registro (02).html', 'w')

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
