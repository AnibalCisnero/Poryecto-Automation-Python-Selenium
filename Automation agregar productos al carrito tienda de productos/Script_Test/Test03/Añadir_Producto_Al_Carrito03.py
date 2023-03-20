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

     def test_Agregar_Mismo_Producto(self):
        # Navegar a la página de Demoblaze
        self.driver.get("https://www.demoblaze.com/index.html")
        self.driver.maximize_window()
        time.sleep(10)
        #Selecciono la categoria Laptop
        cat_laptop = self.driver.find_element(By.XPATH,'/html/body/div[5]/div/div[1]/div/a[3]')
        cat_laptop.click()
        time.sleep(10)
        #Selecciono el producto 
        Sony = self.driver.find_element(By.XPATH,'/html/body/div[5]/div/div[2]/div/div[1]/div/a')
        Sony.click()
        time.sleep(10)
        #Click en el boton añadir al carrito
        button_añadir = self.driver.find_element(By.XPATH,'/html/body/div[5]/div/div[2]/div[2]/div/a')
        button_añadir.click()
        time.sleep(10)
        #Capturo y acepto el alert
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        print(f"Product added Alert Text: {alert_text}")
        alert.accept()
        time.sleep(10)
        #Vuelvo a hacer click en el boton añadir al carrito 
        button_añadir = self.driver.find_element(By.XPATH,'/html/body/div[5]/div/div[2]/div[2]/div/a')
        button_añadir.click()
        time.sleep(10)
        #Capturo y acepto el alert
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        print(f"Product added Alert Text: {alert_text}")
        alert.accept()
        time.sleep(10)
        #Ago click nuevamente en el boton añadir al carrito
        button_añadir = self.driver.find_element(By.XPATH,'/html/body/div[5]/div/div[2]/div[2]/div/a')
        button_añadir.click()
        time.sleep(10)
        #Capturo ya acepto el alert
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        print(f"Product added Alert Text: {alert_text}")
        alert.accept()
        time.sleep(10)
        #Ir al carrito de compras y verificar que los producto se agregaron
        carrito = self.driver.find_element(By.ID, "cartur")
        carrito.click()
        time.sleep(20)
        #Verificamos que los productos se ayan agregado al carrito 
        productos = self.driver.find_elements(By.XPATH, "//tbody/tr")
        time.sleep(10)
        assert len(productos) == 3, f"Solo se han agregado {len(productos)} productos al carrito."
        time.sleep(10)
        #Capturo evidencia
        self.driver.save_screenshot("Producto_Repetido.png")

     def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
     #Abrimos el archivo de salida con la funcion open() lo utilizamos para abrir un archivo en modo de escritura
    archivo_salida = open('Reporte del test 03.html', 'w')

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