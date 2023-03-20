import unittest
from HtmlTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class AñadirProductosCarrito(unittest.TestCase):
     
     def setUp(self):
        #Inicializamos el driver
        self.driver = webdriver.Chrome()

     def test_Captura_PopUp(self):
        # Navegar a la página de Demoblaze
        self.driver.get("https://www.demoblaze.com/index.html")
        self.driver.maximize_window()
        time.sleep(10)

        # Esperar a que se cargue la página y hacer click en el primer producto
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h4/a[text()='Samsung galaxy s6']"))).click()

        # Esperar a que se cargue la página del producto y hacer click en el botón "Añadir a la cesta"
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Add to cart']"))).click()
        #Capturp acepto e imprimos el alert
        time.sleep(10)
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        print(f"Product added Alert Text: {alert_text}")
        alert.accept()
        time.sleep(10)

     def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    #Abrimos el archivo de salida con la funcion open() lo utilizamos para abrir un archivo en modo de escritura
    archivo_salida = open('Reporte del test 05.html', 'w')

    #Creamos un objeto runner de HTMLTestRunner
    runner = HTMLTestRunner(
        stream=archivo_salida, #Para que el informe se guarde en el archivo que generamos en la varibale archivo_salida
        verbosity=2, #El parámetro verbosity se establece en 2, lo que significa que se mostrarán detalles adicionales en el informe.
    )

    #Ejecutamos la suite de pruebas
    suite = unittest.TestLoader().loadTestsFromTestCase(AñadirProductosCarrito)
    runner.run(suite)

    #Cerramos el archivo de salida
    archivo_salida.close()