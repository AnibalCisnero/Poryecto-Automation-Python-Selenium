#Importamos los modulos y bibliotecas necesarios para la Automatizacion
import unittest #Para definir las pruebas
from HtmlTestRunner import HTMLTestRunner #Para generar informes HTML de las pruebas
from selenium import webdriver #Para automatizar la interaccion con el navegador web 
from selenium.webdriver.common.by import By #Para localizar un elemento de la pagina web
import time #Para añadir pausas o retrasos en el ejecucion del script

#Definimos la clase "incioSesion_unittest" que hereda de la clase TestCase de unittest
class InicioSesion(unittest.TestCase):
     #Definimos un metodo setUp() que se ejecutara antes de la prueba
     def setUp(self):
        #incializara una instancia del navegador web Google Chrome
        self.driver = webdriver.Chrome()
     
     #Este es el método de prueba real, llamado "test_IncisoSesionExitoso". 
     #Este método realiza la secuencia de acciones necesarias para realizar la prueba   
     def test_IncisoSesionExitoso(self):
        
        #Abrir la página https://www.demoblaze.com/index.html.
        self.driver.get("https://www.demoblaze.com/index.html")
        
        #Esperar 10 segundos para que la página cargue completamente.
        time.sleep(10)
        
        #Maximizar la ventana del navegador.
        self.driver.maximize_window()

        #Buscar el botón de Log in al inicio de sesión por su ID ('login2') y hacer clic en él.
        self.driver.find_element(By.ID,'login2').click()

        #Esperar 10 segundos para que la ventana modal de inicio de sesión aparezca completamente.
        time.sleep(10)

        #Buscar el campo Username por su ID ('loginusername') y escribir en él el valor "Anibal98".
        self.driver.find_element(By.ID,'loginusername').send_keys("Anibal98")
        
        #Buscar el campo Password por su ID ('loginpassword') y escribir en él el valor numérico 1234.
        self.driver.find_element(By.ID,'loginpassword').send_keys(1234)
        
        #Buscar el botón de inicio de sesión por su ruta XPath y hacer clic en él.
        self.driver.find_element(By.XPATH,"//*[@id='logInModal']/div/div/div[3]/button[2]").click()
        
        #Esperar 20 segundos para que el inicio de sesión se complete y se cargue la página principal después del inicio de sesión.
        time.sleep(20)
     
     #Con este metodo luego de realizar la prueba limpiamos el navegaro web
     def tearDown(self):
        #Cerramos el navegadro
        self.driver.quit()

if __name__ == '__main__':
    #Abrimos el archivo de salida con la funcion open() lo utilizamos para abrir un archivo en modo de escritura
    archivo_salida = open('Reporte del caso de prueba (Incio de sesion 01).html', 'w')

    #Creamos un objeto runner de HTMLTestRunner
    runner = HTMLTestRunner(
        stream=archivo_salida, #Para que el informe se guarde en el archivo que generamos en la varibale archivo_salida
        verbosity=2, #El parámetro verbosity se establece en 2, lo que significa que se mostrarán detalles adicionales en el informe.
    )

    #Ejecutamos la suite de pruebas
    suite = unittest.TestLoader().loadTestsFromTestCase(InicioSesion)
    runner.run(suite)

    #Cerramos el archivo de salida
    archivo_salida.close()