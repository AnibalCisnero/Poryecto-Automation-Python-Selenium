import unittest
from HtmlTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class CerrarSesion(unittest.TestCase):
     def setUp(self):
        self.driver = webdriver.Chrome()
     
        
     def test_user_redirected_to_login_page_after_logout(self):
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
        time.sleep(10)


 
     def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    #Abrimos el archivo de salida con la funcion open() lo utilizamos para abrir un archivo en modo de escritura
    archivo_salida = open('Reporte del caso de prueba (Cerrar Sesion 02).html', 'w')

    #Creamos un objeto runner de HTMLTestRunner
    runner = HTMLTestRunner(
        stream=archivo_salida, #Para que el informe se guarde en el archivo que generamos en la varibale archivo_salida
        verbosity=2, #El parámetro verbosity se establece en 2, lo que significa que se mostrarán detalles adicionales en el informe.
    )

    #Ejecutamos la suite de pruebas
    suite = unittest.TestLoader().loadTestsFromTestCase(CerrarSesion)
    runner.run(suite)

    #Cerramos el archivo de salida
    archivo_salida.close()