import unittest
import logging
from HtmlTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#configuramos el logger básico para que registre los mensajes en un archivo de registro (en este caso, 'test.log')
#solo se registrarán mensajes con un nivel de ERROR o superior.
logging.basicConfig(filename='test.log', level=logging.ERROR)

class Suit_Registro(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
    
    #Este es el método de prueba real, llamado "test_formulario_registro". 
    #Este método realiza la secuencia de acciones necesarias para realizar la prueba
    def test_capturar_form_registro(self):
      try: 
        #Abrir la página https://www.demoblaze.com/index.html.
        self.driver.get("https://www.demoblaze.com/index.html")
        
        #Esperar 10 segundos para que la página cargue completamente.
        time.sleep(10)
        
        #Buscar el botón de Sign Up al inicio de sesión por su ID ('signin2') y hacer clic en él.
        self.driver.find_element(By.ID,'signin2').click()

        #Esperar 10 segundos para que la ventana modal de inicio de sesión aparezca completamente.
        time.sleep(10)

        # Verificar que el formulario de registro aparezca en la página
        formulario = self.driver.find_element(By.XPATH, "//*[@id='signInModal']/div/div")
        self.assertTrue(formulario.is_displayed())
        time.sleep(10)

        # Verificar que el campo "Nombre de Usuario" esté presente en el formulario
        campo_usuario = formulario.find_element(By.ID, "sign-username")
        self.assertTrue(campo_usuario.is_displayed())
        time.sleep(10)

        # Verificar que el campo "Contraseña" esté presente en el formulario
        campo_contraseña = formulario.find_element(By.ID, "sign-password")
        self.assertTrue(campo_contraseña.is_displayed())
        time.sleep(10)

        #Verificar que se muestre el nombre del campo Usuername
        texto_usuario = self.driver.find_element(By.XPATH,'//*[@id="signInModal"]/div/div/div[2]/form/div[1]/label').text
        time.sleep(10)
        #Verificar que se muestre el nombre del campo Password
        texto_contraseña = self.driver.find_element(By.XPATH,'//*[@id="signInModal"]/div/div/div[2]/form/div[2]/label').text
        time.sleep(10)
        
        #Realizo la comparacion del texto capturado con el texto esperado de cada campo
        self.assertEquals(texto_usuario, "Username:", "El nombre del campo de usuario no coincide")
        self.assertEquals(texto_contraseña, "Password:", "El nombre del campo de contraseña no coincide")
        time.sleep(10)
        self.driver.quit()
        time.sleep(20)
        pass
      #En resumen, esta línea se encarga de registrar cualquier excepción que se produzca
      #durante la ejecución de la prueba, lo que facilita el proceso de depuración y solución de problemas.
      except Exception as e:
               logging.exception("Error en la prueba ''test_capturar_form_registro")

    def test_captura_text_registro(self):
      try:
        self.driver.get("https://www.demoblaze.com/index.html")
        time.sleep(10)
        #Hago click en el boton Registro
        self.driver.find_element(By.ID,'signin2').click()
        time.sleep(10)

        # Verificar que el formulario de registro aparezca en la página
        formulario = self.driver.find_element(By.XPATH, "//*[@id='signInModal']/div/div")
        self.assertTrue(formulario.is_displayed())
        time.sleep(15)
        
        campo_usuario = self.driver.find_element(By.ID, 'sign-username')
        campo_usuario.send_keys('Anibal')
        texto_capturado_usuario = campo_usuario.get_attribute('value')
        time.sleep(15)

        campo_password = self.driver.find_element(By.ID, 'sign-password')
        campo_password.send_keys('1234')
        texto_capturado_password = campo_password.get_attribute('value')
        time.sleep(15)
        
        #Realizamos la compararcion del texto capturado con el esperado
        self.assertEqual(texto_capturado_usuario, 'Anibal',  "El usuario capturado no coincide con el Usuario ingresado")
        self.assertEqual(texto_capturado_password, '1234',  "La Pasword capturada no coincide con la Pasword ingresado")

        time.sleep(10)
        self.driver.quit()
        time.sleep(20)
        pass
      #En resumen, esta línea se encarga de registrar cualquier excepción que se produzca
      #durante la ejecución de la prueba, lo que facilita el proceso de depuración y solución de problemas.
      except Exception as e:
               logging.exception("Error en la prueba 'test_captura_text_registro'")

    def test_close_sigUp(self):
      try:
        #Habro la pagina a probar
        self.driver.get("https://www.demoblaze.com/index.html")
        time.sleep(10)
        #Hacer click en el boton sig up
        self.driver.find_element(By.ID,'signin2').click()
        time.sleep(10)
       
        # Verificar que el formulario de registro aparezca en la página
        formulario = self.driver.find_element(By.XPATH, "//*[@id='signInModal']/div/div")
        self.assertTrue(formulario.is_displayed())
        time.sleep(15)

        #Capturar el texto de los botones boton close y sign up
        texto_button_Close = self.driver.find_element(By.XPATH,'//*[@id="signInModal"]/div/div/div[3]/button[1]').text
        time.sleep(15)
        texto_button_SigUp = self.driver.find_element(By.XPATH,'//*[@id="signInModal"]/div/div/div[3]/button[2]').text
        time.sleep(15)
        #Comparar el texto capturaro con el texto esperado
        self.assertEquals(texto_button_Close, "Close", "El nombre del campo de usuario no coincide")
        self.assertEquals(texto_button_SigUp, "Sign up", "El nombre del campo de contraseña no coincide")

        time.sleep(10)
        self.driver.quit()
        time.sleep(20)
        pass
      #En resumen, esta línea se encarga de registrar cualquier excepción que se produzca
      #durante la ejecución de la prueba, lo que facilita el proceso de depuración y solución de problemas.
      except Exception as e:
               logging.exception("Error en la prueba 'test_close_sigUp'")

    def test_registro_fallido(self):
      try:
        #Habro la pagina a probar
        self.driver.get("https://www.demoblaze.com/index.html")
        time.sleep(10)
        #Hacer click en el boton sig up
        self.driver.find_element(By.ID,'signin2').click()
        time.sleep(10)
       
        # Verificar que el formulario de registro aparezca en la página
        formulario = self.driver.find_element(By.XPATH, "//*[@id='signInModal']/div/div")
        self.assertTrue(formulario.is_displayed())
        time.sleep(15)

        #Ingresar un usuario ya registrado
        self.driver.find_element(By.ID,'sign-username').send_keys('Anibal98')
        time.sleep(15)

        #Hacer click en boton sig up
        self.driver.find_element(By.XPATH,'//*[@id="signInModal"]/div/div/div[3]/button[2]').click()
        time.sleep(15)

        #Capturo el alert 
        alert = self.driver.switch_to.alert
        #Capturo el mensaje del alert
        alert_text = alert.text
        #mensaje esperado
        texto_alert_esperado = "Please fill out Username and Password."
        #Comparar el mensaje capturado con el mensaje esperado
        assert texto_alert_esperado == alert_text, f"Texto del alert esperado: {texto_alert_esperado}. Texto de alert real: {alert_text}"
        #Aceptar el alert
        alert.accept()
        time.sleep(20)
        pass
      #En resumen, esta línea se encarga de registrar cualquier excepción que se produzca
      #durante la ejecución de la prueba, lo que facilita el proceso de depuración y solución de problemas.
      except Exception as e:
               logging.exception("Error en la prueba 'test_registro_fallido'")
    
    
    def test_usuario_existente(self):
      try:
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

        #Ingresar un usuario ya registrado
        self.driver.find_element(By.ID,'sign-username').send_keys('Anibal98')
        time.sleep(10)

        #Ingresar una contraseña ya registrada
        self.driver.find_element(By.ID,'sign-password').send_keys('1234')
        time.sleep(10)

        #Hacer click en boton sig up
        self.driver.find_element(By.XPATH,'//*[@id="signInModal"]/div/div/div[3]/button[2]').click()
        time.sleep(10)

        #Capturo el alert 
        alert = self.driver.switch_to.alert
        #Capturo el mensaje del alert
        alert_text = alert.text
        #mensaje esperado
        texto_alert_esperado = "This user already exist."
        #Comparar el mensaje capturado con el mensaje esperado
        assert texto_alert_esperado == alert_text, f"Texto del alert esperado: {texto_alert_esperado}. Texto de alert real: {alert_text}"
        #Aceptar el alert
        alert.accept()
        time.sleep(10)
        self.driver.quit()
        pass
      #En resumen, esta línea se encarga de registrar cualquier excepción que se produzca
      #durante la ejecución de la prueba, lo que facilita el proceso de depuración y solución de problemas.
      except Exception as e:
               logging.exception("Error en la prueba 'test_usuario_existente'")

    def test_contraseña_existente(self):
      try:
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

        #Ingresar una contraseña ya registrada
        self.driver.find_element(By.ID,'sign-password').send_keys('1234')
        time.sleep(10)

        #Hacer click en boton sig up
        self.driver.find_element(By.XPATH,'//*[@id="signInModal"]/div/div/div[3]/button[2]').click()
        time.sleep(10)

        #Capturo el alert 
        alert = self.driver.switch_to.alert
        #Capturo el mensaje del alert
        alert_text = alert.text
        #mensaje esperado
        texto_alert_esperado = "Please fill out Username and Password."
        #Comparar el mensaje capturado con el mensaje esperado
        assert texto_alert_esperado == alert_text, f"Texto del alert esperado: {texto_alert_esperado}. Texto de alert real: {alert_text}"
        #Aceptar el alert
        alert.accept()
        time.sleep(10)
        self.driver.quit()
        pass
      #En resumen, esta línea se encarga de registrar cualquier excepción que se produzca
      #durante la ejecución de la prueba, lo que facilita el proceso de depuración y solución de problemas.
      except Exception as e:
               logging.exception("Error en la prueba 'test_contraseña_existente'")

    def test_Registro_exitoso(self):
      try:   
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
        self.driver.find_element(By.ID,'sign-username').send_keys('Konor20')
        time.sleep(10)

        #Ingresar una contraseña no registrada
        self.driver.find_element(By.ID,'sign-password').send_keys('2023')
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
        time.sleep(10)
        pass
      #En resumen, esta línea se encarga de registrar cualquier excepción que se produzca
      #durante la ejecución de la prueba, lo que facilita el proceso de depuración y solución de problemas.
      except Exception as e:
               logging.exception("Error en la prueba 'test_Registro_exitoso'")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
      # Abrimos el archivo de salida
    archivo_salida = open('reporte Suit de Pruebas Registro.html', 'w')

    # Creamos un objeto runner de HTMLTestRunner
    runner = HTMLTestRunner(
        stream=archivo_salida,
        verbosity=2,
    )

    # Ejecutamos la suite de pruebas
    suite = unittest.TestLoader().loadTestsFromTestCase(Suit_Registro)
    runner.run(suite)

    # Cerramos el archivo de salida
    archivo_salida.close()
