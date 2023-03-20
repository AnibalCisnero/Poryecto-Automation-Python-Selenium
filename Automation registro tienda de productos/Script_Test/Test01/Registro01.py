#Caso de prueba: Comprobar que el formulario de registro aparece correctamente en la página de registro con los campos “Username” y “Password:”

#Importamos los modulos y bibliotecas necesarios para la Automatizacion
import unittest #Para definir las pruebas
from HtmlTestRunner import HTMLTestRunner #Para generar informes HTML de las pruebas
from selenium import webdriver #Para automatizar la interaccion con el navegador web 
from selenium.webdriver.common.by import By #Para localizar un elemento de la pagina web
import time #Para añadir pausas o retrasos en el ejecucion del script

#Definimos la clase "TestRegistro" que hereda de la clase TestCase de unittest
class TestRegistro(unittest.TestCase):
    
     #Definimos un metodo setUp() que se ejecutara antes de la prueba
    def setUp(self):
        #incializara una instancia del navegador web Google Chrome
        self.driver = webdriver.Chrome()
    
    #Este es el método de prueba real, llamado "test_formulario_registro". 
    #Este método realiza la secuencia de acciones necesarias para realizar la prueba
    def test_capturar_form_registro(self):
        
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
        self.assertEqual(texto_usuario, "Username:", "El nombre del campo de usuario no coincide")
        self.assertEqual(texto_contraseña, "Password:", "El nombre del campo de contraseña no coincide")


    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
        # Abrimos el archivo de salida
    archivo_salida = open('reporte Formulario de Registro (01).html', 'w')

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