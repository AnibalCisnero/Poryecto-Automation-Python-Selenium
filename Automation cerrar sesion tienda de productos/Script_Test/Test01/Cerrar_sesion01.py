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
     
        
     def test_Verificar_laPrecencia_Logout(self):
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
        element.screenshot(r'C:\Users\54373\Desktop\Automation cerrar sesion tienda de productos\Captura cerrar sesion.png')
     
     def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
     #Abrimos el archivo de salida con la funcion open() lo utilizamos para abrir un archivo en modo de escritura
    archivo_salida = open('Reporte del caso de prueba (Cerrar Sesion 01).html', 'w')

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