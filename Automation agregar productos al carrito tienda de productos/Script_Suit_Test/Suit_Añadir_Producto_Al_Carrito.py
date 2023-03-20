import unittest
import logging
from HtmlTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

#configuramos el logger básico para que registre los mensajes en un archivo de registro (en este caso, 'test.log')
#solo se registrarán mensajes con un nivel de ERROR o superior.
logging.basicConfig(filename='test.log', level=logging.ERROR)

class Suit_AñadirProductosCarrito(unittest.TestCase):
     def setUp(self):
        self.driver = webdriver.Chrome()

     def test_Agregar_un_Producto(self):
      try:
        self.driver.get("https://www.demoblaze.com/index.html")
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
        self.driver.quit()
        time.sleep(5)
        pass
      #En resumen, esta línea se encarga de registrar cualquier excepción que se produzca
      #durante la ejecución de la prueba, lo que facilita el proceso de depuración y solución de problemas.
      except Exception as e:
               logging.exception("Error en la prueba 'Suit_AñadirProductosCarrito'")

     
     def test_Agregar_Varios_Productos(self):
      try:
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
        self.driver.quit()
        time.sleep(5)
        pass
      #En resumen, esta línea se encarga de registrar cualquier excepción que se produzca
      #durante la ejecución de la prueba, lo que facilita el proceso de depuración y solución de problemas.
      except Exception as e:
               logging.exception("Error en la prueba 'test_Agregar_Varios_Productos'")


     def test_Agrgear_Mismo_Producto(self):
      try:
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
        #Capturo y acepto el alert
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
        self.driver.quit()
        time.sleep(5)
        pass
      #En resumen, esta línea se encarga de registrar cualquier excepción que se produzca
      #durante la ejecución de la prueba, lo que facilita el proceso de depuración y solución de problemas.
      except Exception as e:
               logging.exception("Error en la prueba ' test_Agrgear_Mismo_Producto'")


     def test_Funcionamiento_boton_AñadirAlCarrito(self):
      try:
        # Navegar a la página de Demoblaze
        self.driver.get("https://www.demoblaze.com/index.html")
        self.driver.maximize_window()
        time.sleep(10)

        # Esperar a que se cargue la página y hacer click en el primer producto
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h4/a[text()='Samsung galaxy s6']"))).click()

        # Esperar a que se cargue la página del producto y hacer click en el botón "Añadir a la cesta"
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Add to cart']"))).click()
        
        time.sleep(10)
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        print(f"Product added Alert Text: {alert_text}")
        alert.accept()
        time.sleep(10)

        carrito = self.driver.find_element(By.ID, "cartur")
        carrito.click()
        time.sleep(20)

        productos = self.driver.find_elements(By.XPATH, "//tbody/tr")
        time.sleep(10)
        assert len(productos) == 1, f"Solo se han agregado {len(productos)} productos al carrito."
        time.sleep(10)
        self.driver.save_screenshot("Producto.png")
        self.driver.quit()
        time.sleep(5)
        pass
      #En resumen, esta línea se encarga de registrar cualquier excepción que se produzca
      #durante la ejecución de la prueba, lo que facilita el proceso de depuración y solución de problemas.
      except Exception as e:
               logging.exception("Error en la prueba 'test_Funcionamiento_boton_AñadirAlCarrito'")


     def test_Captura_PopUp(self):
      try:
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
        self.driver.quit()
        time.sleep(5)
        pass
      #En resumen, esta línea se encarga de registrar cualquier excepción que se produzca
      #durante la ejecución de la prueba, lo que facilita el proceso de depuración y solución de problemas.
      except Exception as e:
               logging.exception("Error en la prueba 'test_Captura_PopUp'")


     def test_Funcionamiento_boton_Cart(self):
      try:
        # Navegar a la página de Demoblaze
        self.driver.get("https://www.demoblaze.com/index.html")
        self.driver.maximize_window()
        time.sleep(10)

        # Esperar a que se cargue la página y hacer click en el boton Cart
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="navbarExample"]/ul/li[4]'))).click()
        time.sleep(10)
        self.driver.quit()
        time.sleep(5)
        pass
      #En resumen, esta línea se encarga de registrar cualquier excepción que se produzca
      #durante la ejecución de la prueba, lo que facilita el proceso de depuración y solución de problemas.
      except Exception as e:
               logging.exception("Error en la prueba 'test_Funcionamiento_boton_Cart'")


     def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
        #Abrimos el archivo de salida con la funcion open() lo utilizamos para abrir un archivo en modo de escritura
    archivo_salida = open('Reporte de la Suit Añadir productos al carrito.html', 'w')

    #Creamos un objeto runner de HTMLTestRunner
    runner = HTMLTestRunner(
        stream=archivo_salida, #Para que el informe se guarde en el archivo que generamos en la varibale archivo_salida
        verbosity=2, #El parámetro verbosity se establece en 2, lo que significa que se mostrarán detalles adicionales en el informe.
    )

    #Ejecutamos la suite de pruebas
    suite = unittest.TestLoader().loadTestsFromTestCase(Suit_AñadirProductosCarrito)
    runner.run(suite)

    #Cerramos el archivo de salida
    archivo_salida.close()