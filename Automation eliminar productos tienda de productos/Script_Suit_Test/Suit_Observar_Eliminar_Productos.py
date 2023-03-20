import unittest
import logging
from HtmlTestRunner import HTMLTestRunner
from selenium import webdriver
from reportlab.pdfgen import canvas
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#configuramos el logger básico para que registre los mensajes en un archivo de registro (en este caso, 'test.log')
# solo se registrarán mensajes con un nivel de ERROR o superior.
logging.basicConfig(filename='test.log', level=logging.ERROR)
class Suit_Observar_Eliminar_Productos(unittest.TestCase):
     
    def setUp(self):
        #Inicializamos el driver
        self.driver = webdriver.Chrome()
     
    def test_Eliminar_Un_Producto(self):
      
      try:
         # Navegar a la página de Demoblaze
        self.driver.get("https://www.demoblaze.com/index.html")
        self.driver.maximize_window()
        time.sleep(10)

        Monitores = self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div[1]/div/a[4]')
        Monitores.click()
        
        # Esperar hasta que aparezcan los productos de Monitores 
        WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='contcont']/div/div[2]"))
        )
        time.sleep(10)

        producto_mon = self.driver.find_element(By.XPATH,'//*[@id="tbodyid"]/div[1]/div/a')
        producto_mon.click()
        time.sleep(10)
        #Esperar hasta que carge la pagina de detalles
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[5]'))
            )
        
        time.sleep(10)
        #Hacemos click en boton añadir al carrito
        button_carrito = self.driver.find_element(By.XPATH, '//*[@id="tbodyid"]/div[2]/div/a')
        button_carrito.click()
        time.sleep(10)
        #Capturamos y aceptamos el alert
        alert = self.driver.switch_to.alert#Capturo el alert
        alert.accept()
        time.sleep(20)
        #Hacemos click en boton cart 
        carrito = self.driver.find_element(By.ID,'cartur')
        carrito.click()
        #Esperamos a que carge la pagina del carrito
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID,'page-wrapper'))
        )
        time.sleep(10)
        #Borramos el producto
        delete = self.driver.find_element(By.XPATH,'//*[@id="tbodyid"]/tr/td[4]/a')
        delete.click()
        time.sleep(10)
       

        pass
      #En resumen, esta línea se encarga de registrar cualquier excepción que se produzca
      #durante la ejecución de la prueba, lo que facilita el proceso de depuración y solución de problemas.
      except Exception as e:
               logging.exception("Error en la prueba 'test_Elimar_Un_Productos")

    def test_Eliminar_varios_Productos(self):
        try:
              # Navegar a la página de Demoblaze
           self.driver.get("https://www.demoblaze.com/index.html#")
           self.driver.maximize_window()
           time.sleep(10)

        # Hacer click en Phone
           Phones = self.driver.find_element(By.ID, ('itemc'))
           Phones.click()
           time.sleep(10)

# Esperar hasta que aparezcan los productos de Phone
           WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[@id='tbodyid']/div"))
                )

           producto_Phone = self.driver.find_element(By.XPATH,'//*[@id="tbodyid"]/div[1]/div/a')
           producto_Phone.click()
           time.sleep(10)


         #Esperar hasta que carge la pagina de detalles
           WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/div[5]'))
              )
        
           time.sleep(10)
           button_carrito = self.driver.find_element(By.XPATH, '//*[@id="tbodyid"]/div[2]/div/a')
           button_carrito.click()
           time.sleep(10)

           alert = self.driver.switch_to.alert#Capturo el alert
           alert.accept()
           time.sleep(20)
           self.driver.back()
           self.driver.back()

           time.sleep(15)
           laptop = self.driver.find_element(By.XPATH,'/html/body/div[5]/div/div[1]/div/a[3]')
           laptop.click()

           WebDriverWait(self.driver, 10).until(
               EC.presence_of_element_located((By.XPATH, "//div[@id='tbodyid']/div"))
            )
           time.sleep(10)

           producto_Laptop = self.driver.find_element(By.XPATH,'//*[@id="tbodyid"]/div[1]/div/a')
           producto_Laptop.click()
           time.sleep(10)

        #Esperar hasta que carge la pagina de detalles
           WebDriverWait(self.driver, 10).until(
              EC.presence_of_element_located((By.XPATH, '/html/body/div[5]'))
            )
        
           time.sleep(10)
           button_carrito = self.driver.find_element(By.XPATH, '//*[@id="tbodyid"]/div[2]/div/a')
           button_carrito.click()
           time.sleep(10)

           alert = self.driver.switch_to.alert#Capturo el alert
           alert.accept()
           time.sleep(20)
           self.driver.back()
           self.driver.back()
           time.sleep(15)

           Monitores = self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div[1]/div/a[4]')
           Monitores.click()
        
        # Esperar hasta que aparezcan los productos de Monitores 
           WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='contcont']/div/div[2]"))
           )
           time.sleep(10)

           producto_mon = self.driver.find_element(By.XPATH,'//*[@id="tbodyid"]/div[1]/div/a')
           producto_mon.click()
           time.sleep(10)
        #Esperar hasta que carge la pagina de detalles
           WebDriverWait(self.driver, 10).until(
               EC.presence_of_element_located((By.XPATH, '/html/body/div[5]'))
            )
        
           time.sleep(10)
           button_carrito = self.driver.find_element(By.XPATH, '//*[@id="tbodyid"]/div[2]/div/a')
           button_carrito.click()
           time.sleep(10)

           alert = self.driver.switch_to.alert#Capturo el alert
           alert.accept()
           time.sleep(20)
           self.driver.back()
           self.driver.back()


           carrito = self.driver.find_element(By.ID,'cartur')
           carrito.click()

           WebDriverWait(self.driver, 10).until(
              EC.presence_of_element_located((By.ID,'page-wrapper'))
           )
           time.sleep(10)

           delete = self.driver.find_element(By.XPATH,'//*[@id="tbodyid"]/tr/td[4]/a')
           delete.click()
           time.sleep(10)

           delete = self.driver.find_element(By.XPATH,'//*[@id="tbodyid"]/tr/td[4]/a')
           delete.click()
           time.sleep(10)

           delete = self.driver.find_element(By.XPATH,'//*[@id="tbodyid"]/tr/td[4]/a')
           delete.click()
           time.sleep(10)
           pass

        except Exception as e:
               logging.exception("Error en la prueba 'test_Eliminar_varios_Productos")
     
    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
         # Abrimos el archivo de salida
    archivo_salida = open('reporte de la suit de pruebas Eliminar productos del Carrito.html', 'w')

    # Creamos un objeto runner de HTMLTestRunner
    runner = HTMLTestRunner(
        stream=archivo_salida,
        verbosity=2,
    )

    # Ejecutamos la suite de pruebas
    suite = unittest.TestLoader().loadTestsFromTestCase(Suit_Observar_Eliminar_Productos)
    runner.run(suite)

    # Cerramos el archivo de salida
    archivo_salida.close()