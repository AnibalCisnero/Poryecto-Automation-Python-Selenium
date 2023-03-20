import unittest
from HtmlTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class AñadirProductosCarrito(unittest.TestCase):
     def setUp(self):
        self.driver = webdriver.Chrome()
     
        
     def test_Agregar_un_Producto(self):
        self.driver.get("https://www.demoblaze.com/index.html")
        self.driver.maximize_window()
        time.sleep(10)
        #Elijo un producto y hago click en el mismo para agregarlo al carrito
        producto = self.driver.find_element(By.XPATH,'//*[@id="tbodyid"]/div[1]/div/a')
        producto.click()
        time.sleep(10)
        #Hago click en el boton añadir al carrito
        button_añadir = self.driver.find_element(By.XPATH,'/html/body/div[5]/div/div[2]/div[2]/div/a')
        button_añadir.click()
        time.sleep(10)
        #Capturo y acepto el alert para que el producto se agrege al carrito
        alert = self.driver.switch_to.alert
        alert.accept()
        time.sleep(10)
        #Hago click en el boton carrito para dirigirme a la pagina del mismo y verificar que se agrege el producto
        carrito = self.driver.find_element(By.ID,'cartur')
        carrito.click()
        time.sleep(10)
        #Capturo con una imagen la evidencia
        self.driver.save_screenshot("producto_agregado.png")


     def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
        #Abrimos el archivo de salida con la funcion open() lo utilizamos para abrir un archivo en modo de escritura
    archivo_salida = open('Reporte del test 01.html', 'w')

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