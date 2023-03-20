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
        
    def test_redireccion(self):
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
        
    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    #Abrimos el archivo de salida con la funcion open() lo utilizamos para abrir un archivo en modo de escritura
    archivo_salida = open('Reporte del caso de prueba (Cerrar Sesion 04).html', 'w')

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