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

     def test_Agregar_Varios_Productos(self):
        # Navegar a la página de Demoblaze
        self.driver.get("https://www.demoblaze.com/index.html")
        time.sleep(10)

        # Agregar el primer producto a la carrito de compras
        samsung = self.driver.find_element(By.XPATH, '//*[@id="tbodyid"]/div[1]/div/a')
        samsung.click()
        time.sleep(10)
        button_añadir = self.driver.find_element(By.XPATH,'/html/body/div[5]/div/div[2]/div[2]/div/a')
        button_añadir.click()
        time.sleep(10)
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        print(f"Product added Alert Text: {alert_text}")
        alert.accept()
        boton_inicio = self.driver.find_element(By.XPATH,'/html/body/nav/div/div/ul/li[1]')
        boton_inicio.click()
        time.sleep(10)

        # Agregar el segundo producto a la carrito de compras
        time.sleep(30)
        Nokia = self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/div/div[2]/div/a')
        Nokia.click()
        time.sleep(10)
        button_añadir = self.driver.find_element(By.XPATH,'/html/body/div[5]/div/div[2]/div[2]/div/a')
        button_añadir.click()
        time.sleep(20)
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        print(f"Product added Alert Text: {alert_text}")
        alert.accept()
        time.sleep(10)
        boton_inicio = self.driver.find_element(By.XPATH,'/html/body/nav/div/div/ul/li[1]')
        boton_inicio.click()
        time.sleep(10)

        # Agregar el tercer producto a la carrito de compras
        HTC = self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/div/div[7]/div/a/img')
        HTC.click()
        time.sleep(10)
        button_añadir = self.driver.find_element(By.XPATH,'/html/body/div[5]/div/div[2]/div[2]/div/a')
        button_añadir.click()
        time.sleep(10)
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        print(f"Product added Alert Text: {alert_text}")
        alert.accept()
        time.sleep(10)
        #Ir al carrito de compras y verificar que se hayan agregado los productos
        carrito = self.driver.find_element(By.ID, "cartur")
        carrito.click()
        time.sleep(20)
        #Verificamos que los productos se ayan agregado al carrito 
        productos = self.driver.find_elements(By.XPATH, "//tbody/tr")
        time.sleep(10)
        assert len(productos) == 3, f"Solo se han agregado {len(productos)} productos al carrito."
        time.sleep(10)
        #Tomamos evidencia
        self.driver.save_screenshot("Productos_Agregados.png")

     def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
     #Abrimos el archivo de salida con la funcion open() lo utilizamos para abrir un archivo en modo de escritura
    archivo_salida = open('Reporte del test 02.html', 'w')

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
 